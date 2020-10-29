user_input=input()
alphabet=''
i=0
while i<len(user_input):
  if user_input[i] not in alphabet :
    alphabet=alphabet+user_input[i]
  i=i+1
print(alphabet)
