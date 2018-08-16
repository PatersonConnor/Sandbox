"""Connor Paterson"""
MIN_LENGTH = 3
userpass = len(input("please enter a password:"))
while userpass < MIN_LENGTH:
    print("A password must contain at least 3 characters.")
    userpass = len(input("please enter a password:"))
print("*" * userpass)

