a=input()
i=0
left=''
right=''
while a[i]!=' ':
  left=left+a[i]
  i=i+1
i=i+1
while i<len(a):
  right=right+a[i]
  i=i+1
k=0
n=0
trueaf=''
if len(left)<=len(right):
  while k<len(left) and n<len(right):
    if left[k]==right[n]:
      trueaf=trueaf+left[k]
      k=k+1
      n=n+1
    else:
      n=n+1
  if trueaf==left:
    print('YES')
  else:
    print('NO')
else:
  print('NO')
