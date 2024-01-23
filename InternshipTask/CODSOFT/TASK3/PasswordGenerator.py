import random
import string

def GeneratePassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def PasswordGenerator():
    print("------------Password Generator----------------")

    #usinf error handling
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Please Enter a positive length")
            return

    except ValueError:
        print("Invalit input.Pleae enter a valid number")
        return

    password = GeneratePassword(length)  
    print(f"Generated Password: {password}")


PasswordGenerator()    