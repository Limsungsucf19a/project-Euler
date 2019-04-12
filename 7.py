primes = []
prime_cnt = 0
i = 2
    
while (prime_cnt < 10001):
        isPrime = True
        for j in primes:
            if i % j == 0:
                isPrime = False
                break
            elif j > i**0.5:
                break
        if isPrime:
            print(prime_cnt)
            primes.append(i)
            prime_cnt = prime_cnt + 1
        i = i + 1
print(primes[10000])      
 
 





