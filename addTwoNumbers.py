def num(x):
  som=0
  for i in range(len(x)):
    som += x[i]*pow(10,i)
  return som
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=str(num(a)+ num(b))
lst=[]
for i in range(len(c)):
  lst.append(int(c[i]))
lst.reverse()
print(lst)