dic={"a":[1,2,3],"b":[4,6,7]}
count=0
for x in dic:
    i=0
    while i<len(dic[x]):
        count=count+1
        i=i+1
print(count)