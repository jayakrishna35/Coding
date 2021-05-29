
def rev(x):
    y=x*-1
    if x>0:
        a=int(str(x)[::-1])
    else:
        a=-1*int(str(y)[::-1])
    if a not in range(-2**31,2**31):
        return 0
    else:
        return a

p=int(input())
print(rev(p))
      
