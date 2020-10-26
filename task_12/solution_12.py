a=input()
i=0
i1=1
i2=2
i3=3
occured_twice= False
while i1<len(a):
  i2=i+2
  i3=i+3
  while i3<len(a):
    if a[i2]==a[i] and a[i3]==a[i1]:
  			occured_twice = True
    i2=i2+1
    i3=i3+1
  i=i+1
  i1=i1+1
print(occured_twice)
