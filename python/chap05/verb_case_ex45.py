#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
45. Trích xuất các verb case patterns
Sử dụng các trợ từ sau đây:
が を は で に
"""

import sys
from chunk_ex41 import read_chunks
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 

# return base form of the left-most verb of a chunk
def left_most_verb( ck ):
	for mph in ck.morphs:
		if mph.is_verb():
			return mph.base
	return None

def save(predicates, cid, case):
	if not predicates.has_key(cid):
		predicates[cid] = []
	predicates[cid].append(case)

if __name__ == '__main__':
	cases = {'が': 1, 'を': 1, 'は': 1, 'で': 1, 'に': 1}
	sentences = read_chunks()

	for sen in sentences:
		preds = {}
		for src in sen:
			case = src.case()
			dst_id = src.dest()
			if dst_id != -1 and case != None and cases.has_key(case):
				dst = sen[dst_id]
				if dst.has_verb():
					save(preds, dst_id, case)

		for i in sorted( preds.keys() ):
			ck = sen[i]
			verb = left_most_verb( ck )
			cases_ = ' '.join( sorted( preds[i]) )
			print '\t'.join( [ verb, cases_ ] )






