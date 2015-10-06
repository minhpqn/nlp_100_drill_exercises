# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import re
from ex20 import extract_wikidocs

# 25. Trích xuất templates
# Trích xuất vị trí và tên các folder có template "基礎情報" trong tài liệu.
# Lưu kết quả trong các đối tượng dictionary. Tham khảo về templates tại [đây](https://en.wikipedia.org/wiki/Help:Infobox).

# Return a dictionary object from given an info box in the format
# {{基礎情報 国
#  |略名 =エジプト
#  |日本語国名 =エジプト・アラブ共和国
#  |公式国名 ='''{{lang|ar|جمهورية مصر العربية}}'''
#  |国旗画像 =Flag of Egypt.svg
# }}
def parse_infobox(template):
    box = {}
    lines = template.split('\n')
    pattern = re.compile(r'\|([^=]+) =([^=<]+)')
    for line in lines:
        matches = pattern.findall(line)
        for tp in matches:
            key = tp[0]
            key = key.strip()
            val = tp[1]
            val = val.strip()
            box[key] = val
            
    return box        

def get_infobox():
    docs = extract_wikidocs()
    objs_list = []
    pattern = re.compile(ur'{{基礎情報.+?^}}\n', re.M | re.DOTALL)
    for doc in docs:
        matches = pattern.findall(doc['text'])
        for m in matches:
            dict_obj = parse_infobox(m)
            objs_list.append(dict_obj)
            
    return objs_list        

def main():
    infobox_list = get_infobox()
    for obj in infobox_list:
        for k in sorted(obj.keys()):
            print '%s: %s' % (k.encode('utf-8'), obj[k].encode('utf-8'))
        print    

if __name__ == '__main__':
    main()
