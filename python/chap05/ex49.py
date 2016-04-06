# -*- coding: utf-8 -*-
""" 49. Trích xuất ra chuỗi liên kết giữa các danh từ
"""

from collections import defaultdict
import sys
from chunk_ex41 import read_chunks
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

def ck_repr(ch, ck):
    case = ck.case() if ck.case() != None else ''
    return ch + case

def get_path(ch, listid, sen):
    chain = []
    ck = sen[listid[0]]
    chain.append( ck_repr(ch, ck) )
    for i in range(1, len(listid)):
        chain.append(sen[listid[i]].surf2())
    return ' -> '.join(chain)    

sentences = read_chunks()
for sen in sentences[7:9]:
    nn_ids = [i for i in range(len(sen)) if sen[i].has_noun()]
    paths_to_root = defaultdict(list)
    direct_path   = defaultdict(list)
    for i in nn_ids:
        cur_ck = sen[i]
        paths_to_root[i].append(i)
        while cur_ck != None:
            dst = cur_ck.dst
            if dst != -1:
                paths_to_root[i].append(dst)
                cur_ck = sen[dst]
                if dst in nn_ids:
                    direct_path[(i,dst)] = [ k for k in paths_to_root[i] ]
            else:
                cur_ck = None
        
    for i in nn_ids:
        for j in nn_ids:
            if j <= i: continue
            if direct_path.has_key((i,j)):
                # print direct path between i and j
                chain = []
                for k in direct_path[(i,j)]:
                    if k == i:
                        chain.append( ck_repr('X', sen[k]) )
                    elif k == j:
                        chain.append( ck_repr('Y', sen[k]) )
                    else:
                        chain.append( sen[k].surf2() )
                print ' -> '.join(chain)
            else:
                path_i = paths_to_root[i]
                path_j = paths_to_root[j]
                m = 0
                n = 0
                while m < len(path_i) and n < len(path_j):
                    if path_i[m] == path_j[n]:
                        break
                    if path_i[m] < path_j[n]:
                        m += 1
                    else:
                        n += 1

                if m != len(path_i) and n != len(path_j):
                    k = path_i[m]
                    # print '(i,j) = (%d, %d) %d : %s' % (i,j, k, sen[k].surf2())
                    path1 = get_path( 'X', path_i[0:m], sen )
                    path2 = get_path( 'Y', path_j[0:n], sen )
                    print '%s | %s | %s' % (path1, path2, sen[k].surf2())
                    
                    




                                      
                                      
                        
