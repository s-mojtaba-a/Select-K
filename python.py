def partition(s,start,end,k):
    pivot=s[end]
    i=start
    j=end-1
    if end-start==0:
        return s[start]
    
    while i<=j :
        booli=False
        boolj=False
        if s[i]<=pivot :
            i+=1
            booli=True
        if s[j]>pivot:
            j-=1
            boolj=True
        
        if not boolj and not booli :
            s[i],s[j]=s[j],s[i]
            booli,boolj=False,False
            i+=1
            j-=1
    s[end],s[i]=s[i],s[end]
    if k-1==i :
        return s[i]
    elif k-1 < i :
        return partition (s,0,i-1,k)
    else:
        return partition (s,i+1,end,k)

if __name__ == '__main__': # jast for a test
    s=[6,3,1,3,5,6,9,7,5,2,45,65,43,25,7,89,9,89,0,74,2]
    p=sorted(s)
    print(p)
    for i in range(1,len(s)+1):
        print(partition(s,0,len(s)-1,i))
