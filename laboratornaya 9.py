# блок а номер 4
def sumcifr(n):
    if n < 10:
        return n
    if n > 9:
        return sumcifr(n//10) + n%10
print(sumcifr(546))
# блок б номер 4
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


print("YES" if is_prime(int(input())) else "NO")
