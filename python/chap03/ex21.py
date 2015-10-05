# -*- coding: utf-8 -*-
#!/usr/bin/python

import re
from ex20 import extract_wikidocs

# 21. Trích xuất các dòng có chứa tên đề mục
# Trong các tài liệu, trích xuất các dòng có chứa tên đề mục (category name hay カテゴリ名).

def main():
    wiki_docs = extract_wikidocs()
    for doc in wiki_docs:
        lines = doc['text'].split('\n')
        for line in lines:
            if re.search(ur'Category:.*', line):
                print line.encode('utf-8')

if __name__ == '__main__':
    main()


