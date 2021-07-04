dic={"A":[3,9,0,7],"B":[6,2,4,5]}
for x in dic:
    list1=[]
    a=len(dic[x])-1
    i=0
    while i<len(dic[x]):
        list1.append(dic[x][a])
        a=a-1
        i=i+1
    y=list1
    dic[x]=y
print(dic)