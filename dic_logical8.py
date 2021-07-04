# Q32.Write a Python program to get the key, value and item in a dictionary.
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# Sample Output:
# key  value  count                                                                                             
# 1     10      1                                                                                               
# 2     20      2                                                                                               
# 3     30      3                                                                                               
# 4     40      4                                                                                               
# 5     50      5                                                                                               
# 6     60      6

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
count=0
for i in dict_num:
    count=count+1
    print(i, end="   ")
    print(dict_num[i],end="   ")
    print(count)

