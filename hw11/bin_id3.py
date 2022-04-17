import csv
from math import log2
import copy

from attr import attr

##################################################
# module: bin_id3.py
# description: Binary ID3 decision tree learning
# Carson Fox
# A02251670
# bugs to vladimir kulyukin on canvas
###################################################

### Positive and Negative Constant labels; don't change
### these.
PLUS = "Yes"
MINUS = "No"


class id3_node(object):
    def __init__(self, lbl):
        self.__label = lbl
        self.__children = {}

    def set_label(self, lbl):
        self.__label = lbl

    def add_child(self, attrib_val, node):
        self.__children[attrib_val] = node

    def get_label(self):
        return self.__label

    def get_children(self):
        return self.__children

    def get_child(self, attrib_val):
        assert attrib_val in self.__children
        return self.__children[attrib_val]


class bin_id3(object):
    @staticmethod
    def get_attrib_values(a, kvt):
        """
        Looks up values of attribute a in key-value table.
        """
        return kvt[a]

    @staticmethod
    def get_example_attrib_val(example, attrib):
        """
        Get the value of attribute attrib in example.
        """
        assert attrib in example
        return example[attrib]

    @staticmethod
    def parse_csv_file_into_examples(csv_fp):
        """
        Takes a csv file specified by the path csv_fp and
        converts it into an array of examples, each of which
        is a dictionary of key-value pairs where keys are
        column names and the values are column attributes.
        """
        examples = []
        with open(csv_fp) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0
            key_names = None
            for row in csv_reader:
                if len(row) == 0:
                    continue
                if line_count == 0:
                    key_names = row
                    for i in range(len(key_names)):
                        ## strip whitespace on both ends.
                        row[i] = row[i].strip()
                        line_count += 1
                else:
                    ex = {}
                    for i, k in enumerate(key_names):
                        ## strip white spaces on both ends.
                        ex[k] = row[i].strip()
                    examples.append(ex)
            return examples, key_names

    @staticmethod
    def construct_attrib_values_from_examples(examples, attributes):
        """
        Constructs a dictionary from a list of examples where each attribute
        is mapped to a list of all its possible values in examples.
        """
        avt = {}
        for a in attributes:
            if not a in avt:
                avt[a] = set()
            for ex in examples:
                if a in ex:
                    if not ex[a] in avt[a]:
                        avt[a].add(ex[a])
                else:
                    avt[a].add(None)
        return avt

    @staticmethod
    def find_examples_given_attrib_val(examples, attrib, val):
        """
        Finds all examples in such that attrib = val.
        """
        rslt = []
        # print('Looking for examples where {}={}'.format(attrib, val))
        for ex in examples:
            if attrib in ex:
                if ex[attrib] == val:
                    rslt.append(ex)
        return rslt

    @staticmethod
    def find_most_common_attrib_val(examples, attrib, avt):
        """
        Finds the most common value of attribute attrib in examples.
        """
        attrib_vals = bin_id3.get_attrib_values(attrib, avt)
        val_counts = {}
        for av in attrib_vals:
            SV = bin_id3.find_examples_given_attrib_val(examples, attrib, av)
            val_counts[av] = len(SV)
        max_cnt = 0
        max_val = None
        # print('val_counts = {}'.format(val_counts))
        for val, cnt in val_counts.items():
            if cnt > max_cnt:
                max_cnt = cnt
                max_val = val
        assert max_val != None
        return max_val, max_cnt

    @staticmethod
    def get_non_target_attributes(target_attrib, attribs):
        """
        Returns a comma separated string of all attributes in the list attribs that
        that are not equal to target_attrib;
        - target_attrib is a string.
        - attribs is a list of strings.
        """
        return ", ".join([a for a in attribs if a != target_attrib])

    @staticmethod
    def display_info_gains(gains):
        """
        Displays a dictionary of information gains in the format attribute: gain.
        """
        print("Information gains are as follows:")
        for attrib, gain in gains.items():
            print("\t{}: {}".format(attrib, gain))

    @staticmethod
    def display_id3_node(node, tabs):
        """
        Displays the subtree rooted at a node.
        """
        print(tabs + "{}".format(node.get_label()))
        children = node.get_children()
        for v, n in children.items():
            print(tabs + "\t{}".format(v))
            bin_id3.display_id3_node(n, tabs + "\t\t")

    @staticmethod
    def proportion(examples, attrib, val):
        """
        Computes the proportion of examples whose attribute attrib has the value val.
        """
        if len(examples) == 0:
            return 0
        return len(bin_id3.find_examples_given_attrib_val(examples, attrib, val)) / len(
            examples
        )

    @staticmethod
    def entropy(examples, attrib, avt):
        """
        Computes entropy of examples with respect of attribute attrib.
        avt is the attribute value table computed by construct_attrib_values_from_examples().
        """
        proportions = (bin_id3.proportion(examples, attrib, val) for val in avt[attrib])
        return -sum(p * log2(p) for p in proportions if p != 0)

    @staticmethod
    def gain(examples, target_attrib, attrib, avt):
        """
        Computes gain of the attribute attrib in examples.
        """
        entropy = bin_id3.entropy(examples, target_attrib, avt)

        def reduction(val):
            split = bin_id3.find_examples_given_attrib_val(examples, attrib, val)
            return (
                len(split) / len(examples) * bin_id3.entropy(split, target_attrib, avt)
            )

        return entropy - sum(map(reduction, avt[attrib]))

    @staticmethod
    def find_best_attribute(examples, target_attrib, attribs, avt):
        """
        Finds the attribute in attribs with the highest information gain.
        This method returns three values: best attribute, its gain, and
        a dictionary that maps each attribute to its gain.
        """
        gains = {
            attrib: bin_id3.gain(examples, target_attrib, attrib, avt)
            for attrib in attribs
            if attrib != target_attrib
        }
        best_attrib, best_gain = max(gains.items(), key=lambda pair: pair[1])
        return best_attrib, best_gain, gains

    @staticmethod
    def fit(examples, target_attrib, attribs, avt, dbg):
        """
        Returns a decision tree from examples given target_attribute target_attrib,
        attributes attribs, and attribute-value table.
        - examples is a list of examples;
        - target_attrib is a string (e.g., 'PlayTennis')
        - attribs is a list of attributes (strings)
        - avt is a dictionary constructed by construct_attrib_values_from_examples()
        - dbg is a debug flag True/False. When it is true, then things should
          be printed out as the algorithm computes the decision tree. For example,
          in my implementation I have things like
          if len(SV) == len(examples):
            ## if all examples are positive, then return the root node whose label is PLUS.
            if dbg == True:
                print('All examples positive...')
                print('Setting label of root to {}'.format(PLUS))
            root.set_label(PLUS)
            return root
        """
        global PLUS
        global MINUS

        posExamples = bin_id3.find_examples_given_attrib_val(
            examples, target_attrib, PLUS
        )
        if len(posExamples) == len(examples):
            return id3_node(PLUS)

        negExamples = bin_id3.find_examples_given_attrib_val(
            examples, target_attrib, MINUS
        )
        if len(negExamples) == len(examples):
            return id3_node(MINUS)

        # Don't count target attribute
        if len(attribs) == 1:
            return id3_node(
                bin_id3.find_most_common_attrib_val(examples, target_attrib, avt)[0]
            )

        return bin_id3.split_on_best_attrib(examples, target_attrib, attribs, avt, dbg)

    @staticmethod
    def split_on_best_attrib(examples, target_attrib, attribs, avt, dbg):
        best_attrib, _, _ = bin_id3.find_best_attribute(
            examples, target_attrib, attribs, avt
        )
        root = id3_node(best_attrib)

        for val in avt[best_attrib]:
            split = bin_id3.find_examples_given_attrib_val(examples, best_attrib, val)

            if len(split) == 0:
                child = id3_node(
                    bin_id3.find_most_common_attrib_val(examples, target_attrib, avt)[0]
                )
            else:
                child = bin_id3.fit(
                    split, target_attrib, attribs - {best_attrib}, avt, dbg
                )
            root.add_child(val, child)

        return root

    @staticmethod
    def predict(root: id3_node, example):
        """
        Classifies an example given a decision tree whose root is root.
        """
        global PLUS
        global MINUS

        if root.get_label() == PLUS:
            return PLUS
        if root.get_label() == MINUS:
            return MINUS

        split_val = example[root.get_label()]
        return bin_id3.predict(root.get_child(split_val), example)
