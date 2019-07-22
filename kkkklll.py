k1=input()
temp=""
f=0
for i in range(len(k1)):
  if k1[i]==" ":
    temp+=k1[i]
  elif f==0:
    temp+=k1[i].upper()
    f=1
  elif f==1:
    temp+=k1[i]
    f=0
print(temp)
