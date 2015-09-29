# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys

# 15. Trích xuất ra N hàng cuối cùng của file
# Viết chương trình trích xuất ra N hàng cuối cùng của file. Chương trình nhận đầu vào từ dòng lệnh là số tự nhiên N.
# Sử dụng lệnh tail trong unix để thực hiện công việc.

# Confirm the result
# % python ex15.py 2
# % tail -n 2 ../../data/hightemp.txt

# Read n lines from the end of a file
# This solution cannot work if the size of a file does not fit the memory
def tail_slow(filename, n):
    if n == 0:
        print 'illegal line count: 0'
        sys.exit(1)

    f = open(filename, 'rU')
    lines = f.readlines()
    f.close()
    
    start = max(0, len(lines) - n)
    for i in xrange(start, len(lines)):
        sys.stdout.write(lines[i])

# TODO: implement an efficient solution for very big files
def tail(filename, n):
    if n == 0:
        print 'illegal line count: 0'
        sys.exit(1)

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print 'usage: N'
        sys.exit(1)

    n = int(args[0])
    filename = '../../data/hightemp.txt'
    tail_slow(filename, n)

if __name__ == '__main__':
    main()
    
