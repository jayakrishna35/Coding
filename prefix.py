n=1000001
seive=[1]*n
prefix=[0]*n
def pre():
    i=2
    while(i*i<=n):
        if seive[i]==0:
            for j in range(i*i,n,i):
                seive[j]=0
        i+=1
    seive[0]=0
    seive[1]=0
    for i in range(2,n):
        if (seive[i]==1):
            prefix=prefix[i-1]+i
        else:
            prefix[i]=prefix[i-1]
t=int(input())
pre()
for _ in range(t):
    l,r=map(int,input().split())
    print(prefix[r]-prefix[l-1])
    t=t-1
