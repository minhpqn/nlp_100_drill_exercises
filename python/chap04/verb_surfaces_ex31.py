# -*- coding: utf-8 -*-
#!/usr/bin/python

# 31. Động từ
# Trích xuất tất cả các surface forms của động từ (pos=動詞).

from read_data_ex30 import read_data

if __name__ == '__main__':
    sentences = read_data()
    for sen in sentences:
        for morph in sen:
            if morph['pos'] == '動詞':
                print morph['surface']
    

