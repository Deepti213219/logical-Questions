# Q19.What is the output of the following code snippet?
# output:-3 3

def func(x = 1, y = 2):
    x = x + y
    y += 1
    print(x, y)
func(y = 2, x = 1)
