#kalai
n7=int(input())
l=list(map(int,input().split()))
a1=l
c1=[]
while(len(a1)!=1):
	for i1 in range(len(a1)):
		if i1%2!=0:
			c1.append(a1[i1])
	a1=c1
	c1=[]
print(l1.index(a1[0]))
