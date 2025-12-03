#4
a = 'аааооо'
cnt = 0
while 'а' in a:
    a = a.replace('а', 'о', 1)
    cnt += 1
print(cnt)
print(a.count('о'))

#9
a = 'колесо крутится пока колесо не лопнет'
print(a.count('колесо'))
