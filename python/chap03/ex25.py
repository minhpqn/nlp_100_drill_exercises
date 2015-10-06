# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import re
from ex20 import extract_wikidocs

# 25. Trích xuất templates
# Trích xuất vị trí và tên các folder có template "基礎情報" trong tài liệu.

def main():
    docs = extract_wikidocs()
    pattern = re.compile(ur'{{基礎情報.+?}}', re.M | re.DOTALL)
    for doc in docs:
        matches = pattern.findall(doc['text'])
        for m in matches:
            sys.stdout.write(m.encode('utf-8'))

if __name__ == '__main__':
    main()
