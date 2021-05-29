def factors(n):
    bool=False
    for i in range(2,n):
      if n%i==0:
        a=i 
        b=int(n/a)
        if (prime(a) and prime(b)):
            bool=True
            
    return bool
def prime(m):
    prime=True
    for i in range(2,m):
        if m%i==0:
            prime=False
            
            
    return prime
if __name__ == '__main__':
        num=int(input())
        a="NO"
        for i in range(1,num//2):
            x=i 
            y=num-i
            if(factors(x) and factors(y)):
                a="YES"
                
print(a)
    
    
