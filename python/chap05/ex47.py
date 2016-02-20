#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
47. Mining các cấu trúc câu có động từ chức năng
"""

import sys
from chunk_ex41 import read_chunks, sen_surf
from verb_case_ex45 import left_most_verb
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 

def save(predicates, pred, case, src):
	if not predicates.has_key(pred):
		predicates[pred] = []

	predicates[pred].append( [case, src] )

def get_sahen_noun(ck):
	for mph in reversed(ck.morphs):
		if mph.pos == '名詞' and mph.pos1 == 'サ変接続':
			return mph.base
	return None

if __name__ == '__main__':
	cases = {'が': 1, 'を': 1, 'は': 1, 'で': 1, 'に': 1}
	sentences = read_chunks()
	for sen in sentences:
		preds = {}
		for src_id in xrange( 0, len(sen) ):
			src = sen[src_id]
			case = src.case()
			sahen_noun = get_sahen_noun(src)
			dst_id = src.dest()
			if dst_id != -1 and case != None and case == 'を' and sahen_noun != None:
				dst = sen[dst_id]
				if dst.has_verb():
					pred = ''.join( [ sahen_noun, 'を', 
						             left_most_verb(dst) ] )
					for i in dst.srcs:
						ck = sen[i]
						ck_case = ck.case()
						if i != src_id and ck_case != None and cases.has_key(ck_case):
							save(preds, pred, ck_case, ck.surf2() )

		for pred in sorted( preds.keys() ):
			pairs_  = sorted( preds[pred], key = lambda x: x[0] )
			cases_  = ' '.join( map( lambda x: x[0], pairs_ ) )
			chunks_ = ' '.join( map( lambda x: x[1], pairs_ ) )
			print '\t'.join( [ pred, cases_, chunks_ ] )

