'''n=int(input())
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
if flag==1:
    print("not prime")
else:
    print("prime")'''
# 2 to n/2
'''n=int(input())
flag=0
for i in range(2,n//2):
    if n%i==0:
        flag=1
        break
if flag==1:
    print("not prime")
else:
    print("prime")'''
# 2 to sqrt of n
'''n=int(input())  
flag=0
for i in range(2,int(n**0.5+1)):
    if n%i==0:
        flag=1
        break
if flag==1:
    print("not prime")
else:
    print("prime")'''
#2 to sqrt of n by importing math
'''import math
n=int(input())
x=int(math.sqrt(n))
flag=0
for i in range(2,x+1):
    if n%i==0:
        flag=1
        break
if flag==1:
    print("not prime")
else:
    print("prime")'''
#2 to sqrt of n using while
'''n=int(input())
flag=0
i=2
while(i*i<=n):
    if n%i==0:
            flag=1
            
            
    i+=1
    if flag==1:
        print("not prime")
    else:
        print("prime")'''

        

    
