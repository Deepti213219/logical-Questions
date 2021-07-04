

a=["a","b","a","c","b","d"]
#  output =[['a',2],['b',1]['c',1],['d',1]] 
list1=[]
i=0
while i<len(a):
    list2=[]
    count=0
    j=0
    while j<len(a):
        if a[i]==a[j]:
            count=count+1
        j=j+1
    list2.append(a[i])
    list2.append(count)
    if list2 not in list1:
        list1.append(list2)
    i=i+1
print(list1)

