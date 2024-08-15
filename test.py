# -*- coding: utf-8 -*-
# @Time    : 2024/8/16 08:11:25
# @Author  : ZMF
# @FileName: test.py
# @Software: PyCharm
# @IDE: PyCharm
# @E-Mail: ZZMF20110806@163.com
import datetime

print(str(datetime.date.today() - datetime.timedelta(datetime.date.weekday(datetime.date.today()))))
print(str(datetime.date.weekday(datetime.date(2024, 8, 19))))