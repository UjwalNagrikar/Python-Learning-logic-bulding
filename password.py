import random 

# pass word genrator 
print("Password Generator")

def password_genrator(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    password = "".join(random.choice(characters) for i in range(length))
    return password
length = int(input("Enter the length of the password: "))
print("Generated password:", password_genrator(length))
