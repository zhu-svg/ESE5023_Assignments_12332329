# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:31:24 2023

@author: zyg
"""

#第五问解答：我和师兄讨论思路，使用itertools函数，在report中有详细记载。
import itertools
import random
def Find_Expression(target):
    def evaluate(expression):
        try:
            return eval(expression)
        except:
            return None
    digits = "123456789"
    add_min = ['+', '-', '']
    solutions = []
    for i in itertools.product(add_min, repeat=len(digits) - 1):
        expression = ''.join(d + op for d, op in zip(digits, i)) + digits[-1]
        result = evaluate(expression)
        if result is not None and result == target:
            solutions.append(expression + '=' + str(target))
    return solutions 
def ExampleFindExpression(target):
    print(f"Find expression ({target}):")
    solutions = Find_Expression(target)
    for solution in solutions:
        print(solution) 
               
c=random.randint(1, 100)
b=len(Find_Expression(c))
print(f"当随机数c={c}时，此时结果如下,并且此时生成的结果有{b}种")
print(Find_Expression(c))


#最大值最小值
Total_solutions = []  
for whole in range(1, 101, 1):
    e = len(Find_Expression(whole))
    Total_solutions.append(e) 
print(Total_solutions)
max_value = max(Total_solutions)

max_indices = [i + 1 for i, value in enumerate(Total_solutions) if value == max_value]
max_indices_str = '或者'.join([f'{idx}' for idx in max_indices])

print(f"最大值是 {max_value}，它出现在：{max_indices_str}")

min_value=min(Total_solutions)
min_indices = [i+1 for i,  value in enumerate(Total_solutions)  if value == min_value]
min_indices_str = '或者'.join([f'{idx}' for idx in min_indices])
print(f"最小值是 {min_value}，它出现在：{min_indices_str}")


#图像
x=[]
y=[]
import matplotlib.pyplot as plt
for i in range(1,100):
    y_value = len(Find_Expression(i))
    x.append(i)
    y.append(y_value)
plt.plot(x, y)
plt.show()