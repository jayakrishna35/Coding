n=3000
d={}
sum1=0
s=[i for i in range(n)]
i=2
while(i*i<=n):
  if s[i]==i:
    for j in range(i*i,n,i):
     s[j]=i
  i+=1
num=int(input())
for k in range(num):
    lsum=0
    while(k!=1):
     if s[k] in d:
         d[s[k]]+=1
     else:
         d[s[k]]=1
     k=k//s[k]
 
    for j in d.keys():
         if j not in s:
             break
         else:
             lsum+=d[]
             sum1=lsum
         
print(sum1)
