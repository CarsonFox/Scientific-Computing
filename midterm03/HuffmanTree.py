################################################
## module: HuffmanTree.py
# description: A Huffman Tree Class
# Carson Fox
# A02251670
##
# bugs to vladimir kulyukin in canvas
################################################

from heapq import heapify, heappop, heappush

from HuffmanTreeNode import HuffmanTreeNode


class HuffmanTree(object):
    def __init__(self, root=None):
        self.__root = root

    def getRoot(self) -> HuffmanTreeNode:
        return self.__root

    def encodeSymbol(self, s):
        if not s in self.__root.getSymbols():
            raise Exception("Unknown symbol")
        else:
            return self.__root.encodeSymbol(s)

    def encodeText(self, txt):
        return "".join(self.getRoot().encodeSymbol(sym) for sym in txt)

    def decode(self, bin_string):
        def symbols(rest):
            while len(rest) > 0:
                sym, rest = self.__root.decode(rest)
                yield sym

        return "".join(symbols(bin_string))

    @staticmethod
    def mergeTwoNodes(htn1, htn2):
        symbols = set(htn1.getSymbols())
        for i in htn2.getSymbols():
            symbols.add(i)
        n = HuffmanTreeNode(
            symbols=symbols, weight=htn1.getWeight() + htn2.getWeight())
        n.setLeftChild(htn1)
        n.setRightChild(htn2)
        return n

    @staticmethod
    def displayHuffmanTreeNode(ht_node, tabs):
        if ht_node is None:
            return
        print(tabs + "{}:{}".format(ht_node.getSymbols(), ht_node.getWeight()))
        HuffmanTree.displayHuffmanTreeNode(ht_node.getLeftChild(), tabs + "\t")
        HuffmanTree.displayHuffmanTreeNode(
            ht_node.getRightChild(), tabs + "\t")

    @staticmethod
    def displayHuffmanTree(huff_tree):
        HuffmanTree.displayHuffmanTreeNode(huff_tree.getRoot(), "")

    @staticmethod
    def displayListOfNodes(list_of_nodes):
        for n in list_of_nodes:
            print(str(n))

    @staticmethod
    def fromListOfHuffmanTreeNodes(list_of_nodes, dbg=False):
        heapify(list_of_nodes)

        while len(list_of_nodes) > 1:
            a, b = heappop(list_of_nodes), heappop(list_of_nodes)
            heappush(list_of_nodes, HuffmanTree.mergeTwoNodes(a, b))

        return HuffmanTree(list_of_nodes[0])

    @staticmethod
    def freqMapToListOfHuffmanTreeNodes(freq_map):
        return [
            HuffmanTreeNode(symbols=set([item[0]]), weight=item[1])
            for item in freq_map.items()
        ]
