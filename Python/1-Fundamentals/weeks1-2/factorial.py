def factorial(num):
    '''
       Calculate the product of an integer and all the integers below it 
    '''
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


print(factorial(500))
