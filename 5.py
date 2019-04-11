 
n = 0
con = 0
#list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list = [1,2,3,4,5,6,7,8,9,10]

while True:
    n = n + 1
    for i in list:
        print(n,i)
        #list의 모든 수로 나누어 떨어질때까지 값을 찾음
        #하나라도 중간에 나누어 떨어지지 않으면 다음수로 증가
        if n%list[i] != 0: 
            break
        if list[i] == 10:
            con = 1
            break
    if con == 1:
        break 
 
print(n)
