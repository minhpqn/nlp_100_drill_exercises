# -*- coding: utf-8 -*-
"""83. Tính tần xuất xuất hiện của từ/context

   Sử dụng đầu ra của bài 82, tính phân bố xuất hiện và các hằng số sau:
   - *f*(*t*,*c*): là số lần đồng xuất hiện của từ *t* và context word *c*.
   - *f*(*t*,\*): số lần xuất hiện của từ *t*.
   - *f*(\*,*c*): số lần xuất hiện của context word *c*.
   - *N*: Tổng số lần xuất hiện của từ và các context word (hằng số).
"""

from collections import defaultdict
import os
import sys

def cal_freq(filename):
    f   = open(filename, 'rU')
    ft  = defaultdict(int)
    fc  = defaultdict(int)
    ftc = defaultdict(int)
    N   = 0
    count = 0
    for line in f:
        line = line.strip()
        if count % 1000000 == 0:
            sys.stderr.write('Processing line %d...\n' % (count+1))
        count += 1
        if line == '': continue

        tokens = line.split('\t')
        t = tokens[0]
        
        for c in tokens[1:]:
            fc[c] += 1
            ftc[(t,c)] += 1
        N += len(tokens) - 1    
        ft[t] += 1

    f.close()

    return (ftc, ft, fc, N)

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    ftc, ft, fc, N = cal_freq('words_context.tsv')

    print 'Number of pairs N= %d' % N

    for t, c in ftc.keys[:9]:
        print '(%s,%s):  %d' % (t, c, ftc[(t,c)])
    


