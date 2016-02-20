#!/usr/bin/python
# -*- coding: utf-8 -*-

# 40. Đọc vào kết quả dependency parsing (theo morphemes)
# Cài đặt lớp Morph cho các morphemes. Lớp này có các biến thành phần (member variables) là surface (cho surface forms của morphems), base (cho base form), pos (cho POS tag), pos1 (cho detailed POS tag 1 品詞細分類1). Sau đó đọc vào kết quả phân tích dependency parsing trong file neko.txt.cabocha. Mỗi câu sẽ bao gồm một danh sách các Morph objects. Hiển thị danh sách các morphemes cho câu thứ 3 trong văn bản.

import sys
import re
import codecs 
from collections import deque

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1

    def __str__(self):
        return ','.join( [self.surface, self.base, self.pos, self.pos1] )

    # return true if the token is a punctuation mark
    def is_punc(self):
        return self.pos1 == '句点' or self.pos1 == '読点'

    def is_noun(self):
        return self.pos == '名詞'

    def is_verb(self):
        return self.pos == '動詞'

# read dependency parsing result from an input file
# return a list of sentences, each sentence is a list of Morph objects
def read_morphs(filename):   
    f = codecs.open(filename, 'rU')

    sentences = []
    sen = []
    count = 0
    for line in f:
        line = line.rstrip()
        if line == '': continue
        if re.search(r'^\*', line): continue
        if re.search(r'^EOS$', line):
            count += 1
            sentences.append(sen)
            sen = []
            continue
        # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
        fields = line.split("\t")
        surf = fields[0]
        features = fields[1].split(',')
        base = features[-3]
        pos  = features[0]
        pos1 = features[1]
        morph = Morph(surf, base, pos, pos1)
        sen.append(morph)

    f.close()

    print 'Number of sentences: %d' % count

    return sentences

def read_data():
    return read_morphs('../../data/neko.txt.cabocha')
    
if __name__ == '__main__':
    sentences = read_data()
    third_sent = sentences[2]
    for morph in third_sent:
         print morph

    


