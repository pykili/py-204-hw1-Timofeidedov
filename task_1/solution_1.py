a=input()
b=0
i=0
while i<len(a):
  c=int(a[i])
  if c>b:
    b=c
  i=i+1
print(b)
