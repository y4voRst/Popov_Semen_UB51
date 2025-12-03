#1 номер 4 вариант
def evcl(a, b): 
    while a != 0 and b != 0:
        if a > b: 
            a = a - b
        else: 
            b = b - a 
    return max(a, b) #если дробь несократима то ретурнет 1


if (evcl((A/B),(C/D))) == 1:
    print((A/B) / (C/D))
else: print("дробь сократима")
#2 номер 4 вариант
def inside(x, y, a, b, R):
    dist_squared = (x - a)**2 + (y - b)**2
    return dist_squared < R**2

def count(points, a, b, R):
    count = 0
    for x, y in points:
        if inside(x, y, a, b, R):
            count += 1
    return count

a, b, R = 0, 0, 5
points = [(1, 2), (5, 5), (0, 0), (6, 0)]

cnt = count(points, a, b, R)
print(cnt)

#9 1
def sumcifr(n):
    if n < 10:
        return n
    if n > 9:
        return n%10 + sumcifr(n//10)
a = 21
cnt = 0
while a > 0:
    a = a - sumcifr(a)
    cnt += 1
print(a, cnt)

#9 2
def proiz(n):
    a = 1
    for i in n:
        a *= i
    return a

def srar(n):
    b = 0
    for i in n:
        b += i
    return b/len(n)
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
print("Массив a: ", proiz(a), srar(a))
print("Массив b: ", proiz(b), srar(b))
print("Массив c: ", proiz(c), srar(c))
