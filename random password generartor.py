
import string
import random

characters=list(string.ascii_letters+string.digits+"!@#$%^&*()")

def generate_password():
    password_length=int(input("How long would you like your password to be?"))

    random.shuffle(characters)

    password=[]

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password="".join(password)

    print(password)

option=input("Do youwant generate a password?(yes/no):")

if option=="yes":
    generate_password()
elif option=="no":
    print("program ended")
    quit()
else:
    print("Invalid input,please input yes or no")
    quit()
            