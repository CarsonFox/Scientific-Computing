###################################################
# module: HuffmanTreeNode.py
# description: A Node of the Huffman Encoding Tree
# author: vladmir kulyukin
# bugs to vladimir kulyukin in canvas
###################################################


class HuffmanTreeNode(object):
    def __init__(self, symbols=set(), weight=0):
        self.__symbols = set(symbols)
        self.__weight = weight
        self.__leftChild = None
        self.__rightChild = None

    def getSymbols(self):
        return self.__symbols

    def setSymbols(self, s):
        self.__symbols = s

    def getWeight(self):
        return self.__weight

    def setWeight(self, w):
        self.__weight = w

    def getLeftChild(self):
        return self.__leftChild

    def setLeftChild(self, lc):
        self.__leftChild = lc

    def getRightChild(self):
        return self.__rightChild

    def setRightChild(self, lc):
        self.__rightChild = lc

    def __str__(self):
        return "HTN(" + str(self.__symbols) + ", " + str(self.__weight) + ")"

    def __eq__(self, htn):
        return (
            self.getWeight() == htn.getWeight()
            and len(self.getSymbols().difference(htn.getSymbols())) == 0
            and len(htn.getSymbols().difference(self.getSymbols())) == 0
        )

    def __lt__(self, htn):
        return self.__weight < htn.__weight

    def isLeaf(self):
        return self.__rightChild is None and self.__leftChild is None

    def encodeSymbol(self, s):
        if self.isLeaf():
            assert s in self.getSymbols()
            return ""

        if s in self.getLeftChild().getSymbols():
            return "0" + self.getLeftChild().encodeSymbol(s)
        else:
            return "1" + self.getRightChild().encodeSymbol(s)

    def decode(self, bin_string):
        if self.isLeaf():
            sym, *_ = self.getSymbols()
            return sym, bin_string
        else:
            bit, rest = bin_string[0], bin_string[1:]
            if bit == "0":
                return self.getLeftChild().decode(rest)
            else:
                return self.getRightChild().decode(rest)
