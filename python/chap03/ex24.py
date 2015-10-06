# -*- coding: utf-8 -*-
#!/usr/bin/python

import re
from ex20 import extract_wikidocs

# 24. Trích xuất các liên kết file
# Trích xuất toàn bộ các liên kết đến các media files trong tài liệu.

def main():
    docs = extract_wikidocs()
    pattern = re.compile(ur'(File|ファイル):([^\|]+)')
    for doc in docs:
        # Find all markups File: or ファイル:
        references = pattern.findall(doc['text'])
        for ref in references:
            print ref[1].encode('utf-8')
            
if __name__ == '__main__':
    main()    
