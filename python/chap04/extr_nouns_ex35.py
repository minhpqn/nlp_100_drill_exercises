#!/usr/bin/python
# -*- coding: utf-8 -*-

# 35. Trích xuất các kết nối danh từ (noun connections hay 名詞の連接)
# Trích xuất tất cả các noun connections (các danh từ đứng cạnh nhau liên tiếp). Khi trích xuất, chú ý trích xuất chuỗi danh từ matching dài nhất có thể. Ví dụ ABC trong đó A, B, C là danh từ thì phải trích xuất ABC thay vì AB.

from read_data_ex30 import read_data
from read_data_ex30 import print_sent_info

def is_noun(morph):
    if morph['pos'] == '名詞' and morph['pos1'] != '非自立':
        return True
    return False    

def print_all_compound_nouns(sen):
    i = 0
    while True:
        while i < len(sen) and not is_noun(sen[i]):
            i += 1
        if i == len(sen):
            break
        j = i
        while j < len(sen) and is_noun(sen[j]):
            j += 1
        # concat words from sen[i] to sen[j-1]
        noun = ''.join(  map( lambda mrph: mrph['surface'], sen[i:j] ) )
        print noun
        i = j
            
def extract_nouns():
    sentences = read_data()
    for sen in sentences:
        print_all_compound_nouns(sen)
        
if __name__ == '__main__':
    extract_nouns()
