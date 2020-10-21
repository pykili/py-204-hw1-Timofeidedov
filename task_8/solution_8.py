n=int(input())
a=0
i=0
while i<=n-1:
    user_input = int(input())
    if user_input==0:
      break
    a=a + user_input
    i=i+1
print(a/i)
