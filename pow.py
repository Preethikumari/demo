def power(y,z):
    if(z==1):
        return(y)
    if(z!=1):
        return(y*power(y,z-1))
y=int(input()
z=int(input())
print(power(y,z))
