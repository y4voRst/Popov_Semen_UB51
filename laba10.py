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
