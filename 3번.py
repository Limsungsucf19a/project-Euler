# 소인수분해 프로그램

x = int(input("인수분해할 숫자입력"))         
d = 2                      

while d <= x:
    if x % d == 0:         
        print(d)            
        x = x / d   
    else:
        d = d + 1  

      



