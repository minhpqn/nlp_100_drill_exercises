# -*- coding: utf-8 -*-
#!/usr/bin/python

import urllib2
import urllib
import json
import sys
import re
from ex28 import get_infobox

# 29. Lấy ra các URL của quốc kỳ
# Sử dụng nội dung của các template và lấy ra URl đến quốc kỳ (国旗画像のURL).
# Hint: Gọi API [imageinfo](https://www.mediawiki.org/wiki/API:Properties) của [MediaWWiki](https://www.mediawiki.org/wiki/API:Main_page), biến đổi các file references thành URL.

def image_url(image_name):
    data = {}
    data['action'] = 'query'
    data['titles'] = image_name
    data['prop'] = 'imageinfo'
    data['format'] = 'json'
    data['iiprop'] = 'url'
    url_values = urllib.urlencode(data)
    url = 'https://en.wikipedia.org/w/api.php'
    full_url = url + '?' + url_values
    
    data = urllib2.urlopen(full_url)
    info = data.read()
    image_data = json.loads(info)

    pages = image_data['query']['pages']
    image_url = ''
    for key in pages.keys():
        image_url = pages[key]['imageinfo'][0]['url']
    return image_url

def main():
    infobox_list = get_infobox()
    for obj in infobox_list:
        if obj.has_key(u'国旗画像'):
            flag_name = obj[u'国旗画像']
            flag_name = 'File:' + flag_name
            print flag_name
            flag_url  = image_url(flag_name)
            print flag_url
            
if __name__ == '__main__':
    main()    
