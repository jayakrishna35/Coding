n=int(input())
s=[i for i in range(n+1)]
i=2
while(i*i<=n):
    if s[i]==i:
        for j in range(i*i,n+1,i):
            s[j]=0
    i+=1
s[0]=0
s[1]=0
s=list(set(s))
s.sort()
s=s[1:]
#print(s)
for i in s[:(len(s)//2)]:
    #print(i)
    if n-i in s:
        print(i,n-i)
