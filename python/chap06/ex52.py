# -*- coding: utf-8 -*-
""" 52. Stemming
    Đầu vào là đầu ra của bài tập 51, áp dụng thuật toán Porter stemming
    để lấy ra gốc của các từ (stem). In ra các từ và stem cách nhau bởi
    ký tự tab. Nếu bạn sử dụng Python, bạn có thể sử dụng module
    [stemming](<https://pypi.python.org/pypi/stemming>).
"""

# SYNOPSIS: python ex50.py | python ex51.py | python ex52.py

from nltk.stem.snowball import SnowballStemmer
import sys
import codecs

stemmer = SnowballStemmer(u'english')

for w in sys.stdin:
    w = w.strip()
    if w == '':
        print
    else:
        wstem = stemmer.stem(w.decode('utf-8', errors='ignore'))
        print '%s\t%s' % (w, wstem)









