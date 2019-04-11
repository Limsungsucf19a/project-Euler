 
n = 0
con = 0
#list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list = [1,2,3]

while True:
    n = n + 1
    for i in list:
        print(n,i)
        if n%list[i] != 0:
            break
        if list[i] == 3:
            con = 1
            break
    if con == 1:
        break
 
print(n)
