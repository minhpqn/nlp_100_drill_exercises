# -*- coding: utf-8 -*-
"""82. Trích xuất context

   Sử dụng corpus được tạo ra trong bài tập 81, trích xuất context của
   tất cả các từ xuất hiện trong corpus. Context của mỗi từ *t* trong dữ liệu
   sẽ cặp với từ *t* và xuất ra theo định dạng: các thông tin cách nhau bởi
   ký tự tab. Context *c* của mỗi từ *t* được định nghĩa như sau:

   - Trích xuất các từ ở trước và sau của *t* với kích thước cửa sổ là *d*
     (chú ý context words của *t* sẽ không bao gồm bản thân của từ *t*)
   - Với mỗi từ *t*, kích thước của context (window size) *d* sẽ được chọn
     ngẫu nhiên trong tập {1, 2, 3, 4, 5}.

"""

import random
import sys
import os

if __name__ == '__main__':
    random.seed(9999)

    os.system('cls' if os.name == 'nt' else 'clear')

    datafile = '../../data/enwiki-20150112-400-r10-105752.preprocessed.txt'
    with open(datafile, 'rU') as f:
        for line in f:
            line = line.strip()
            if line == '': continue
            tokens = line.split()
            for i, w in enumerate(tokens):
                d = random.randint(1, 5)
                cntx_words = [ tokens[i+j] for j in range(-d, d+1) if
                               (j != 0 and i+j >= 0 and i+j < len(tokens)) ]
                print '\t'.join([tokens[i]] + cntx_words)
                    
                

    


