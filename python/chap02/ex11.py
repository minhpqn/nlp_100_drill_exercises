# -*- coding: utf-8 -*-
import re

# 11. Biến đổi các ký tự tab thành space
# Chuyễn mỗi ký tự tab thành ký tự space. Xác nhận kết quả lần lượt bằng các lệnh sed, tr, và expand.

# Confirm the results with unix command
# command sed:
# On Mac OS use "Ctrl + V" followed by a tab key for the tab character
# % sed 's/       / /g' < ../../data/hightemp.txt
# On Unix systems just use \t
# % sed 's/\t/ /g' < ../../data/hightemp.txt
# References for sed command:
#  http://www.grymoire.com/Unix/Sed.html#uh-0
#  http://www.tutorialspoint.com/unix_commands/sed.htm
# command tr:
# % cat ../../data/hightemp.txt | tr '\t' ' '
# command expand:
# % expand ../../data/hightemp.txt | tr -s " "

def tab_to_space(filename):
    f = open(filename, 'rU')
    for line in f:
        print re.sub(r'\t', ' ', line),
    f.close()

def main():
    filename = '../../data/hightemp.txt'
    tab_to_space(filename)

if __name__ == '__main__':
    main()    
        
