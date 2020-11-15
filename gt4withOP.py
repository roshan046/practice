def gtwithOP(a,b,c,d):
    if a>b and a>c and a>d:
        return a
    
    if b>a and b>c and b>d:
        return b
    
    if c>a and c>b and c>d:
        return c
    
    if d>a and d>b and d>c:
        return d
    
    if a==b and a==c and a==d:
        return 'equal'
ans = gtwithOP(8,8,8,8)
print(ans)