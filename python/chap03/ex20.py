# -*- coding: utf-8 -*-
#!/usr/bin/python

import gzip
import sys
import json
import codecs
import re

# 20. Đọc vào dữ liệu JSON
# Đọc dữ liệu từ file JSON chứa các tài liệu Wikipedia, trích xuất & hiển thị nội dung của tài liệu có liên quan đến "イギリス" (có nghĩa là nước Anh). Sử dụng các nội dung của tài liệu được trích xuất này để thực thi các nhiệm vụ trong các bài tập từ 21-29.

def extract_wikidocs():
    filename = '../../data/jawiki-country.json.gz'
    f = gzip.open(filename, 'rU')
    wiki_docs = []
    for line in f:
        line = line.rstrip()
        doc = json.loads(line, 'utf-8')
        if re.search(ur'イギリス', doc['text']):
            wiki_docs.append(doc)    
    f.close()

    return wiki_docs

def main():
    wiki_docs = extract_wikidocs()
    print '# Wikipedia articles related to イギリス: %s' % len(wiki_docs)
    for doc in wiki_docs:
        # print json.dumps(doc, ensure_ascii=False).encode('utf-8')
        print doc['title'].encode('utf-8')
        print doc['text'].encode('utf-8')

if __name__ == '__main__':
    main()

