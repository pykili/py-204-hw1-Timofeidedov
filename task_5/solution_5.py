n=0
x=0
y=0
while n<10:
  a=input()
  n=n+1
  i=0
  j=0
  z=0
  x1=0
  y1=0
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
    form1=lemma
    c=len(lemma)+i
    while a[i]!='\t':
      form=form+a[i]
      if i>c-1:
        form1=form1+a[i]
      i=i+1
    if form!=lemma and form1==form :
      while z<len(form):
        if form[z] in 'eöü':
          x1=x1+1
        if form[z] in 'aou':
          y1=y1+1
        z=z+1
      if (x1>0 and y1==0) or (y1>0 and x1==0) or (x1==0 and y1==0):
        x=x+1
      else: 
        y=y+1
print('Следует'+str(x)+' раз')
print('Не следует'+str(y)+' раз')
