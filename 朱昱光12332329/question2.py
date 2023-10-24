# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:26:47 2023

@author: zyg
"""

#第二问解答
import random
rows_M1 = 5
cols_M1 = 10
rows_M2 = 10
cols_M2 = 5
# 生成随机矩阵 M1

M1 = [[random.randint(0, 50) for _ in range(cols_M1)] for _ in range(rows_M1)]
# 生成随机矩阵 M2
M2 = [[random.randint(0, 50) for _ in range(cols_M2)] for _ in range(rows_M2)]
# 打印矩阵 M1
print("Matrix M1:")
for row in M1:
    print(row)
# 打印矩阵 M2
print("Matrix M2:")
for row in M2:
    print(row)


def matrix_multip(M1, M2):
    rows_M1 = len(M1)
    cols_M1 = len(M1[0])
    rows_M2 = len(M2)
    cols_M2 = len(M2[0])

 
    if cols_M1 != rows_M2:
        raise ValueError
        
    result = [[0 for _ in range(cols_M2)] for _ in range(rows_M1)]
    for i in range(rows_M1):
        for j in range(cols_M2):
            for k in range(cols_M1):
                result[i][j] += M1[i][k] * M2[k][j]
    return result
result_matrix = matrix_multip(M1, M2)
print(result_matrix)