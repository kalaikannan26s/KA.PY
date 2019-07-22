a1,b1=map(int,input().split())
c1=list(map(int,input().split()))
for j in range (0,b1):
    c1=[c1[-1]]+c1[:-1]
print(*c1,end='')
