# -*- coding: utf-8 -*-
""" 58. Trích xuất tuples
    Từ kết quả phân tích dependency của Stanford Core NLP
    (collapsed-dependencies), trích xuất các bộ 3
    [Subject, Predicate, Purpose] và in ra các bộ 3 này (các thành phần
    cách nhau bởi ký tự tab). Subject, Predicate, Purpose được xác định
    dựa vào các tiêu chuẩn sau:
    - Predicate: Là word ở các node con (dependant) của các dependency
      relations: nsubj, dobj
    - Subject: Các node con (dependant) trong các quan hệ nsubj từ predicate
    - Purpose: Các node con (dependant) trong các quan hệ dobj từ predicate
"""

import os
import sys
import re
from xml.dom import minidom

if __name__ == '__main__':
    pass

