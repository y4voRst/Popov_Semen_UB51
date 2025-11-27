# 1-й
def getMtrx(name):
    matr = []
    with open(name, "r") as f:
        for line in f:
            row = [int(x) for x in line.split()]
            matr.append(row)
    return matr

maxSum, st = 0, []
for i in getMtrx("Попов Семён Максимович_УБ-51_vvod.txt"):
    if maxSum < sum(i):
        maxSum = sum(i)
        st = i
print("строка с макс числом: " + str(st) + "сумма строки: " + str(maxSum))

f = open("Попов Семён Максимович_УБ-51_vivod.txt", 'w', encoding="utf-8")
f.write("строка с макс числом: " + str(st) + "сумма строки: " + str(maxSum))
# 2-й
def getMtrx(name):
    matr = []
    with open(name, "r") as f:
        for line in f:
            row = [int(x) for x in line.split()]
            matr.append(row)
    return matr

a = getMtrx("Попов Семён Максимович_УБ-51_vvod2.txt")

for i in range(len(a)):
    for j in range(len(a)):
        if a[i][j]<0: a[i][j]=0
        elif a[i][j]>0: a[i][j]=1

st = ''
for i in range(len(a)):
    s = ''
    for j in range(0, i+1):
        s += str(a[i][j])
    st += s + '\n'
f = open("Вывод2.txt", "w")
f.write(st)
# 3-й
def getMtrx(name):
    mtrx = []
    with open(name, "r") as f:
        for line in f:
            row = [int(x) for x in line.split()]
            mtrx.append(row)
    return mtrx

k = 3
maks = 0
b = 0
for i in getMtrx("Попов Семён Максимович_УБ-51_vvod3.txt"):
    for j in i:
        if j % k == 0:
            b += 1
        maks = max(j, maks)
f = open("Вывод3.txt", "w", encoding="utf-8")
f.write(str('количество элементов кратных k: ' + str(b) + 'наибольший из этих элементов: ' + str(maks)))
# 4-й
from math import *
def getMtrx(name):
    mtrx = []
    with open(name, "r") as f:
        for line in f:
            row = [int(x) for x in line.split()]
            mtrx.append(row)
    return mtrx
def vivodMtrx(mtrx,name):
    f = open(name, "w")
    for ln in mtrx:
        for w in ln:
            f.write(str(w) + " ")
        f.write('\n')

maks = 0
stol, strok = 0, 0
a = getMtrx("Попов Семён Максимович_УБ-51_vvod4.txt")
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
vivodMtrx(b, "Вывод4.txt")
