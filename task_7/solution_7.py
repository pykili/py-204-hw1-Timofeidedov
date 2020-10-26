my_string=input()
palindrom=''
n=0
for my_char in my_string:
  palindrom=my_char+palindrom
if my_string==palindrom:
  print('YES')
else:
  print('NO')
