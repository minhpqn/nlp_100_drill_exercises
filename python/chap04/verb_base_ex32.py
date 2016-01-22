# -*- coding: utf-8 -*-
#!/usr/bin/python

# 32. Dạng nguyên thể của động từ (動詞の原形)
# Trích xuất tất cả dạng nguyên thể của động từ (base form).

from read_data_ex30 import read_data

if __name__ == '__main__':
    sentences = read_data()
    for sen in sentences:
        for morph in sen:
            if morph['pos'] == '動詞':
                print morph['base']
