#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
80. Tiền xử lý dữ liệu
"""

import re
import sys
from bz2 import BZ2File
import codecs

def is_blank(tk):
	if re.search( r'^[\s\t　]*$', tk ):
		return True

	return False

def clean(tk):
	match = re.search(r'^[\.,!\?;:\(\)\[\]\'\"\s\t]*(.*?)[\.,!\?;:\(\)\[\]\'"\s\t]*$', tk)
	if match:
		return match.group(1)
	return tk

if __name__ == '__main__':
	datafile = '../../data/enwiki-20150112-400-r10-105752.txt.bz2'
	output = '../../data/enwiki-20150112-400-r10-105752.tokenized.txt'

	with codecs.open( output, 'w' ) as fo:
		with BZ2File( datafile, 'rU' ) as f:
			for line in f:
				line = line.rstrip()
				if is_blank(line): continue
				tokens = [ clean(tk) for tk in line.split() 
					                     if not is_blank( clean(tk) ) ]
				fo.write( '%s\n' % ' '.join(tokens) )
