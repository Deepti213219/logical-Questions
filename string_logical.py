name="reena"
string2=" "
# string=0
# a=len(name)-1
i=0
while i<len(name):
    if name[i] not in string2:
        string2=string2 + name[i]
    i=i+1
print(string2)
