# номер 1 вариант 4
matr = [[1, 2, 3, 5, 5], [5, 7, 3, 2, 2], [4, 1, 50, 1, 5], [2, 5, 1, 5, 9]]
maxSum, st = 0, []

for i in matr:
    if maxSum < sum(i):
        maxSum = sum(i)
        st = i
print("строка с макс числом: " + str(st) + "сумма строки: " + str(maxSum))

minSum, st1 = 10000000, []
for i in matr:
    if minSum > sum(i):
        minSum = sum(i)
        st1 = i
print("строка с мин числом: " + str(st) + "сумма строки: " + str(minSum))
# номер 2 вариант 4
n = 3
a = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)
for i in range(n):
    for j in range(n):
        print(a[i][j], end =' ')
    print()

for i in range(n):
    for j in range(n):
        if a[i][j]<0: a[i][j]=0
        elif a[i][j]>0: a[i][j]=1

def diag(matr):
    s = []
    n = len(matr)
    for i in range(n):
        for j in range(i):  
            print(matr[i][j])
    return "готово"
print(diag(a))
# номер 1 вариант 9
a = [[6, 9, 2], [12, 15, 17], [3, 18, 7]]
k = 3
maks = 0
b = 0
for i in a:
    for j in i:
        if j % k == 0:
            b += 1
        maks = max(j, maks)
print('количество элементов кратных k: ',b, 'наибольший из этих элементов: ', maks)
# номер 2 вариант 9
from math import *
a = [[54, 1, -2, 25, 1], [1, -15, 1, 1, 93], [37, 1, 100, 1, -1], [1, 80, 1, -72, 5], [53, -2, 1, 9, 1]]
maks = 0
stol, strok = 0, 0
for i in a:
    for j in i:
        if abs(j) > maks:
            maks = abs(j)
            stol = a.index(i)
            strok = i.index(j)
b = []
for i in range(len(a)):
    if i == strok:
        continue
    row = []
    for j in range(len(a)):
        if j == stol:
            continue
        row.append(a[i][j])
    b.append(row)
print(b)
