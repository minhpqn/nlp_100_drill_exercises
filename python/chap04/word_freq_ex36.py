#!/usr/bin/python
# -*- coding: utf-8 -*-

# 36. Tần suất xuất hiện của từ
# Lập trình tính tần suất xuất hiện của từ trong văn bản. Đưa ra các từ theo thứ tự giảm dần của tần suất xuất hiện.

from read_data_ex30 import read_data

def is_noun(morph):
    if morph['pos'] == '名詞' and morph['pos1'] != '非自立':
        return True
    return False

def is_verb(morph):
    if morph['pos'] == '動詞' and morph['pos1'] != '非自立':
        return True
    return False

def is_adj(morph):
    if morph['pos'] == '形容詞' and morph['pos1'] != '非自立':
        return True
    return False

def get_word_frequency():
    word_freq = {}
    sentences = read_data()
    for sen in sentences:
        for morph in sen:
            word = morph['base']
            if is_noun(morph) and word != '*' and word != 'ー' and word != '一':
                if word_freq.has_key(word):
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1                
    return word_freq            

if __name__ == '__main__':
    word_freq = get_word_frequency()
    sorted_words = sorted(word_freq.keys(), key = lambda x: word_freq[x], reverse = True)
    for word in sorted_words:
        print '%s %d' % (word, word_freq[word])
