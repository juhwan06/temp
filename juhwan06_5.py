'''
a = []
for i in range(8):
    a.append(int(input("점수를 쓰세요 : ")))
b = []
c = 0
for j in range(5):
    d = 0
    for w in range(len(a)):
        if(a[d] < a[w]):
            d = w
    b.append([a[d], d])
    a[d] = -1                                   #점수 구하기

e = 0
for q in range(len(b)):
    e = e + b[q][0]

print(e,"점")
for t in range(len(b)):
    print(b[t][1]+1,"번")
'''
'''
a = (1,5)  #튜플

a = {}
a = { "a" : 1, "b" : 2, "c" : 3}
c = { "a" : 4, "b" : 5, "c" : 6}                        #dict (사전) 
b = [a, c]
print(b[1]["a"])
'''
'''
i = int(input("숫자를 입력하세요 : "))

def a(a,b):
    ab = a + b     # 더하기
    return ab

def m(a,b):
    ab = a - b     # 빼기
    return ab
                                                       #함
def x(a,b):
    ab = a * b     # 곱하기
    return ab

def d(a,b):
    ab = a / b     #나누기
    return ab

if(i == 1):
    print(a(5,5))

elif(i == 2):수
    print(m(5,5))

elif(i == 3):
    print(x(5,5))

else:
    print(int(d(5,5)))
'''
'''
def made():
    a=[]
    for i in range(8):
        a.append(int(input("점수를 쓰세요 : ")))
    return a

def count(a):
    b = []
    c = 0
    for j in range(5):
        d = 0
        for p in range(len(a)):
            if (a[d] < a[p]):
                d = p
        b.append([a[d], d])
        a[d] = -1
    return b
def add(b):
    e = 0
    for q in range(len(b)):
        e = e + b[q][0]
    return e
def total(e):
    print(e, "점")
    for t in range(len(b)):
        print(b[t][1] + 1, "번")
    return
a = made()
b = count(a)
e = add(b)
total(e)
'''