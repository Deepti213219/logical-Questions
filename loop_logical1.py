num=int(input("enter any no. ="))
i=0
while i<num:
    num1=int(input('enter any n0.='))
    j=0
    sum=0
    while j<num1:
        if num1//10 and num1%10:
            sum=sum+num1
        j+=1
    i=i+1
    print(sum)