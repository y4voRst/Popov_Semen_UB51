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
