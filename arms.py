c=int(input())
d=int(input())
for a in range(c,d+1):
	b=0
	temp=a
	while temp>0:
		digit=temp%10
		b+=digit**3
		temp//=10
	if a==b:
		print(a)
