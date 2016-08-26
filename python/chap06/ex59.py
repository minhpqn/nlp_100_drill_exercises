# -*- coding: utf-8 -*-
""" 59. Phrase structure analysis
    Từ kết quả phân tích cây cú pháp phrase structure (theo định dạng
    [S-expression], in ra tất cả các noun phrases trong văn bản.
    Chú ý, cần in ra cả các noun phrases nằm trong các noun phrases khác
    (nested NP).
"""

from xml.dom import minidom

"""
(ROOT (S (PP (NP (JJ Natural) (NN language) (NN processing)) (IN From) (NP (NNP Wikipedia))) (, ,) (NP (NP (DT the) (JJ free) (NN encyclopedia) (JJ Natural) (NN language) (NN processing)) (PRN (-LRB- -LRB-) (NP (NN NLP)) (-RRB- -RRB-))) (VP (VBZ is) (NP (NP (NP (DT a) (NN field)) (PP (IN of) (NP (NN computer) (NN science)))) (, ,) (NP (JJ artificial) (NN intelligence)) (, ,) (CC and) (NP (NP (NNS linguistics)) (VP (VBN concerned) (PP (IN with) (NP (NP (DT the) (NNS interactions)) (PP (IN between) (NP (NP (NNS computers)) (CC and) (NP (JJ human) (-LRB- -LRB-) (JJ natural) (-RRB- -RRB-) (NNS languages)))))))))) (. .)))
"""

class Node:
    def __init__(self, lb, text=None):
        self.label    = lb
        self.children = []
        self.text     = text

    def is_leaf():
        return len(self.children) == 0

    def children(self):
        return self.children
        
    def to_s(self):
        """ return string representation of the current node
        """
        return ' '

def parse_s_exp(s_exp):
    """ Parse the S-expression and return the root node
    """

    stack = []
    i = 0
    par
    while ( i < len(s_exp) ):
        if s_exp[i] == '(':
            i += 1
            stack.append(s_exp[i])
            lb = ''
            while i < len(s_exp) and s_exp[i] != ' ' and s_exp[i] != ')':
                lb += s_exp[i]
                i += 1
            print 'label = %s' % lb
            stack.append(lb)
        elif s_exp[i] == ')':
            i += 1
            stack.append(s_exp[i])
        elif s_exp[i] == ' ':
            i += 1
        else:
            txt = ''
            while i < len(s_exp) and s_exp[i] != ' ' and s_exp[i] != ')':
                txt += s_exp[i]
                i += 1
            if len(stack) > 0 and stack[-1] != ')' and stack[-1] != '(':
                lb = stack.pop()
                node = Node(lb, txt)
                # print 'leaf node: label = %s text = %s' % (lb, txt)
    
if __name__ == '__main__':
   xmldoc   = minidom.parse('../../data/nlp.txt.xml')
   xmlnodes = xmldoc.getElementsByTagName('parse')

   for xmlnode in xmlnodes:
       s_exp = xmlnode.firstChild.data
       sen_node = parse_s_exp(s_exp)

       
       




