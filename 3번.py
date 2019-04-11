# 소인수분해 프로그램

a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x = int(input("인수분해할 숫자입력"))         
d = 2   
i = 0                   

while d <= x:
    if x % d == 0:         
        a[i] = d           
        x = x / d 
        i = i + 1  
    else:
        d = d + 1  
       
print(a)       
print(max(a))  



