# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:27:08 2023

@author: zyg
"""

#第三问解答
def Pascal_triangle(k):
    if k == 1:
        return [1]
    elif k == 2:
        return [1, 1]
    else:
        row = Pascal_triangle(k - 1)
        new_row = [1]
        for i in range(1, k - 1): 
            new_row.append(row[i - 1] + row[i])
        new_row.append(1)
        return new_row
k = 100  
result = Pascal_triangle(k)
print(result)
k = 200  
result = Pascal_triangle(k)
print(result)