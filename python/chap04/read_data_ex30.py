# -*- coding: utf-8 -*-
#!/usr/bin/python

import re
import codecs

# 30. Đọc vào kết quả morphological analysis
# Viết chương trình đọc vào kết quả morphological analysis (file neko.txt.mecab).
# Yêu cầu: Với mỗi morpheme, lưu các thông tin: 表層形 (surface form), 基本形 (base form), 品詞 (pos), 品詞細分類1 (pos1) bằng cấu trúc dữ liệu hash map với các key tương ứng là: surface, base, pos, pos1. Lưu trữ mỗi câu bằng danh sách của các morpheme. Trong các bài tập còn lại trong chương 4, hãy sử dụng cách tổ chức dữ liệu trong bài 30 này.

# read morphological analysis in a file into list of sentences
# each sentence contains a list of morphemes
def read_file(filename):
    f = codecs.open(filename, 'rU')
    sentences = []
    morphemes = []
    for line in f:
        line = line.strip()
        if line == '':
            next
        elif line == 'EOS':
            if morphemes:
                sentences.append(morphemes)
            morphemes = []    
        else:
            # print 'Read morpheme -- %s' % line
            morph = {}
            fields = line.split()
            surf     = fields[0]
            features = fields[1].split(',')
            pos  = features[0]
            pos1 = features[1]
            base = features[6]
            
            morph['surface'] = surf
            morph['base'] = base
            morph['pos']  = pos
            morph['pos1'] = pos1
            
            morphemes.append(morph)
    f.close()

    return sentences

def read_data():
    input_file = '../../data/neko.txt.mecab'
    return read_file(input_file)

# print sentence information, which is the list of morphemes    
def print_sent_info(sen):
    print "+ Number of morphemes: %s" % len(sen)
    for morph in sen:
        print '  %s  %s,%s,%s' % (morph['surface'], morph['pos'], morph['pos1'], morph['base'])
    
if __name__ == '__main__':
    sentences = read_data()
    print 'Number of sentences: %s' % len(sentences)

    for i in xrange(5):
        sen = sentences[i]
        print_sent_info(sen)


