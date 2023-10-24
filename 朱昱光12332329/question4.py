# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:28:10 2023

@author: zyg
"""

#第四问解答
def Least_moves(n):
    if n==1:
        return 0
    elif n%2!=0:
        return 1+ Least_moves(n-1)
    else:
        return 1+ min(Least_moves(n-1), Least_moves(int(n/2)))
    
import random
n=random.randint(1,100)
result = Least_moves(n)
print(f"当n={n}时，此时Least_moves={result}")