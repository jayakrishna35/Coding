result=0
for value in range(0,11):
   result=result+value
   faf=value-1
   if faf>0:
      print("current value ",value," previous value ",faf,"Sum: ",result)
   else:
       print("current value ",value," previous value 0 ","Sum: ",result)
