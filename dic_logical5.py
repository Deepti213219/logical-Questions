# Q22. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

dic={'1':['a','b'], '2':['c','d']}
for x in dic:
    i=0
    while i<len(dic[x]):
        print(dic[x][i]+dic[x])
        i=i+1
