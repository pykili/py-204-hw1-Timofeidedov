n=0
while n<=10:
  a=input()
  n=n+1
  i=0
  j=0
  form=''
  lemma=''
  if a[0] != '#' and a[0] != ' ':
    while a[i]!='\t': #за пробелы извиняюсь, но я все еще не особо хорош в синтаксисе питона и боюсь все порушить случайно
        i=i+1
    i=i+1
    j=i
    while a[j]!='\t':
        j=j+1
    j=j+1
    while a[j]!='\t':
      lemma=lemma+a[j]
      j=j+1
    form1=lemma
    c=len(lemma)+i
    while a[i]!='\t':
      form=form+a[i]
      if i>c-1:
        form1=form1+a[i]
      i=i+1
    if form!=lemma and form1!=form :
      print (form)
      print (lemma)
