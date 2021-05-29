r=int(input("Enter the no.of rows:"))
c=int(input("Enter the no.of columns:"))
matrix=[]
print("Enter the elements one by one:")
for i in range(r):
      a=list(map(int, input().split()))
      b=[]
      for j in range(c):
         a.append(a[r*i+j])
      matrix.append(a)
for i in range(r):
      for j in range(c):
         print(matrix[i][j],end=" ")
      print()
      
