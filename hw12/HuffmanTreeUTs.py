#####################################################################
# module: HuffmanTreeUTs.py
# description: unit tests for HuffmanTree and BinHuffmanTree classes.
# author: vladimir kulyukin
# my debugging traces are given as comments right before some tests.
# bugs to vladimir kulyukin in canvas
#####################################################################

import unittest
from HuffmanTree import HuffmanTree
from HuffmanTreeNode import HuffmanTreeNode
from BinHuffmanTree import BinHuffmanTree
from CharFreqMap import CharFreqMap

## Change the value of work_dir to the directory with
## the files moby_dick_ch01.txt, moby_dick_ch01.txt,
## test_txt0.txt, and test_txt1.txt.
work_dir = 'data/'

class HuffmanTreeUTs(unittest.TestCase):

    char_freqs01 = [('A', 4), ('B', 3), ('C', 1), ('D', 1)]
    char_freqs02 = [('A', 8), ('B', 3), ('C', 1), ('D', 1),
                    ('E', 1), ('F', 1), ('G', 1), ('H', 1)]

    def test_ht_ut00(self, tn=0):
        print('\n============ Huffman Tree UT {} ======================='.format(tn))
        htn01 = HuffmanTreeNode(symbols=set(['A', 'B', 'C']), weight=10)
        htn02 = HuffmanTreeNode(symbols=set(['B', 'C', 'A']), weight=10)
        assert htn01 == htn02
        assert htn02 == htn01
        htn03 = HuffmanTreeNode(symbols=set([1, 2, 3]), weight=5)
        htn04 = HuffmanTreeNode(symbols=set([2, 3, 1, 5, 4]), weight=5)
        assert htn03 != htn02
        assert htn02 != htn03
        htn05 = HuffmanTreeNode(symbols=set([1, 2, 3]), weight=1)
        htn06 = HuffmanTreeNode(symbols=set([2, 3, 1]), weight=5)
        ### Check that all nodes we've created are leaves.
        for htn in [htn01, htn02, htn03, htn04, htn05, htn06]:
            htn.isLeaf()
        ### make htn02 and htn03 the left and right child nodes of htn01
        htn01.setLeftChild(htn02)
        htn01.setRightChild(htn03)
        ### now htn01 is no longer a leaf, but htn02 and htn03 still are.
        assert not htn01.isLeaf()
        assert htn02.isLeaf()
        assert htn03.isLeaf()
        print('\n============ Huffman Tree  UT {} passed =============='.format(tn))

    '''
============ Huffman Tree UT 1 =======================
Node list is as follows:
0) HTN({'A'}, 4)
1) HTN({'B'}, 3)
2) HTN({'C'}, 1)
3) HTN({'D'}, 1)
Two lowest weight nodes are:
node 1 = HTN({'C'}, 1)
node 2 = HTN({'D'}, 1)
Removing two lowest weight nodes from node list...
Merging two removed nodes into new node HTN({'D', 'C'}, 2)...
Adding new merged node to node list...
Node list is as follows:
0) HTN({'B'}, 3)
1) HTN({'A'}, 4)
2) HTN({'D', 'C'}, 2)
Two lowest weight nodes are:
node 1 = HTN({'D', 'C'}, 2)
node 2 = HTN({'B'}, 3)
Removing two lowest weight nodes from node list...
Merging two removed nodes into new node HTN({'B', 'D', 'C'}, 5)...
Adding new merged node to node list...
Node list is as follows:
0) HTN({'A'}, 4)
1) HTN({'B', 'D', 'C'}, 5)
Two lowest weight nodes are:
node 1 = HTN({'A'}, 4)
node 2 = HTN({'B', 'D', 'C'}, 5)
Removing two lowest weight nodes from node list...
Merging two removed nodes into new node HTN({'B', 'A', 'D', 'C'}, 9)...
Adding new merged node to node list...
Node list is as follows:
0) HTN({'B', 'A', 'D', 'C'}, 9)
{'B', 'A', 'D', 'C'}:9
	{'A'}:4
	{'B', 'D', 'C'}:5
		{'D', 'C'}:2
			{'C'}:1
			{'D'}:1
		{'B'}:3
HTN({'B', 'A', 'D', 'C'}, 9)
HTN({'A'}, 4)
HTN({'B', 'D', 'C'}, 5)
HTN({'D', 'C'}, 2)
HTN({'C'}, 1)
HTN({'D'}, 1)
HTN({'B'}, 3)
============ Huffman Tree  UT 1 passed ==============
    '''
    
    def test_ht_ut01(self, tn=1):
        print('\n============ Huffman Tree UT {} ======================='.format(tn))        
        hnodes = [HuffmanTreeNode(symbols=set([kv[0]]), weight=kv[1])
                  for kv in HuffmanTreeUTs.char_freqs01]
        ht = HuffmanTree.fromListOfHuffmanTreeNodes(hnodes, dbg=True)
        assert ht is not None
        HuffmanTree.displayHuffmanTree(ht)                
        print(str(ht.getRoot()))
        print(str(ht.getRoot().getLeftChild()))
        print(str(ht.getRoot().getRightChild()))
        print(str(ht.getRoot().getRightChild().getLeftChild()))
        print(str(ht.getRoot().getRightChild().getLeftChild().getLeftChild()))
        print(str(ht.getRoot().getRightChild().getLeftChild().getRightChild()))
        print(str(ht.getRoot().getRightChild().getRightChild()))
        print('\n============ Huffman Tree  UT {} passed =============='.format(tn))

    '''    
============ Huffman Tree UT 2 =======================
Node list is as follows:
0) HTN({'A'}, 8)
1) HTN({'B'}, 3)
2) HTN({'C'}, 1)
3) HTN({'D'}, 1)
4) HTN({'E'}, 1)
5) HTN({'F'}, 1)
6) HTN({'G'}, 1)
7) HTN({'H'}, 1)
Two lowest weight nodes are:
node 1 = HTN({'C'}, 1)
node 2 = HTN({'D'}, 1)
Removing two lowest weight nodes from node list...
Merging two removed nodes into new node HTN({'D', 'C'}, 2)...
Adding new merged node to node list...
Node list is as follows:
0) HTN({'E'}, 1)
1) HTN({'F'}, 1)
2) HTN({'G'}, 1)
3) HTN({'H'}, 1)
4) HTN({'B'}, 3)
5) HTN({'A'}, 8)
6) HTN({'D', 'C'}, 2)
Two lowest weight nodes are:
node 1 = HTN({'E'}, 1)
node 2 = HTN({'F'}, 1)
Removing two lowest weight nodes from node list...
Merging two removed nodes into new node HTN({'E', 'F'}, 2)...
Adding new merged node to node list...
Node list is as follows:
0) HTN({'G'}, 1)
1) HTN({'H'}, 1)
2) HTN({'D', 'C'}, 2)
3) HTN({'B'}, 3)
4) HTN({'A'}, 8)
5) HTN({'E', 'F'}, 2)
Two lowest weight nodes are:
node 1 = HTN({'G'}, 1)
node 2 = HTN({'H'}, 1)
Removing two lowest weight nodes from node list...
Merging two removed nodes into new node HTN({'H', 'G'}, 2)...
Adding new merged node to node list...
Node list is as follows:
0) HTN({'D', 'C'}, 2)
1) HTN({'E', 'F'}, 2)
2) HTN({'B'}, 3)
3) HTN({'A'}, 8)
4) HTN({'H', 'G'}, 2)
Two lowest weight nodes are:
node 1 = HTN({'D', 'C'}, 2)
node 2 = HTN({'E', 'F'}, 2)
Removing two lowest weight nodes from node list...
Merging two removed nodes into new node HTN({'E', 'D', 'C', 'F'}, 4)...
Adding new merged node to node list...
Node list is as follows:
0) HTN({'H', 'G'}, 2)
1) HTN({'B'}, 3)
2) HTN({'A'}, 8)
3) HTN({'E', 'D', 'C', 'F'}, 4)
Two lowest weight nodes are:
node 1 = HTN({'H', 'G'}, 2)
node 2 = HTN({'B'}, 3)
Removing two lowest weight nodes from node list...
Merging two removed nodes into new node HTN({'B', 'H', 'G'}, 5)...
Adding new merged node to node list...
Node list is as follows:
0) HTN({'E', 'D', 'C', 'F'}, 4)
1) HTN({'A'}, 8)
2) HTN({'B', 'H', 'G'}, 5)
Two lowest weight nodes are:
node 1 = HTN({'E', 'D', 'C', 'F'}, 4)
node 2 = HTN({'B', 'H', 'G'}, 5)
Removing two lowest weight nodes from node list...
Merging two removed nodes into new node HTN({'H', 'E', 'D', 'C', 'F', 'B', 'G'}, 9)...
Adding new merged node to node list...
Node list is as follows:
0) HTN({'A'}, 8)
1) HTN({'H', 'E', 'D', 'C', 'F', 'B', 'G'}, 9)
Two lowest weight nodes are:
node 1 = HTN({'A'}, 8)
node 2 = HTN({'H', 'E', 'D', 'C', 'F', 'B', 'G'}, 9)
Removing two lowest weight nodes from node list...
Merging two removed nodes into new node HTN({'H', 'A', 'D', 'C', 'F', 'B', 'G', 'E'}, 17)...
Adding new merged node to node list...
Node list is as follows:
0) HTN({'H', 'A', 'D', 'C', 'F', 'B', 'G', 'E'}, 17)
Huffman Tree is as follows:
{'H', 'A', 'D', 'C', 'F', 'B', 'G', 'E'}:17
	{'A'}:8
	{'H', 'E', 'D', 'C', 'F', 'B', 'G'}:9
		{'E', 'D', 'C', 'F'}:4
			{'D', 'C'}:2
				{'C'}:1
				{'D'}:1
			{'E', 'F'}:2
				{'E'}:1
				{'F'}:1
		{'B', 'H', 'G'}:5
			{'H', 'G'}:2
				{'G'}:1
				{'H'}:1
			{'B'}:3

============ Huffman Tree  UT 2 passed ==============
    '''

    def test_ht_ut02(self, tn=2):
        print('\n============ Huffman Tree UT {} ======================='.format(tn))        
        hnodes = [HuffmanTreeNode(symbols=set([kv[0]]), weight=kv[1])
                  for kv in HuffmanTreeUTs.char_freqs02]
        ht = HuffmanTree.fromListOfHuffmanTreeNodes(hnodes, dbg=True)
        assert ht is not None
        print('Huffman Tree is as follows:')        
        HuffmanTree.displayHuffmanTree(ht)
        print('\n============ Huffman Tree  UT {} passed =============='.format(tn))

    def test_ht_ut03(self, tn=3):
        print('\n============ Huffman Tree UT {} ======================='.format(tn))
        ### Let's build the Huffman Tree from Lecture 25 bottom up.
        A_8 = HuffmanTreeNode(symbols=set(['A']), weight=8)
        B_3 = HuffmanTreeNode(symbols=set(['B']), weight=3)
        C_1 = HuffmanTreeNode(symbols=set(['C']), weight=1)
        D_1 = HuffmanTreeNode(symbols=set(['D']), weight=1)
        E_1 = HuffmanTreeNode(symbols=set(['E']), weight=1)
        F_1 = HuffmanTreeNode(symbols=set(['F']), weight=1)
        G_1 = HuffmanTreeNode(symbols=set(['G']), weight=1)
        H_1 = HuffmanTreeNode(symbols=set(['H']), weight=1)
        ### Merging G1 and H1
        GH_2 = HuffmanTree.mergeTwoNodes(G_1, H_1)
        ### Merging E_1 and F_1
        EF_2 = HuffmanTree.mergeTwoNodes(E_1, F_1)
        ### Merging C_1 and D_1
        CD_2 = HuffmanTree.mergeTwoNodes(C_1, D_1)
        ### Merging EF_2 and GH_2
        EFGH_4 = HuffmanTree.mergeTwoNodes(EF_2, GH_2)
        ### Merging B_3 and CD_2
        BCD_5 = HuffmanTree.mergeTwoNodes(B_3, CD_2)
        ### Merging BCD_5 and EFGH_4
        BCDEFGH_9 = HuffmanTree.mergeTwoNodes(BCD_5, EFGH_4)
        ### Merging A_8 and BCDEFGH_9
        ABCDEFGH_17 = HuffmanTree.mergeTwoNodes(A_8, BCDEFGH_9)
        ### Let's construct the tree
        scip_ht = HuffmanTree(root=ABCDEFGH_17)
        ### Let's build the alternative Huffman Tree
        hnodes = [HuffmanTreeNode(symbols=set([kv[0]]), weight=kv[1])
                  for kv in HuffmanTreeUTs.char_freqs02]
        alt_ht = HuffmanTree.fromListOfHuffmanTreeNodes(hnodes, dbg=True)
        assert alt_ht is not None
        print('Huffman Tree Codes:')        
        for ch, _ in HuffmanTreeUTs.char_freqs02:
            print('encode({}) = {}'.format(ch, scip_ht.encodeSymbol(ch)))
        print('Alternative Huffman Tree Codes:')        
        for ch, _ in HuffmanTreeUTs.char_freqs02:
            print('encode({}) = {}'.format(ch, alt_ht.encodeSymbol(ch)))
        for ch, _ in HuffmanTreeUTs.char_freqs02:
            assert len(scip_ht.encodeSymbol(ch)) == len(alt_ht.encodeSymbol(ch))
        print('\n============ Huffman Tree  UT {} passed =============='.format(tn))


    '''
============ Huffman Tree UT 4 =======================
txt0 = AABCCDEFG
enc0 = 00100101010101011110011011110
txt1 = AABBBBHHHFFGGGDDDDEEEECCCCCCCCDDDDDHHHHHAAAAAA
enc1 = 00100101010101011110011011110
dec0 = AABCCDEFG
dec1 = AABBBBHHHFFGGGDDDDEEEECCCCCCCCDDDDDHHHHHAAAAAA

============ Huffman Tree  UT 4 passed ==============
    '''

    def test_ht_ut04(self, tn=4):
        print('\n============ Huffman Tree UT {} ======================='.format(tn))
        ### Let's again build the Huffman Tree from Lecture 25 bottom up and
        ### use it to encode and decode messages and test encoding and decoding equations.
        A_8 = HuffmanTreeNode(symbols=set(['A']), weight=8)
        B_3 = HuffmanTreeNode(symbols=set(['B']), weight=3)
        C_1 = HuffmanTreeNode(symbols=set(['C']), weight=1)
        D_1 = HuffmanTreeNode(symbols=set(['D']), weight=1)
        E_1 = HuffmanTreeNode(symbols=set(['E']), weight=1)
        F_1 = HuffmanTreeNode(symbols=set(['F']), weight=1)
        G_1 = HuffmanTreeNode(symbols=set(['G']), weight=1)
        H_1 = HuffmanTreeNode(symbols=set(['H']), weight=1)
        ### Merging G1 and H1
        GH_2 = HuffmanTree.mergeTwoNodes(G_1, H_1)
        ### Merging E_1 and F_1
        EF_2 = HuffmanTree.mergeTwoNodes(E_1, F_1)
        ### Merging C_1 and D_1
        CD_2 = HuffmanTree.mergeTwoNodes(C_1, D_1)
        ### Merging EF_2 and GH_2
        EFGH_4 = HuffmanTree.mergeTwoNodes(EF_2, GH_2)
        ### Merging B_3 and CD_2
        BCD_5 = HuffmanTree.mergeTwoNodes(B_3, CD_2)
        ### Merging BCD_5 and EFGH_4
        BCDEFGH_9 = HuffmanTree.mergeTwoNodes(BCD_5, EFGH_4)
        ### Merging A_8 and BCDEFGH_9
        ABCDEFGH_17 = HuffmanTree.mergeTwoNodes(A_8, BCDEFGH_9)
        ### Let's construct the first huffman tree
        ht01 = HuffmanTree(root=ABCDEFGH_17)
        ### Let's encded and decode some two simple texts with ht01.
        txt0 = 'AABCCDEFG'
        txt1 = 'AABBBBHHHFFGGGDDDDEEEECCCCCCCCDDDDDHHHHHAAAAAA'
        enc0 = ht01.encodeText(txt0)
        print('txt0 = {}'.format(txt0))
        print('enc0 = {}'.format(enc0))
        enc1 = ht01.encodeText(txt1)
        print('txt1 = {}'.format(txt1))
        print('enc1 = {}'.format(enc1))
        dec0 = ht01.decode(enc0)
        print('dec0 = {}'.format(dec0))
        dec1 = ht01.decode(enc1)
        print('dec1 = {}'.format(dec1))        
        assert dec0 == txt0
        assert dec1 == txt1
        print('\n============ Huffman Tree  UT {} passed =============='.format(tn))

    def test_ht_ut05(self, tn=5):
        print('\n============ Huffman Tree UT {} ======================='.format(tn))
        htnodes = [HuffmanTreeNode(symbols=set([kv[0]]), weight=kv[1])
                   for kv in HuffmanTreeUTs.char_freqs02]
        ht = HuffmanTree.fromListOfHuffmanTreeNodes(htnodes)
        print('Encoding/Decoding with the following Huffman Tree:')
        HuffmanTree.displayHuffmanTree(ht)
        
        bht = BinHuffmanTree(root=ht.getRoot())
        ### Let's encded and decode some two simple texts.
        txt0 = 'AABCCDEFG'
        txt1 = 'AABBBBHHHFFGGGDDDDEEEECCCCCCCCDDDDDHHHHHAAAAAA'

        ### Let's compare character-based encoding with binary encoding
        enc0 = ht.encodeText(txt0)
        print('The bit length of \'{}\' is {} bits'.format(txt0, len(txt0)*8))
        print('It took {} bits to encode \'{}\' as \'{}\''.format(8*len(enc0), txt0, enc0))
        bin_enc0, num_bytes0, pad_bits0 = bht.encodeText(txt0)
        print('It took {} bits to encode \'{}\' as {}'.format(8*num_bytes0 + pad_bits0, txt0, bin_enc0))
        enc1 = ht.encodeText(txt1)
        print('The bit length of \'{}\' is {} bits'.format(txt1, len(txt1)*8))
        bin_enc1, num_bytes1, pad_bits1 = bht.encodeText(txt1)
        print('It took {} bits to encode \'{}\' as {}'.format(8*num_bytes1 + pad_bits1, txt1, bin_enc1))
        dec0 = bht.decode(bin_enc0, pad_bits0)
        dec1 = bht.decode(bin_enc1, pad_bits1)
        assert dec0 == txt0
        assert dec1 == txt1
        print('\n============ Huffman Tree  UT {} passed =============='.format(tn))        

    def test_ht_ut06(self, tn=6):
        print('\n============ Huffman Tree UT {} ======================='.format(tn))        
        htnodes = [HuffmanTreeNode(symbols=set([kv[0]]), weight=kv[1])
                   for kv in HuffmanTreeUTs.char_freqs02]
        ht = HuffmanTree.fromListOfHuffmanTreeNodes(htnodes)
        bht = BinHuffmanTree(root=ht.getRoot())
        txt0 = 'AABCCDEFG'
        txt1 = 'AABBBBHHHFFGGGDDDDEEEECCCCCCCCDDDDDHHHHHAAAAAA'
        with open(work_dir + 'test_txt0.txt', 'w', encoding='utf-8') as of:
            of.write(txt0)
            of.flush()
        bht.encodeTextToFile(txt0, work_dir + 'test_txt0')
        with open(work_dir + 'test_txt1.txt', 'w') as of:
            of.write(txt1)
            of.flush()
        bht.encodeTextToFile(txt1, work_dir + 'test_txt1')
        dec0 = bht.decodeTextFromFile(work_dir + 'test_txt0')
        dec1 = bht.decodeTextFromFile(work_dir + 'test_txt1')
        assert txt0 == dec0
        assert txt1 == dec1
        print('\n============ Huffman Tree  UT {} passed =============='.format(tn))

    def test_ht_ut07(self, tn=7):
        print('\n============ Huffman Tree UT {} ======================='.format(tn))
        cfm1 = CharFreqMap.computeCharFreqMap(work_dir + 'moby_dick_ch01.txt')
        nodes = HuffmanTree.freqMapToListOfHuffmanTreeNodes(cfm1)
        ht = HuffmanTree.fromListOfHuffmanTreeNodes(nodes)
        bht = BinHuffmanTree(root=ht.getRoot())
        bht.encodeTextFromFileToFile(work_dir + 'moby_dick_ch01.txt',
                                     work_dir + 'moby_dick_ch01')
        with open(work_dir + 'moby_dick_ch01.txt', 'r', encoding='utf-8') as inf:
            data = inf.read()
            dec0 = bht.decodeTextFromFile(work_dir + 'moby_dick_ch01')
            assert dec0 == data
        print('\n============ Huffman Tree  UT {} passed =============='.format(tn))

    def test_ht_ut08(self, tn=8):
        print('\n============ Huffman Tree UT {} ======================='.format(tn))        
        cfm2 = CharFreqMap.computeCharFreqMap(work_dir + 'moby_dick_ch02.txt')
        nodes = HuffmanTree.freqMapToListOfHuffmanTreeNodes(cfm2)
        ht = HuffmanTree.fromListOfHuffmanTreeNodes(nodes)
        bht = BinHuffmanTree(root=ht.getRoot())
        bht.encodeTextFromFileToFile(work_dir + 'moby_dick_ch02.txt',
                                     work_dir + 'moby_dick_ch02')
        with open(work_dir + 'moby_dick_ch02.txt', 'r', encoding='utf-8') as inf:
            data = inf.read()
            dec0 = bht.decodeTextFromFile(work_dir + 'moby_dick_ch02')
            assert dec0 == data
        print('\n============ Huffman Tree  UT {} passed =============='.format(tn))


    def test_ht_ut09(self, tn=9):
        print('\n============ Huffman Tree UT {} ======================='.format(tn))        
        cfm = CharFreqMap.computeCharFreqMap(work_dir + 'moby_dick_ch01.txt')
        nodes = HuffmanTree.freqMapToListOfHuffmanTreeNodes(cfm)
        ht = HuffmanTree.fromListOfHuffmanTreeNodes(nodes)
        bht = BinHuffmanTree(root=ht.getRoot())
        bht.persist(work_dir + 'moby_dick_ch01_bht.bin')
        print('\n============ Huffman Tree  UT {} passed =============='.format(tn))        

    def test_ht_ut10(self, tn=10):
        print('\n============ Huffman Tree UT {} ======================='.format(tn))                
        cfm = CharFreqMap.computeCharFreqMap(work_dir + 'moby_dick_ch02.txt')
        nodes = HuffmanTree.freqMapToListOfHuffmanTreeNodes(cfm)
        ht = HuffmanTree.fromListOfHuffmanTreeNodes(nodes)
        bht = BinHuffmanTree(root=ht.getRoot())
        bht.persist(work_dir + 'moby_dick_ch02_bht.bin')
        print('\n============ Huffman Tree  UT {} passed =============='.format(tn))                

    def test_ht_ut11(self, tn=11):
        print('\n============ Huffman Tree UT {} ======================='.format(tn))                
        bht01 = BinHuffmanTree.load(work_dir + 'moby_dick_ch01_bht.bin')
        bht02 = BinHuffmanTree.load(work_dir + 'moby_dick_ch02_bht.bin')
        with open(work_dir + 'moby_dick_ch01.txt', 'r', encoding='utf-8') as inf:
            data = inf.read()
            dec01 = bht01.decodeTextFromFile(work_dir + 'moby_dick_ch01')
            assert dec01 == data
            print('Assertion passed!')
        with open(work_dir + 'moby_dick_ch02.txt', 'r', encoding='utf-8') as inf:
            data = inf.read()
            dec02 = bht02.decodeTextFromFile(work_dir + 'moby_dick_ch02')
            assert dec02 == data
        print('\n============ Huffman Tree  UT {} passed =============='.format(tn))
    
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
