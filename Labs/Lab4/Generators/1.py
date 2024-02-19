def sqrt_of_numbers(n):
    for i in range (n+1):
        yield i**2

n = int(input())
for square in sqrt_of_numbers(n):
    print(square, end=" ")