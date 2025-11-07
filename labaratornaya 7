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
