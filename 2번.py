def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

sum = 0
i = 1

while(fibonacci(i) < 4000000):
        if (fibonacci(i) % 2 == 0):
           sum = sum + fibonacci(i)
           print(fibonacci(i))
        i = i + 1

print(sum)
#4613732