def max_num(num1,num2,num3):
    if str(num1) == 'bo' :
        return num1
    elif num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num('bo',4,5))