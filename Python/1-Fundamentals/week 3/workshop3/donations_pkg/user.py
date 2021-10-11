def login(database, username, password):
    '''
        Retrieve login information as well
        as database (dictionary) that will be used
    '''

    if username in database and password == database[username]:
        print("Welcome!", username)
        return username
    elif username in database and password != database[username]:
        print("Incorrect password please try again: ")
        return ""
    else:
        print("User not not found. Please register.")
        return ""


def register(database, username):
    '''
        Log user and Database
    '''

    if username in database:
        print("Username already registered.")
        return ""
    else:
        print("User", username, "has been registered")
        return username
