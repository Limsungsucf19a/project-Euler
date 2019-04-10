def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

sum = 0
for i in range(1, 34):
    if (fibonacci(i) % 2 == 0):
       sum = sum + fibonacci(i)
       print(fibonacci(i))
print(sum)