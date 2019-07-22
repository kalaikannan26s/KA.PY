k1=int(input())
l1=input()
a=list(map(int,l1.split()))
str1=""
a.reverse()
for i in a:
    str1+=str(i)+"->"
a=str1.strip('->')
print(a)
