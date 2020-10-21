n=1
a=0
b=0
i=1
while n<=100:
  while i<=(2*n-1):
     if i%2==1 :
       b=b+i
     i=i+1
  if n*n!=b:
    a=a+1
  n=n+1
if a==0:
  print('YES')
else:
  print('NO')

