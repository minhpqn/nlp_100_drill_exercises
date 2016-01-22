# -*- coding: utf-8 -*-
#!/usr/bin/python

# 33. Danh từ dạng サ (サ変名詞)
# Trích xuất toàn bộ các danh từ dạng サ (サ変名詞). Tham khảo trang Wikipedia tiếng Nhật về [サ行変格活用](https://ja.wikipedia.org/wiki/%E3%82%B5%E8%A1%8C%E5%A4%89%E6%A0%BC%E6%B4%BB%E7%94%A8).

import re
from read_data_ex30 import read_data

if __name__ == '__main__':
    sentences = read_data()
    for sen in sentences:
        for morph in sen:
            if morph['pos'] == '名詞' and morph['pos1'] == 'サ変接続':
                print morph['surface']
