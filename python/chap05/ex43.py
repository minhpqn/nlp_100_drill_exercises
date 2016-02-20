#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Trích xuất các dependency relations giữa các chunk chứa danh từ và 
các chunk chứa động từ.
Trích xuất các dependency relations giữa các chunk chứa danh từ và 
các chunk chứa động từ. 
In ra theo định dạng tab. Tương tự như bài 42, không hiển thị các 
dấu (punctuation marks) trong các chunk.
"""

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 
import sys
from chunk_ex41 import read_chunks

if __name__ == '__main__':
	sentences = read_chunks()
	for sen in sentences:
		for src in sen:
			if src.dest() != -1:
				dst = sen[src.dest()]
				if src.has_noun() and dst.has_verb():
					sys.stdout.write('\t'.join([ src.surf2(), 
						                         dst.surf2() ]))
					sys.stdout.write('\n')
