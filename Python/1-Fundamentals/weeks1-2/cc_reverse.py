def reverse(txt):
    '''
        I changed the parameter since str is a built-in command!
    '''
    return txt[::-1]


name = input("What is your name? ")
print("Your name reversed is:", reverse(name))
