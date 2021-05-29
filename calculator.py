n1=float(input("Enter a number: "))
op=input("Enter a operator: ")
n2=float(input("Enter another number: "))
if op=="+":
  print(n1+n2)
elif op=="-":
  print(n1-n2)
elif op=="*":
  print(n1*n2)
elif op=="/":
  print(n1/n2)
else:
  print("Invalid Operator")
