#/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Hiển thị chunk nguồn (head) và chunk đích (modifier) trong các 
depedency relations

Hiển thị nội dung (dạng text) các chunk nguồn (head) và 
chunk đích (modifier) trên mỗi dòng và cách nhau bởi ký tự tab.
Chú ý không hiển thị các dấu (punctuation marks) trong các chunk.
"""

import sys
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 
from chunk_ex41 import read_chunks

if __name__ == '__main__':
	sentences = read_chunks()
	for sen in sentences:
		for src in sen:
			if src.dest() != -1:
				dst = sen[src.dest()]
				sys.stdout.write('\t'.join([ src.surf2(), dst.surf2() ]))
				sys.stdout.write('\n')
