a=int(input())
order = len(str(a))
b = 0
temp = a
while temp > 0:
   digit = temp % 10
   b += digit ** order
   temp //= 10
if a == b:
   print("yes")
else:
   print("no")
