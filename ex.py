def expo(basnum,pownum):
   result=1
   for i in range(pownum):
      result=result*basnum
   return result
print(expo(2,5))
