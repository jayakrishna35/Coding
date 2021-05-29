list1=[10,5,3,7,9,78]
list2=[34,4,5,7,98]
result=[]
for i in list1:
   k=i%2
   if k==0:
     result.append(i)
for j in list2:
    l=j%2
    if l!=0:
      result.append(j)
print(result)
