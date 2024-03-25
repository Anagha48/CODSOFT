import string
import random
pswd_length = int(input("Enter length of your password: "))

print("Choose character set that need your password  : \n1. Letters\n2. Digits\n3. Special symbols\n4. Exit")

selectedchar = ""

while(True):
	choice = int(input("enter your choice: "))
	if choice == 1:
		selectedchar += string.ascii_letters
	elif choice == 2:
		selectedchar += string.digits
	elif choice == 3:
		selectedchar += string.punctuation
	elif choice == 4:
		break
	else:
		print("invalid choice..\nPlease select a valid option....")

password = []

for i in range(pswd_length):
	randomcharacters = random.choice(selectedchar)
	password.append(randomcharacters)

# printing password as a string
print("your password is " + "".join(password))



