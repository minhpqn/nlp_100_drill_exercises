# -*- coding: utf-8 -*-
"""54. POS Tag
   Đọc vào kết quả phân tích dạng XML của Stanford Core NLP.
   Trích xuất ra word, lemma, POS tag và in ra các thuộc tính của mỗi word
   trên một dòng; các thuộc tính cách nhau bởi dấu tab.
"""

from xml.dom import minidom
import os
import sys

# Reference: http://www.diveintopython.net/xml_processing/searching.html
if __name__ == '__main__':
    xmldoc = minidom.parse('../../data/nlp.txt.xml')
    token_list = xmldoc.getElementsByTagName('token')
    for tknode in token_list:
        info = []
        for tag in ['word', 'lemma', 'POS']:
            node = tknode.getElementsByTagName(tag)
            info.append(node[0].firstChild.data)
        print '\t'.join(info)
        

        
    
