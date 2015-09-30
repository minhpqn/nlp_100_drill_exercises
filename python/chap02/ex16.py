# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
import string

# 16. Chia file thành N phần
# Chia file thành N phần (đơn vị là các hàng trong file). Chương trình nhận đầu vào từ dòng lệnh là số tự nhiên N.
# Sử dụng lệnh split để thực hiện công việc.
# Sau đó, cải tiến chương trình để chia thành thành N phần bằng nhau (thay vì N lines mỗi file).

# Confirm the result by split
# % split -l 8 ../../data/hightemp.txt
# % python ex16.py 8
# Divide a file into N files
# % python ex16.py --files 3
#  (get the same results as % python ex16.py 8)
# Also try:
# % python ex16.py --files 5
#   (should output 5 file, the first file contains 4 lines,
#    each file of last 4 files contains 5 lines)

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))
    
def writelines(filename, lines):
    f = open(filename, 'w')
    f.writelines(lines)
    f.close()

# Return the next filename given the current filename
# e.g., xaa -> xab
def next_filename(current):
    suffix_len = len(current) - 1
    alphabets = list(string.ascii_lowercase)
    charidx = {}
    for i in range(len(alphabets)):
        charidx[ alphabets[i] ] = i

    # solution 1: use recursive function
    # TODO: implement non-recursive solution
    if suffix_len == 0:
        return None

    last_char_idx = charidx[ current[suffix_len] ]
    
    if last_char_idx < len(alphabets) - 1:
        return current[0:suffix_len] + alphabets[last_char_idx + 1]
    else:
        prefx = next_filename(current[0:suffix_len])
        if prefx == None:
            return None
        else:
            return prefx + 'a'
        
# test if function next_filename() works properly
def test_next_filename():
    print 'next_filename'
    test(next_filename('xa'), 'xb')
    test(next_filename('xab'), 'xac')
    test(next_filename('xaz'), 'xba')
    test(next_filename('xyz'), 'xza')
    test(next_filename('xazz'), 'xbaa')
    test(next_filename('xzz'), None)
    test(next_filename('xz'), None)
        
def split_by_nlines(filename, nlines, suffix_length = 2):
    f = open(filename, 'rU')
    lines = f.readlines()
    f.close

    nfile = int( len(lines)/nlines )
    if nfile * nlines < len(lines):
        nfile += 1

    prefix = 'x'
    current = prefix + 'a' * suffix_length
    for i in xrange(nfile):
        filename = current
        l = i * nlines
        r = min( (i+1) * nlines, len(lines) )
        writelines(filename, lines[l:r])
        
        current = next_filename(current)

def split_by_nfiles(filename, nfiles, suffix_length = 2):
    f = open(filename, 'rU')
    lines = f.readlines()
    f.close

    prefix = 'x'
    current = prefix + 'a' * suffix_length
    nlines = int( len(lines)/nfiles )

    resi = len(lines) - nlines * nfiles

    l = 0
    r = 0
    for i in xrange(nfiles-resi):
        filename = current
        l = r
        r = l + nlines
        writelines(filename, lines[l:r])
        current = next_filename(current)

    # write the last resi files
    for i in xrange(nfiles-resi, nfiles):
        filename = current
        l = r
        r = l + (nlines+1)
        writelines(current, lines[l:r])
        current = next_filename(current)

def main():
    args = sys.argv[1:]
    if not args:
        print 'usage: [ --files ] N'
        sys.exit(1)

    byfile = False    
    if args[0] == '--files':
        byfile = True
        del args[0]
    
    if len(args) != 1:
        print 'usage: [ --files ] N'
        sys.exit(1)

    n = int(args[0])
    filename = '../../data/hightemp.txt'
    if byfile:
        split_by_nfiles(filename, n)
    else:    
        split_by_nlines(filename, n)

if __name__ == '__main__':
    main()    
    
    



