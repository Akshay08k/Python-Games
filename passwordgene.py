import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"
spe_character = "!@#$%^&*()"
all = upper + lower + numbers + spe_character
password = ""
length = int(input("Enter The Length Of password : "))
for index in range(length):
    password = password + random.choice(all)
print("Password generated: {}".format(password))
