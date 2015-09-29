# -*- coding: utf-8 -*-

# 10. Đếm số dòng trong file
# Đếm số dòng trong file. Xác nhận kết quả bằng lệnh wc trong unix

# use command wc -l for confirmation
# % wc -l ../../data/hightemp.txt

def line_count(filename):
    n = 0
    f = open(filename, 'rU')
    for line in f:
        n += 1
        
    f.close()    
    return n

def main():
    filename = '../../data/hightemp.txt'
    print "number of lines in %s: %s" %(filename, line_count(filename))

if __name__ == '__main__':
    main()
    
    


