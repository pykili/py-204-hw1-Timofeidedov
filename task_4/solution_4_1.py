n=0
while n<=10:
  a=input()
  n=n+1
  i=0
  j=0
  form=''
  lemma=''
  if a[0] != '#' and a[0] != ' ':
    while a[i]!='\t':
        i=i+1
    i=i+1
    j=i
    while a[j]!='\t':
        j=j+1
    j=j+1
    while a[j]!='\t':
      lemma=lemma+a[j]
      j=j+1
    while a[i]!='\t':
      form=form+a[i]
      i=i+1
    if form!=lemma:
      print (form)
      print (lemma)
