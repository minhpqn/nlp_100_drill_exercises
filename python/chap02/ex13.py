# -*- coding: utf-8 -*-
import sys

# 13. Trộn hai file col1.txt và col2.txt
# Kết hợp nội dung trong 2 file col1.txt và col2.txt để tạo thành một file mới có nội dung giống với cột 1 và cột 2 trong file ban đầu (các cột cách nhau bởi ký tự tab).
# Sử dụng lệnh paste để thực hiện bài tập và xác nhận kết quả của chương trình bạn viết.

# Confirm using paste command
# % paste col1.txt col2.txt

# Paste multiple files into one file
# For variable number of arguments, use tuples with *args
# TODO: paste files with different number of lines
# Output to stdout
def paste(*filenames):
    files = []
    for filename in filenames:
        f = open(filename, 'rU')
        files.append(f)

    f0 = files[0]
    for line1 in f0:
        cols = [line1.rstrip()]
        for i in xrange(1,len(files)):
            line2 = files[i].readline()
            cols.append(line2.rstrip())
        print '\t'.join(cols)

    for f in files:
        f.close()

def main():
    paste('col1.txt', 'col2.txt')

if __name__ == '__main__':
    main()    
    
    
