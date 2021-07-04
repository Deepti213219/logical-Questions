student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
count=0
j=0
while j<len(student):
    # print(student[i])
    for x in student[j]:
        count=count+1        
    j=j+1
print(count)

# output:-9