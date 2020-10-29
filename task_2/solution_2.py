user_input = input()
most_frequent_character=''
i=0
i1=0
b=0
a=0
while i<len(user_input):
  while i1<len(user_input):
    if user_input[i] == user_input[i1]:
      a=a+1
    i1=i1+1
  if a>=b:
    b=a
    most_frequent_character=user_input[i]
  a=0
  i1=0
  i=i+1
print(most_frequent_character)
