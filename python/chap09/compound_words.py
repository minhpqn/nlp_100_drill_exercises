# -*- coding: utf-8 -*-
""" 81. Xử lý tên các nước tạo thành từ các compound words

    Trong tiếng Anh, nhiều từ cạnh nhau có thể tạo thành một từ có ý nghĩa.
    Ví dụ, hợp chủng quốc Hoa Kỳ là "United States", vương quốc Anh là
    "United Kingdom". Nếu chỉ dùng các "United", "State", hay "Kingdom" như
    các từ riêng lẻ, ý nghĩa của các từ này sẽ nhập nhằng. Vì thế trong khi
    tiền xử lý dữ liệu, ta cần xác định các từ ghép này. Đoán nhận các từ
    ghép là một bài toán khó, nên ở đây ta chỉ đoán nhận các từ ghép là tên
    của các nước.

    Trước hết, download danh sách tên của các nước trên Internet.

    Dùng danh sách tên các nước này để đoán nhận các từ ghép là tên nước
    trong dữ liệu sử dụng ở bài 80, sau đó biến đổi các ký tự spaces thành ký
    tự underscore (_) để nối các từ thành phần.

    Ví dụ "United States" sẽ trở thành "United_States", "Isle of Man"
    sẽ trở thành "Isle_of_Man."

    First download country list to Country-List.txt by using the command:
    wget http://vbcity.com/cfs-filesystemfile.ashx/__key/CommunityServer.Components.PostAttachments/00.00.61.18.99/Country-List.txt

"""

import sys
import re

def is_blank(tk):
    if re.search( r'^[\s\t　]*$', tk ):
        return True
        
    return False

def get_processed(line, regx):
    """ Convert spaces in country names into underscore (_)
        from a sentence in a line
    """

    # use sub method to replace spaces in matching parts into _
    matched_parts = regx.findall(line)
    for match in matched_parts:
        _match = re.sub(r'\s+', '_', match)
        line = re.sub(match, _match, line)

    return line        

if __name__ == '__main__':
    # given the preprocessed file in the exercise 80
    datafile = '../../data/enwiki-20150112-400-r10-105752.tokenized.txt'
    output = '../../data/enwiki-20150112-400-r10-105752.preprocessed.txt'

    names = []
    with open('./Country-List.txt', 'rU') as fin:
        for line in fin:
            line = line.strip()
            if is_blank(line): continue
            if re.search(r'\s', line):
                line = re.sub(r'\(', '\\\(', line)
                line = re.sub(r'\)', '\\\)', line)
                names.append(line)

    # create a big regular expression from a list of strings
    regx_str = ''.join( [ '(', '|'.join(names), ')' ] )

    # create a regular expression by using compile method
    regx = re.compile(regx_str)

    with open(output, 'w') as fo:
        with open(datafile, 'rU') as f:
            for line in f:
                line = line.rstrip()
                if is_blank(line): continue
                line  = get_processed(line, regx)
                fo.write( '%s\n' % line )
                
        
