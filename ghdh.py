#a
k1=int(input())
l2=list(map(int,input().split()))
rem=1
l=[]
for i in l2:
  rem=rem*i
for i in l2:
  l.append(rem//i)
print(*l)
