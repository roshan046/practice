def gtwithList(a,b,c,d):
    lst=[]
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.append(d)

    return max(lst) , min(lst) , sum(lst) , sum(lst)/len(lst)

print(gtwithList(5,6,9,8))