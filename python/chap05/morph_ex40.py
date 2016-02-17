#!/usr/bin/python
# -*- coding: utf-8 -*-

# 40. Đọc vào kết quả dependency parsing (theo morphemes)
# Cài đặt lớp Morph cho các morphemes. Lớp này có các biến thành phần (member variables) là surface (cho surface forms của morphems), base (cho base form), pos (cho POS tag), pos1 (cho detailed POS tag 1 品詞細分類1). Sau đó đọc vào kết quả phân tích dependency parsing trong file neko.txt.cabocha. Mỗi câu sẽ bao gồm một danh sách các Morph objects. Hiển thị danh sách các morphemes cho câu thứ 3 trong văn bản.

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1


# read dependency parsing result from an input file
# return a list of sentences, each sentence is a list of Morph objects
def read_dp_result(filename):

def read_data():
    sentences = read_dp_result('../../data/neko.txt.cabocha')
    
if __name__ == '__main__':
    sentences = read_data()
    third_sent = sentences[2]
    for morph in third_sent:
        print morph

    


