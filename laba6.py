#4 1
a = [2, 12, 435, 126, 932, 2187346]
b = max(a)
print(b)
print(a.index(b))

#4 2
a = [2, 4, 6, 8, 1]
b = []
for i in a:
    if i % 2 != 0:
        b.append(i)
if len(b) > 0:
    print(b)
else:
    print("Нечетных чисел нет")

#9 1
from math import *
n = int(input())
a = []
for i in range(n):
    a.append(abs(float(input())))
print("Минимальный по модулю элемент: ", min(a))

#9 2
a = [1,2,3,4,5,6,7,8,9,10]
b = [11,12,13,14,15,16,17,18,19,20]
c = []
for i in a:
    c.append(i)
a = b
b = c
print(a, b)

#XD
