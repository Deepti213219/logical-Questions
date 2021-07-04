# Q33.Python: Print a dictionary line by line
# students = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# Sample Output:
# Aex                                                                                                           
# class : V                                                                                                     
# rolld_id : 2                                                                                                  
# Puja                                                                                                          
# class : V                                                                                                     
# roll_id : 3 

students = {'Aex':{'class':'V','rolld_id':2},
        'Puja':{'class':'V','roll_id':3}}
i=0
for x in students:
    for y in x:
        print(students[x][i])