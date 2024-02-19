def n_to_zero(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for i in n_to_zero(n):
    print (i, end=" ")