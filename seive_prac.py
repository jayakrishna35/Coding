n=6
seive=[1 for i in range(n+1)]
i=2
while(i*i<=n):
    if seive[i]==1:
        for j in range(i*i,n+1,i):
            seive[j]=0
    i+=1
seive[0]=1
seive[1]=1
if seive[n]==1:
    print("prime")
else:
    print("not prime")
