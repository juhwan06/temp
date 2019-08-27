# 데이터 종류 : 정수, 소수, 문자, 참/거짓
'''
a = int(input("숫자를 입력하세요 : "))
b = []
for i in range(1,101):
    b.append(i)
c = 1
d = 100
e = 0                                        #이진 검색
while(a != 1111111):

    f = int((c + d) / 2)

    if(f == a):
        e = e + 1
        break
    elif(f < a):
        c = f
        e = e + 1
    elif(f > a):
        d = f
        e = e + 1
print(e)
'''

''''
a = int(input("숫자를 입력하세요 : "))
b = int(input("숫자를 입력하세요 : "))
                                               #최대 공약수 구하기(리스트 이용) 
c = []
for i in range(1,a + 1):
    if((a / i) == int(a / i)):
        c.append(int(a / i))

d = []
for t in range(1,b + 1):
    if((b / t) == int(b / t)):
        d.append(int(b / t))
f = []
for q in range(len(c)):
    e = c[q]
    for w in range(len(d)):
        if(e == (d[w])):
            f.append(d[w])
g = 0
for z in range(len(f)):
    if (f[z] > g):
        g = f[z]
print(g)
'''

'''
a = int(input("숫자를 입력하세요 : "))
b = int(input("숫자를 입력하세요 : "))
                                                     #최대 공약수 구하기(리스트 이용하지 않)
c = 0
d = 0

if(a > b):
    d = a
else:
    d = b
for i in range(1, d + 1):
    if((a % i == 0) and (b % i == 0)):
        e = i
print(e)
'''
