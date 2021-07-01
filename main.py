import random


def shuffle(string):
	templist = list(string)
	random.shuffle(templist)
	return ''.join(templist)


uppercaseLetter = chr(random.randint(65, 90))  # Add Random uppercase letter
uppercaseLetter2 = chr(random.randint(65, 90))  # Add Random second uppercase letter
lowercaseLetter = chr(random.randint(97, 122))  # Add Random lowercase letter
lowercaseLetter2 = chr(random.randint(97, 122))  # Add Random second lowercase letter
number = chr(random.randint(48, 57))  # Add random number
number2 = chr(random.randint(48, 57))  # Add second random number
# Later add random punctuation
# ?=63 @=64 !=33 #=35 $=36 %=37 &=38

# Generate Random Password
password = uppercaseLetter + uppercaseLetter2 + lowercaseLetter + lowercaseLetter2 + number + number2
password = shuffle(password)

print(password)
