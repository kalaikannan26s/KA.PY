import sys
n1=list(input())
b2=[]
if len(n1)==1:
    print("yes")
    sys.exit()
for i in range(0,2):
    for i in range(i,len(n1),2):
        b2.append(n1[i])
if b2==n1:
    print("no")
else: print("yes")
