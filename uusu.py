k1=input()
a1=list(map(int,k1.split()))
b1=a1[1]
uv=input()
flag=0
ab2=list(map(int,uv.split()))
for j in range(0,len(ab2)-1):
	for k in range(j+1,len(ab2)):
		if ab2[j]+ab2[k]==b1:
			print("yes")
			flag=1
			break
	if flag==1:
		break
if flag!=1:
	print("no")
