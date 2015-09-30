# -*- coding: utf-8 -*-
#!/usr/bin/python

# 17. Đưa ra các các xâu ký tự duy nhất (unique) trong cột 1
# Đưa ra các xâu ký tự duy nhất trong cột 1 của file.
# Sử dụng lệnh cut, sort, uniq để thực hiện nhiệm vụ.

# Confirm by using the command:
# % cut -f 1 ../../data/hightemp.txt | sort
# Note that sorting unicode strings may have different outputs
# based on OS (set Set LC_ALL=C before sorting)
# Solution: http://stackoverflow.com/questions/3412933/python-not-sorting-unicode-properly-strcoll-doesnt-help

# print out sorted unique strings in the column n
def unique_strings(filename, n):
    f = open(filename, 'rU')
    strdict = {}
    for line in f:
        line = line.rstrip()
        cols = line.split()
        col = cols[n-1]
        strdict[col] = None
        
    f.close()

    for key in sorted(strdict.keys()):
        print key

def main():
    unique_strings('../../data/hightemp.txt', 1)

if __name__ == '__main__':
    main()
    
    
    
