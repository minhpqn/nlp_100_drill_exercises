# -*- coding: utf-8 -*-
""" 51. Tách từ
    Coi ký tự trắng (space) là ký tự phân tách các từ.
    Lấy đầu ra của bài 50 làm đầu vào, trích xuất các từ trong các câu và
    in ra theo định dạng: mỗi dòng 1 từ. In ra dòng trắng để đánh dấu
    kết thúc câu.
"""

# SYNOPSIS: python ex50.py | python ex51.py

import re
import os
import sys

def clean(tk):
	match = re.search(r'^[\.,!\?;:\(\)\[\]\'\"\s\t]*(.*?)[\.,!\?;:\(\)\[\]\'"\s\t]*$', tk)
	if match:
		return match.group(1)
	return tk

for line in sys.stdin:
    line = line.strip()
    for w in line.split():
        print clean(w)
    print
    
