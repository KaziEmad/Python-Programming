#variable for the input
user = input("Enter your name: ")

#printing the input in format 1
print("Hello " + user + "!")

#printing the input in format 2
print("Hello, %s!" % user)

#printing the input in format 3
print("Hello {}!".format(user))

#printing the input in format 4
print(f"Hello {user}!")