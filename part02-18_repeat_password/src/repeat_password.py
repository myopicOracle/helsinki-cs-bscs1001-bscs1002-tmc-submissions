# Write your solution here

password = input("Password: ")

while True: 
    verify = input("Repeat password: ")
    if password == verify:
        print("User account created!")
        break
    else: 
        print("They do not match!")