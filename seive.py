n=int(input())
s=[i for i in range(n+1)]
print(s)
i=2
while(i*i<=n):
     if s[i]==i:
         for j in range(i*i,n+1,i):
             s[j]=0
             
     i+=1
s[0]=0
s[1]=0
print(s)
if(s[n]==1):
    print("prime")
else:
    print("not prime")
