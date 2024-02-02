
def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) +1):
        if a % i == 0:
            return False
    return True
def filter_prime(lst):
    primes = []
    for i in lst:
        if is_prime(int(i)):
            primes.append(int(i))
    return primes

lst = input().split(" ")
lst1 = filter_prime(lst)
print(lst1)