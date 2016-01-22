#!/usr/bin/python
# -*- coding: utf-8 -*-

# 34. 「AのB」
# Trích xuất tất cả các danh từ ghép (compound nouns) kết nối bằng の.

from read_data_ex30 import read_data

if __name__ == '__main__':
    sentences = read_data()
    for sen in sentences:
        for i in xrange(len(sen)):
            morph = sen[i]
            if morph['surface'] == 'の' and morph['pos'] == '助詞':
                if i > 0 and i < len(sen)-1:
                    prev_mp = sen[i-1]
                    next_mp = sen[i+1]
                    if prev_mp['pos'] == '名詞' and prev_mp['pos1'] != '非自立' and next_mp['pos'] == '名詞' and next_mp['pos1'] != '非自立':
                        word = ''.join((prev_mp['surface'], 'の', next_mp['surface']))
                        print word
