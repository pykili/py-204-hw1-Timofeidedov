alphabet=''
i=0
n=1
while n<=10:
  user_input=input()
  while i<len(user_input):
    if user_input[i] in alphabet :
      alphabet=alphabet
    else:
      alphabet=alphabet+user_input[i]
    i=i+1
  i=0
  n=n+1
print(alphabet)
