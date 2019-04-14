with open("C:\down\q008_data.txt") as file_object:
    lines = file_object.readlines()

print(lines[0])
string=''
for line in lines:
    string=string+line.rstrip()
#print(string)

#for i in range(0,1000):
#    print(string[i:i+13])

#for i in range(0,1000):
#    product =1
#    for j in string[i:i+13]:
#        product = product * int(j)
#    print(string[i:i+13],product)

#from functools import reduce
#for i in range(0,1000):
#    product = reduce(lambda x,y:int(x)*int(y), string[i:i+13])
#    print(string[i:i+13],product)

maxValue =0
for i in range(0,1000):
    product =1
    for j in string[i:i+13]: 
        product = product * int(j)
    if product > maxValue:
        maxValue = product
   # print(string[i:i+13],product, maxValue)
#print(maxValue)
