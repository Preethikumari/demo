c=int(input())
d=int(input())
for a in range(c,d+1):
	b=0
	z=a
	while z>0:
		y=z%10
		b+=y**3
		z//=10
	if a==b:
		print(a)
