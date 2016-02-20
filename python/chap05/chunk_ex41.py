#!/usr/bin/python
# -*- coding: utf-8 -*-

# Tiếp theo bài 40, cài đặt lớp Chunk để lưu trữ các chunk (hay bunsetsu (文節)).
# Lớp này có các biến thành phần là: - morphs (để lưu trữ danh sách các Morph objects) - dst để lưu trữ index của chunk mà chunk hiện tại trỏ đến (chunk đích - destination) - srcs để lưu trữ danh sách các indexes của các chunk trỏ đến chunk hiện tại.
# Sau đó, đọc vào kết quả dependency parsing. Mỗi câu sẽ bao gồm danh sách 
# của các Chunk objects. Hiển thị xâu ký tự và giá trị của biến dst của 
# các chunk trong câu thứ 8 của file đầu vào.
# Các bài tập còn lại trong chương 5 sẽ sử dụng các chương trình được 
# tạo ra trong bài tập 40 và 41.

import sys
import codecs
import re
from morph_ex40 import Morph

class Chunk:
	def __init__(self, id, morphs, dst, srcs = []):
		self.id     = id
		self.morphs = morphs
		self.dst    = dst
		self.srcs   = srcs

	def dest(self):
		return self.dst

	# get 助詞 from the bunsetsu
	def case(self):
		for i in reversed( range( 0, len(self.morphs) ) ):
			cur_mph = self.morphs[i]
			if i > 0 and cur_mph.pos == '助詞' and ( cur_mph.pos1 == '格助詞' or cur_mph.pos1 == '係助詞' ):
				prev_mph = self.morphs[i-1]
				if prev_mph.is_noun():
					return cur_mph.surface
		return None					


	def add_morph(self, morph):
		self.morphs.append(morph)

	def set_srcs(self, srcs):
		self.srcs = srcs
		
	def add_src(self, i):
		self.srcs.append(i)

	def is_empty(self):
		return len(self.morphs) == 0

	def surf(self):
		return ''.join( map( lambda x: x.surface, self.morphs ) )

	# return text of the chunk without punctuation marks
	def surf2(self):
		return ''.join( map( lambda x: x.surface, 
			filter( lambda x: not x.is_punc(), self.morphs ) ) )

	def has_noun(self):
		for mrph in self.morphs:
			if mrph.is_noun():
				return True
		return False

	def has_verb(self):
		for mrph in self.morphs:
			if mrph.is_verb():
				return True
		return False

def sen_surf(sen):
	return ''.join( map( lambda x: x.surf(), sen ) )

def set_srcs(sen):
	for i in xrange( 0, len(sen) ):
		ck = sen[i]
		if ck.dst != -1:
			if ck.dst >= len(sen):
				print 'error: %s' % ck.dst
				print sen_surf(sen)
				sys.exit()
			sen[ck.dst].add_src(i)
 
def __read_chunks(filename):
	sys.stderr.write('%s\n' % filename)
	sentences = []
	count = 0
	sen = []
	morphs = []
	dst = None
	cid = None
	id2src = {}

	f = open(filename, 'rU')
	for line in f:
		line = line.rstrip()
		if line == '':
			continue
		match = re.search(r'^\*\s(\d+)\s(-?\d+)', line)
		if match:
		 	if dst != None and len(morphs) > 0:
		 		chunk = Chunk(cid, morphs, dst)
		 		sen.append(chunk)

		 	cid = int(match.group(1))
		 	dst = int(match.group(2))
		 	if dst != -1:
		 		if not id2src.has_key(dst):
		 			id2src[dst] = []
		 		id2src[dst].append(cid)

		 	morphs = []
		elif re.search(r'^EOS$', line):
			count += 1
			if dst != None and len(morphs) > 0:
				chunk = Chunk(cid, morphs, dst)
		 		sen.append(chunk)

		 	for i in xrange(0, len(sen)):
		 		ck = sen[i]
		 		if id2src.has_key(i):
		 			ck.set_srcs(id2src[i])

			sentences.append(sen)
			sen = []
			morphs = []
			id2src = {}
		else:
			fields = line.split("\t")
			surf = fields[0]
			features = fields[1].split(',')
			base = features[-3]
			pos  = features[0]
			pos1 = features[1]
			morph = Morph(surf, base, pos, pos1)
			morphs.append(morph)
	f.close()

	sys.stderr.write('Number of sentences: %d\n' % count)
	return sentences

def read_chunks():
	return __read_chunks('../../data/neko.txt.cabocha')

if __name__ == '__main__':
	sentences = read_chunks()
	sen = sentences[7]
	for ck in sen:
		print '%dD\t%s' % (ck.dest(), ck.surf())

