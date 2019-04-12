
def getPrimeList(num):
    primes = []
    if num < 2:
        return primes
    for i in range(2, num+1):
        isPrime = True
        for j in primes:
            if i % j == 0:
                isPrime = False
                break
            elif j > i**0.5:
                break
        if isPrime:
            primes.append(i)
    return primes
 
# 1000 이하의 소수
if __name__ == '__main__':
    print(getPrimeList(1000))




