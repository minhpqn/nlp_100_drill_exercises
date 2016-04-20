# -*- coding: utf-8 -*-
""" 53. Tokenization
    Sử dụng tool Stanford CoreNLP để phân tích văn bản đầu vào và lấy ra
    output theo định dạng XML. Sau đó đọc vào đầu ra XML và trích xuất
    ra các token (word) theo định dạng mỗi word trên 1 dòng.
"""

# preprocess text file with stanford-corenlp
# % sh corenlp_analyze.sh ../../data/nlp.txt
# xml output is ../../data/nlp.txt.xml

import os
import sys
import re

if __name__ == '__main__':
    with open('../../data/nlp.txt.xml', 'rU') as f:
        for line in f:
            line = line.strip()
            match = re.match(r'<word>(.+)</word>', line)
            if match:
                print match.group(1)
        


