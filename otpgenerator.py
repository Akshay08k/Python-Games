import random
otp = (random.randint(1000,9999))
print(otp)
validotp = int(input("Enter Otp that you received"))
if(otp == validotp):
    print("Congratulations Your Otp validation is successful")
else:
    print("Wrong OTP try again")