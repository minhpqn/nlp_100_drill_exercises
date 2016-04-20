# -*- coding: utf-8 -*-
"""55. Trích xuất named entities
   Trích xuất tất cả các named entities trong văn bản đầu vào.
"""

from xml.dom import minidom
import os
import sys
import re

if __name__ == '__main__':
    xmldoc = minidom.parse('../../data/nlp.txt.xml')
    token_list = xmldoc.getElementsByTagName('token')
    for tknode in token_list:
        NERs = tknode.getElementsByTagName('NER')
        if NERs[0].firstChild.data != 'O':
            node = tknode.getElementsByTagName('word')[0]
            print '%s\t%s' % (node.firstChild.data, NERs[0].firstChild.data)

