a=["a","b","a","c","d"]
list1=[]
i=0
count=0
while i<len(a):
    if a[i] not in list1:
        list1.append(a[i])
        count=count+1
    i=i+1
print(count)
print(list1)