users = [
    ( 0 , "Bob", "passowrd"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longpassword"),
    (3,"username","1234"),
]
#Logging process
username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
username_password = input("Enter your password: ")

_,username,password = username_mapping[username_input]

if username_password == password:
    print("The access is successful. The password is correct.")
else:
    print("The password is wrong. Please try again later.")