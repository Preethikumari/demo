c=int(input())
d=int(input())
for a in range(c,d+1):
	sum=0
	temp=a
	while temp>0:
		digit=temp%10
		sum+=digit**3
		temp//=10
	if a==sum:
		print(a)
