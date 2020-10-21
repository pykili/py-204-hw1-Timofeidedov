a=input()
i=0
i1=len(a)-1
b=0
while i<i1:
  if a[i]!=a[i1] :
    b=b+1
  i=i+1
  i1=i1-1
if b==0:
  print('YES')
else:
  print('NO')
