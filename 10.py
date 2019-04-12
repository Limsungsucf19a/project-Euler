primes = []
sum = 0
i = 2
while True:
        isPrime = True
        for j in primes:
            if i % j == 0:
                isPrime = False
                break
            elif j > i**0.5:
                break
        if isPrime:
            primes.append(i)
            prime = i
         #   print(prime)
            if prime < 2000000:
               sum = sum + prime
            elif prime >= 2000000:
               break
        i = i + 1
print(sum)      
 