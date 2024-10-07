def min_value(list):
    
    min = list[0]
    for i in list:
       
        if i < min:
            min = i
    return min

num = [12, 65, 54, 39, 102, 37, 72, 33, 5, -28, 0, 15]
print(min_value(num))
