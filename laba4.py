#4
n = int(input())
s = 0
for i in range(n):
    x = int(input())
    s += x
print(s)

#9
n = int(input())
a, b = 0, 1
s = 0
for i in range(n):
    s += a
    a, b = b, a + b
print(s+1)
