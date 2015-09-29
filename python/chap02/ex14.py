# -*- coding: utf-8 -*-
import sys

# 14. Trích xuất ra N hàng đầu tiên của file
# Viết chương trình trích xuất ra N hàng đầu tiên của file. Biến số dạng dòng lệnh là số tự nhiên N.
# Sử dụng lệnh head trong unix để thực hiện công việc.

# Confirm the result
# % python ex14.py 2
# % head -n 2 ../../data/hightemp.txt

def head(filename, n):
    if n == 0:
        print 'illegal line count: 0'
        sys.exit(1)

    f = open(filename, 'rU')
    i = 1
    for line in f:
        if i > n:
            break
        sys.stdout.write(line)
        i += 1

    f.close()

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print 'usage: N'
        sys.exit(1)

    n = int(args[0])
    filename = '../../data/hightemp.txt'
    head(filename, n)

if __name__ == '__main__':
    main()    
