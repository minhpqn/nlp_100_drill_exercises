# -*- coding: utf-8 -*-
#!/usr/bin/python
import re
from ex20 import extract_wikidocs

# 22. Trích xuất các tên đề mục (Category name)
# Trích xuất tên đề mục của trong các tài liệu. Trong bài tập này, cần trích xuất chính xác các tên đề mục chứ không phải dòng chứa tên đề mục.

def main():
    wiki_docs = extract_wikidocs()
    for doc in wiki_docs:
        lines = doc['text'].split('\n')
        for line in lines:
            # TODO: extract exact category name
            if re.search(ur'Category:.*', line):
                print line.encode('utf-8')

if __name__ == '__main__':
    main()                
    


