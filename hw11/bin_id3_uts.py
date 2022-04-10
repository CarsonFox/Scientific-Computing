#############################################################
# module: bin_id3_uts.py
# description: unit tests for bin_id3 class.
# bugs to vladimir kulyukin in canvas
##############################################################

import unittest
from bin_id3 import id3_node
from bin_id3 import bin_id3
from bin_id3 import PLUS, MINUS

class bin_id3_uts(unittest.TestCase):

    def test_id3_ut00(self, tn=0):
        """
        Parses csv file play_tennis.csv into examples and column names.
        Displays all examples.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        attribs    = set(colnames[1:])
        print('attribs = {}'.format(attribs))
        assert len(examples) == 14
        print('Examples:\n')
        for i, ex in enumerate(examples):
            print('{}) {}'.format(i+1, ex))
        print('\nColumn names:')
        for i, cn in enumerate(colnames):
            print('{}) {}'.format(i+1, cn))
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut01(self, tn=1):
        """
        Tests bin_id3.construct_attrib_values_from_examples().
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        print('Attribute --> Values:\n')
        for k, v in avt.items():
            print('{} --> {}'.format(k, v))
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut02(self, tn=2):
        """
        Tests id3_node class and constructs a decision tree manually.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        
        yes_node = id3_node(PLUS)
        assert yes_node.get_label() == PLUS
        no_node = id3_node(MINUS)
        assert no_node.get_label() == MINUS
        humidity_node = id3_node('Humidity')
        assert humidity_node.get_label() == 'Humidity'
        humidity_node.add_child('High', no_node)
        humidity_node.add_child('Normal', yes_node)
        assert humidity_node.get_child('High').get_label() == MINUS
        assert humidity_node.get_child('Normal').get_label() == PLUS
        assert len(humidity_node.get_children()) == 2
        bin_id3.display_id3_node(humidity_node, '')

        wind_node = id3_node('Wind')
        assert wind_node.get_label() == 'Wind'
        wind_node.add_child('Strong', no_node)
        wind_node.add_child('Weak', yes_node)
        assert wind_node.get_child('Strong').get_label() == MINUS
        assert wind_node.get_child('Weak').get_label() == PLUS
        assert len(wind_node.get_children()) == 2
        bin_id3.display_id3_node(wind_node, '')
        
        outlook_node = id3_node('Outlook')
        assert outlook_node.get_label() == 'Outlook'
        outlook_node.add_child('Sunny', humidity_node)
        assert outlook_node.get_child('Sunny').get_label() == 'Humidity'
        outlook_node.add_child('Overcast', yes_node)
        assert outlook_node.get_child('Overcast').get_label() == PLUS
        outlook_node.add_child('Rain', wind_node)
        assert outlook_node.get_child('Rain').get_label() == 'Wind'
        assert len(outlook_node.get_children()) == 3
        bin_id3.display_id3_node(outlook_node, '')
        
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut03(self, tn=3):
        """
        - Finds the examples with Outlook=Sunny;
        - In the examples with Outlook=Sunny finds all examples with PlayTennis=Yes;
        - In the examples with Outlook=Sunny finds all examples with PlayTennis=No.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_sunny_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Sunny')
        print('Examples with Outlook=Sunny:\n')
        for i, ex in enumerate(outlook_sunny_examples):
            print('{}) {}'.format(i+1, ex))
        assert len(bin_id3.find_examples_given_attrib_val(outlook_sunny_examples, 'PlayTennis', 'Yes')) \
            == 2
        assert len(bin_id3.find_examples_given_attrib_val(outlook_sunny_examples, 'PlayTennis', 'No')) \
            == 3
        print('\n============ ID3 UT {} passed ================'.format(tn))        

    def test_id3_ut04(self, tn=4):
        """
       Tests bin_id3.proportion(). What proporition of examples has PlayTennis=Yes.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        attribs    = set(colnames[1:])
        attrib     = 'PlayTennis'
        attrib_val = 'Yes'
        p = bin_id3.proportion(examples, attrib, attrib_val)
        print('proportion({}, {}) = {}'.format(attrib, attrib_val, p))
        gt  = 9.0/14
        err = 0.0001
        assert abs(p - gt) <= err
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut05(self, tn=5):
        """
        Tests bin_id3.proportion(). What proporition of examples has Humidity=High.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        attribs    = set(colnames[1:])
        attrib     = 'Humidity'
        attrib_val = 'High'
        p = bin_id3.proportion(examples, attrib, attrib_val)
        print('proportion({}, {}) = {}'.format(attrib, attrib_val, p))
        gt  = 7.0/14
        err = 0.0001
        assert abs(p - gt) <= err
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut06(self, tn=6):
        """
        Finds entropy of the original examples with respect to target_attribute PlayTennis.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        H = bin_id3.entropy(examples, 'PlayTennis', avt)
        ## ground truth value for Entropy
        gH = 0.9402859586706309
        err = 0.0001
        print('Entropy(S)={}'.format(H))
        assert abs(H - gH) <= err        
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut07(self, tn=7):
        """
        Let S = 
        1) {'Day': 'D1',  'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'}
        2) {'Day': 'D2',  'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'}
        3) {'Day': 'D8',  'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'}
        4) {'Day': 'D9',  'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'}
        5) {'Day': 'D11', 'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'}
        Compute Entropy(S) w/ respect to PlayTennis;
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_sunny_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Sunny')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        H   = bin_id3.entropy(outlook_sunny_examples, 'PlayTennis', avt)
        gH  = 0.9709505944546686
        err = 0.0001
        print('Entropy(S)={}'.format(H))
        assert abs(H - gH) <= err
        print('\n============ ID3 UT {} pass =================='.format(tn))        

    def test_id3_ut08(self, tn=8):
        """
        Computes information gain of Wind in the examples and target_attribute PlayTennis.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        print('bin_id3: avt={}'.format(avt))
        g   = bin_id3.gain(examples, 'PlayTennis', 'Wind', avt)
        gt  = 0.04812703040826927
        err = 0.0001
        print('gain(Wind)={}'.format(g))
        assert abs(g - gt) <= err
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut09(self, tn=9):
        """
        Tests information gain of Humidity in the examples and target_attribute PlayTennis.
        """        
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        g   = bin_id3.gain(examples, 'PlayTennis', 'Humidity', avt)
        gt  = 0.15183550136234136
        err = 0.0001
        print('gain(Humidity)={}'.format(g))
        assert abs(g - gt) <= err
        print('\n============ ID3 UT {} passed ================'.format(tn))


    def test_id3_ut10(self, tn=10):
        """
        Tests information gain of Outlook in the examples and target_attribute PlayTennis.
        """        
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        g   = bin_id3.gain(examples, 'PlayTennis', 'Outlook', avt)
        gt  = 0.2467498197744391
        err = 0.0001
        print('gain(Outlook)={}'.format(g))
        assert abs(g - gt) <= err
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut11(self, tn=11):
        """
        Tests information gain of Temperature in the examples and target_attribute PlayTennis.
        """        
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        g   = bin_id3.gain(examples, 'PlayTennis', 'Temperature', avt)
        gt  = 0.029222565658954647
        err = 0.0001
        print('gain(Temperature)={}'.format(g))
        assert abs(g - gt) <= err
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut12(self, tn=12):
        """
        Find all examples with Outlook=Sunny and compute info gain of Humidity.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_sunny_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Sunny')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        g   = bin_id3.gain(outlook_sunny_examples, 'PlayTennis', 'Humidity', avt)
        gt  = 0.9709505944546686
        err = 0.0001
        print('gain(Humidity)={}'.format(g))
        assert abs(g - gt) <= err
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut13(self, tn=13):
        """
        Find all examples with Outlook=Sunny and compute info gain of Temperature.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_sunny_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Sunny')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        g   = bin_id3.gain(outlook_sunny_examples, 'PlayTennis', 'Temperature', avt)
        gt  = 0.5709505944546686
        err = 0.0001
        print('gain(Temperature)={}'.format(g))
        assert abs(g - gt) <= err
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut14(self, tn=14):
        """
        Find all examples with Outlook=Sunny and compute info gain of Wind.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_sunny_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Sunny')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        g   = bin_id3.gain(outlook_sunny_examples, 'PlayTennis', 'Wind', avt)
        gt  = 0.01997309402197489
        err = 0.0001
        print('gain(Wind)={}'.format(g))
        assert abs(g - gt) <= err
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut15(self, tn=15):
        """
        Find all examples with Outlook=Overcast and check that those examples consist of
        4 postive examples and 0 negative examples.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_over_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Overcast')
        print('Examples with Outlook=Overcast:\n')
        for i, ex in enumerate(outlook_over_examples):
            print('{}) {}'.format(i+1, ex))
        assert len(bin_id3.find_examples_given_attrib_val(outlook_over_examples, 'PlayTennis', 'Yes')) == 4
        assert len(bin_id3.find_examples_given_attrib_val(outlook_over_examples, 'PlayTennis', 'No')) == 0        
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut16(self, tn=16):
        """
        Find all examples with Outlook=Overcast and compute info gain of Humidity.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_over_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Overcast')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])        
        g   = bin_id3.gain(outlook_over_examples, 'PlayTennis', 'Humidity', avt)
        gt  = 0.00
        err = 0.0001
        print('gain(Humidity)={}'.format(g))
        assert abs(g - gt) <= err
        print('\n============ ID3 UT {} passed ================'.format(tn))
        
    def test_id3_ut17(self, tn=17):
        """
        Find all examples with Outlook=Overcast and compute info gain of Temperature.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_over_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Overcast')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])        
        g   = bin_id3.gain(outlook_over_examples, 'PlayTennis', 'Temperature', avt)
        gt  = 0.0
        err = 0.0001
        print('gain(Temperature)={}'.format(g))
        assert abs(g - gt) <= err
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut18(self, tn=18):
        """
        Find all examples with Outlook=Overcast and compute info gain of Wind.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_over_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Overcast')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])        
        g   = bin_id3.gain(outlook_over_examples, 'PlayTennis', 'Wind', avt)
        gt  = 0.0
        err = 0.0001
        print('gain(Wind)={}'.format(g))
        assert abs(g - gt) <= err
        print('\n============ ID3 UT {} passed ================'.format(tn))
        
    def test_id3_ut19(self, tn=19):
        """
        Find all examples with Outlook=Rain and check that they include 3 positive and 2 negative
        examples.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_rain_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Rain')
        print('Examples with Outlook=Rain:\n')
        for i, ex in enumerate(outlook_rain_examples):
            print('{}) {}'.format(i+1, ex))
        assert len(bin_id3.find_examples_given_attrib_val(outlook_rain_examples, 'PlayTennis', 'Yes')) == 3
        assert len(bin_id3.find_examples_given_attrib_val(outlook_rain_examples, 'PlayTennis', 'No')) == 2        
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut20(self, tn=20):
        """
        Let S = 
        1) {'Day': 'D1',  'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'}
        2) {'Day': 'D2',  'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'}
        3) {'Day': 'D8',  'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'}
        4) {'Day': 'D9',  'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'}
        5) {'Day': 'D11', 'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'}
        Compute 
        1) Entropy(S);
        2) Gain(Temperature);
        3) Gain(Humidity);
        4) Gain(Wind);
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_sunny_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Sunny')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        H   = bin_id3.entropy(outlook_sunny_examples, 'PlayTennis', avt)
        gH  = 0.9709505944546686
        err = 0.0001
        print('Entropy(S)={}'.format(H))
        assert abs(H - gH) <= err
        g   = bin_id3.gain(outlook_sunny_examples, 'PlayTennis', 'Temperature', avt)
        gt  = 0.5709505944546686
        err = 0.0001
        print('gain(Temperature)={}'.format(g))
        assert abs(g-gt) <= err
        g   = bin_id3.gain(outlook_sunny_examples, 'PlayTennis', 'Humidity', avt)
        gt  = 0.9709505944546686
        err = 0.0001
        print('gain(Humidity)={}'.format(g))
        assert abs(g-gt) <= err
        g   = bin_id3.gain(outlook_sunny_examples, 'PlayTennis', 'Wind', avt)
        gt  = 0.01997309402197489
        err = 0.0001
        print('gain(Wind)={}'.format(g))
        assert abs(g-gt) <= err
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut21(self, tn=21):
        """
        Let S = 
        1) {'Day': 'D1',  'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'}
        2) {'Day': 'D2',  'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'PlayTennis': 'No'}
        3) {'Day': 'D8',  'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'PlayTennis': 'No'}
        4) {'Day': 'D9',  'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'PlayTennis': 'Yes'}
        5) {'Day': 'D11', 'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Strong', 'PlayTennis': 'Yes'}

        Find most common value for attribute PlayTennis
        Find most common value for attribute Humdity
        Find most common value for attribute Wind
        Find most common value for attribute Temperature
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        outlook_sunny_examples = bin_id3.find_examples_given_attrib_val(examples, 'Outlook', 'Sunny')
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        atv, cnt = bin_id3.find_most_common_attrib_val(outlook_sunny_examples, 'PlayTennis', avt)
        assert atv == 'No'
        assert cnt == 3
        atv, cnt = bin_id3.find_most_common_attrib_val(outlook_sunny_examples, 'Humidity', avt)
        assert atv == 'High'
        assert cnt == 3
        atv, cnt = bin_id3.find_most_common_attrib_val(outlook_sunny_examples, 'Wind', avt)
        assert atv == 'Weak'
        assert cnt == 3
        atv, cnt = bin_id3.find_most_common_attrib_val(outlook_sunny_examples, 'Temperature', avt)
        assert atv == 'Hot' or atv == 'Mild'
        assert cnt == 2
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut22(self, tn=22):
        """
        Find best (i.e., highest info gain) attribute in original Examples and display its
        info gain and the gains all the other attributes.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        attribs    = set(colnames[1:])
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        ba, bag, gs = bin_id3.find_best_attribute(examples, 'PlayTennis', attribs, avt)
        assert ba == 'Outlook'
        gt  = 0.2467498197744391
        err = 0.0001
        assert abs(bag - gt) <= err
        bin_id3.display_info_gains(gs)
        print('Best Attribute = {}'.format(ba))
        print('Best Gain      = {}'.format(bag))
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut23(self, tn=23):
        """
        Fit a decision tree with Binary ID3 to labeled examples and display it.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        attribs = set(colnames[1:])
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        target_attrib = 'PlayTennis'
        root = bin_id3.fit(examples, target_attrib, attribs, avt, True)   
        bin_id3.display_id3_node(root, '')
        print('\n============ ID3 UT {} passed ================'.format(tn))

    def test_id3_ut24(self, tn=24):
        """
        Fit a decision tree with Binary ID3 to 14 labeled examples; 
        Predict labels of the same 14 examples with the target attribute values
        removed (such examples are called unlabeled).
        The unlabeled examples are loaded from play_tennis_unlbl.csv.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        global PLUS
        global MINUS
        ### Let's learn a DT.
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        attribs = set(colnames[1:])
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        target_attrib = 'PlayTennis'
        dtr = bin_id3.fit(examples, target_attrib, attribs, avt, True)   
        bin_id3.display_id3_node(dtr, '')

        ### Let's load unlabeled examples
        unlbl_examples, unlbl_colnames = bin_id3.parse_csv_file_into_examples('play_tennis_unlbl.csv')
        print(len(unlbl_examples))
        print('Unlabeled Examples:\n')
        for i, ex in enumerate(unlbl_examples):
            print('{}) {}'.format(i+1, ex))
        print('\nColumn names:')
        for i, cn in enumerate(unlbl_colnames):
            print('{}) {}'.format(i+1, cn))

        prediction = bin_id3.predict(dtr, unlbl_examples[0])
        assert prediction == MINUS
        prediction = bin_id3.predict(dtr, unlbl_examples[1])
        assert prediction == MINUS
        prediction = bin_id3.predict(dtr, unlbl_examples[2])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[3])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[4])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[5])
        assert prediction == MINUS
        prediction = bin_id3.predict(dtr, unlbl_examples[6])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[7])
        assert prediction == MINUS
        prediction = bin_id3.predict(dtr, unlbl_examples[8])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[9])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[10])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[11])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[12])
        assert prediction == PLUS
        prediction = bin_id3.predict(dtr, unlbl_examples[13])
        assert prediction == MINUS
        print('\n============ ID3 UT {} passed ================'.format(tn))

    ### test predict
    def test_id3_ut25(self, tn=25):
        """
        Tests the DT on play_tennis_data.csv and play_tennis_target.txt.
        play_tennis_data.csv contains 1000 examples whose target values are given
        in play_tennis_target.txt.
        """
        print('\n============ ID3 UT {} ======================='.format(tn))
        examples, colnames = bin_id3.parse_csv_file_into_examples('play_tennis.csv')
        attribs = set(colnames[1:])
        avt = bin_id3.construct_attrib_values_from_examples(examples, colnames[1:])
        target_attrib = 'PlayTennis'
        dtr = bin_id3.fit(examples, target_attrib, attribs, avt, True)
        print('Learned decision tree is\n')
        bin_id3.display_id3_node(dtr, '')
        uexamples, ucolnames = bin_id3.parse_csv_file_into_examples('play_tennis_data.csv')
        gt = []
        with open('play_tennis_target.txt', 'r') as inf:
            for ln in inf:
                gt.append(ln.strip())
        assert len(uexamples) == len(gt)
        accurate_count = 0
        for uex, gtt in zip(uexamples, gt):
            pred = bin_id3.predict(dtr, uex)
            if pred == gtt:
                accurate_count += 1
        accuracy = accurate_count/len(uexamples)
        assert accuracy == 1.0
        print('classification accuracy = {}'.format(accurate_count/len(uexamples)))

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
