l=[2,3,2,2,2,4,3,4,1,8]
dic={}
for i in l:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
print(dic[2])
print(dic.keys())
print(dic.values())
print(dic.values(2))

