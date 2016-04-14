# -*- coding: utf-8 -*-
""" 50. Tách câu (Sentence segmentation)
    Sử dụng patterns (. or ; or : or ? or !) -> ký tự space -> chữ cái
    tiếng Anh viết hoa (captial letter) để tách các câu trong văn bản.
    Đầu vào là văn bản nlp.txt, in ra mỗi câu trong văn bản trên 1 dòng.
"""

import re
import sys
import os
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

def sent_segment(a_string):
    sentences = []
    regx = re.compile(r'([\.;:\?!])\s+([A-Z])')
    
    m = regx.search(a_string)
    last_pos = 0
    pos = m.start() if m != None else None

    while ( pos != None ):
        s = a_string[last_pos:pos+1]
        sentences.append(s)
        last_pos = last_pos + m.end() - 1 if m != None else None
        m = regx.search(a_string[last_pos:])
        pos = last_pos + m.start() if m != None else None
        
    return sentences

def unit_test():
    a_string = 'Natural language processing (NLP) is a field of computer science, artificial intelligence, and linguistics concerned with the interactions between computers and human (natural) languages. As such, NLP is related to the area of humani-computer interaction; Many challenges in NLP involve natural language understanding, that is, enabling computers to derive meaning from human or natural language input, and others involve natural language generation. ABD? Minh! Yeu.'

    print a_string
    print 

    sentences = sent_segment(a_string)
    print '\n'.join(sentences)


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    with open('../../data/nlp.txt', 'rU') as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            sentences = sent_segment(line)
            for s in sentences:
                print s
            
            
            
