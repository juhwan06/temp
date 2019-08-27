import random

# 데이터 종류 : 정수, 소수, 문자, 참/거짓

a = []
for q in range(10):
    flag = 0
    if (q == 0):
        a.append(random.randrange(1, 10))
    else:
        b = random.randrange(1, 10)
        for j in range(len(a)):
            if (b == a[j]):
                flag = 1
                break
        if (flag != 1):
            a.append(b)
c = a[0]
for i in range(len(a)):
    if(c < a[i]):
        c = a[i]
print(a)
print(c)
 
