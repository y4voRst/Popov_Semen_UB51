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
