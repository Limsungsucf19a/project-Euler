# 최대공약수
def gcd(a, b):
      while (b != 0):
        temp = a % b
        a = b
        b = temp
      return abs(a)


# 최소 공배수 
def lcm(a, b):
    gcd_value = gcd(a, b)
    if (gcd_value == 0): 
        return 0 
    return abs( int((a * b) / gcd_value) )

print(gcd(12,14))
print(lcm(12,14))