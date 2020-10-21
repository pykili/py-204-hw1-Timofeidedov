user_input=input()
alphabet=''
i=0
while i<len(user_input):
  if user_input[i] in alphabet :
    alphabet=alphabet
  else:
    alphabet=alphabet+user_input[i]
  i=i+1
print(alphabet)
