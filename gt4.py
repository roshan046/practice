def greatest(a,b,c,d):
    if a>b:
        if a>c:
            if a>d:
                return a
            else:
                return d
        else:
            if (c>d):
                return c
            else:
                return d
    else:
        if (b>c):
            if (b>d):
                return b
            else:
                return d
        else:
            if (c>d):
                return c
            else:
                return d

x=int(input("enter first number"))
y=int(input("enter second number"))
z=int(input("enter third number"))
r=int(input("enter fourth number"))
answer=greatest(x,y,z,r)
print(answer)
