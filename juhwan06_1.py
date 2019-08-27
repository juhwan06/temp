

'''
i = 0
while(i != 100):
    print(i)
    i = i+1
'''

'''
for i in range (1,100):
    a =  i % 10
    if(a == 3 or a == 6 or a==9):                              # 3, 6, 9 _1
        print("*")
    elif:
        print(i)
        '''

'''
for i in range (1,100):
    a = i % 10
    b = i - a                                                  # 3, 6, 9 _2
        if (a == 3 or a == 6 or a == 9):
            print("**")
        else:
            print("*")

    elif(a == 3 or a == 6 or a == 9):
        print("*")
    else:
        print(i)
'''
'''
a = int(input())
b=1
c=0
while(a < b):
    if(int(a % b) > a % b):
        b + 1
    else:
        c + 1
if(c>=3):
    print("not prime")
else:
    print("prime")                      #소수구하기
'''
'''
a= int(input())
a= True
for i in range(2, int(a/2)+1):
    if (a % i ==0):
        a =False
        break
if(a):
    print("prime")
else:
    print("not prime")
    '''
