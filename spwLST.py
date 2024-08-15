# -*- coding: utf-8 -*-
# @Time    : 2024/8/18 18:37:02
# @Author  : ZMF
# @FileName: spwLST.py
# @Software: PyCharm
# @IDE: PyCharm
# @E-Mail: ZZMF20110806@163.com
with open('meat.txt', 'r+', encoding='utf-8') as meat:
    l = meat.readlines()
    lst = []
    for i in l:
        lst.append(i.replace('\n',''))

print(lst)