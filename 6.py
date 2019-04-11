
sum = 0
sum2 = 0

for x in range  (1,101):
    sum = sum + x**2

for x in range  (1,101):
    sum2 = sum2 + x

sum2 = sum2**2
diff = sum2 - sum
print (sum, sum2, diff)