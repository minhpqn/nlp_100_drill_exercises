# -*- coding: utf-8 -*-
""" 48. Trích xuất ra dependency path từ các danh từ
"""

import sys
from chunk_ex41 import read_chunks
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

if __name__ == '__main__':
    sentences = read_chunks()
    for sen in sentences:
        for i,ck in enumerate(sen):
            if ck.has_noun():
                # print path from ck to the path
                chain = []
                cur_ck = ck
                while cur_ck != None:
                    chain.append(cur_ck.surf2())
                    cur_ck = sen[cur_ck.dst] if cur_ck.dst != -1 else None
                print ' -> '.join(chain)
                





