l1=int(input())
x1=[int(i) for i in input().split()]
while len(x1)!=0:
	n=len(x1)
	y=len(x1)//2
	if n%2==1:
		print(x1[y])
		x1.remove(x1[y])
	else:
		l1=(x1[y]+x1[y-1])//2
		print(l1)
		x1.remove(x1[y])
		x1.remove(x1[y-1])
