n=int(input())
a=0
i=0
k=0
while i<=n-1:
    user_input = int(input())
    if user_input==0:
      i=n
    a=a + user_input
    k=k+1
    i=i+1
print(a/k) #это если мы считаем среднее арифметическое с нулем, если без нуля -- будет (a/(k-1))
