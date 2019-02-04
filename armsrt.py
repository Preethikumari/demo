a=int(input())
length = len(str(a))
b=0
c=a
while(c!= 0):
	b = b + ((c % 10) ** length)
	c=c // 10
if b==a:
	print("yes")
else:
	print("no")
