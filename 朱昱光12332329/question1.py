# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:26:14 2023

@author: zyg
"""
import random
#第一问解答
def Print_values(a,b,c):
# 获取用户输入的数字
    if a <= b <= c:
        print(c, b, a, sep=', ')            
    elif b <= a <= c:
        print(c, a, b, sep=', ') 
    elif b <= c <= a:
        print(a, c, b, sep=', ')
    elif c <= b <= a:
        print(a, b, c, sep=', ')    
    elif c <= a <=b:
        print(b, a, c, sep=', ' )
    elif a <= c <= b:
        print(b, c, a, sep=', ')
    elif a == c == b:
        print(a, b, c, sep=', ')
a = random.random()
b = random.random()
c = random.random()
Print_values(a,b,c)
