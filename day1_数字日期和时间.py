import math
a = float('inf')
b = float('-inf')
c = float('nan')
math.isinf(a)
math.isnan(c)
round(1.23,1)
round(1.27,2)
math.fsum([1,2,3])
#浮点型精确计算
import decimal
a = decimal.Decimal('4.2')
b = decimal.Decimal('2.1')
a+b
print(a + b)
#数字的格式化输出
x = 1234.56789
format(x,"0.2f") # Two decimal places of accuracy
format(x, '>10.1f') # Right justified in 10 chars, one-digit accuracy

#大型数组运算 用numpy
x = [2,3,4,5,6]
y = [3,4,5,6,7]
x*2
x + 10
x + y
import numpy as np
ax = np.array([2,3,4,5,6])
ay = np.array([3,4,5,6,7])
ax*2
np.sqrt(ax)
np.cos(ax)
ax[0]
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a[:,1]
a[1,:]
a[1:3,1:3]
np.where(a < 10, a, 10)
#矩阵与线性代数运算
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
m.T
m.I
v = np.matrix([[2],[3],[4]])
m * v

#随机选择
import random
values = [1, 2, 3, 4, 5, 6]
random.choice(values)
random.sample(values,2)
random.sample(values,7)
random.shuffle(values);values
random.randint(0,10)
