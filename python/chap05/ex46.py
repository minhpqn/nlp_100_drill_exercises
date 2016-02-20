#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from chunk_ex41 import read_chunks
from verb_case_ex45 import left_most_verb
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 

def save( predicates, cid, case, src ):
	if not predicates.has_key(cid):
		predicates[cid] = []

	predicates[cid].append( [case, src] )

if __name__ == '__main__':
	cases = {'が': 1, 'を': 1, 'は': 1, 'で': 1, 'に': 1}
	sentences = read_chunks()

	for sen in sentences:
		preds = {}
		for src_id in xrange( 0, len(sen) ):
			src = sen[src_id]
			case = src.case()
			dst_id = src.dest()
			if dst_id != -1 and case != None and cases.has_key(case):
				dst = sen[dst_id]
				if dst.has_verb():
					save( preds, dst_id, case, src.surf2() )

		for i in sorted( preds.keys() ):
			ck = sen[i]
			verb = left_most_verb( ck )
			pairs_  = sorted( preds[i], key = lambda x: x[0] )
			cases_  = ' '.join( map( lambda x: x[0], pairs_ ) )
			chunks_ = ' '.join( map( lambda x: x[1], pairs_ ) )
			print '\t'.join( [ verb, cases_, chunks_ ] )