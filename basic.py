# First Python Programming First expression
print("I am Ahsan Ul Haq")
# Print 15 Aesteries evaluation of expression
print('*' * 15)

# Data Type
price  = 10
quantity = 4.5
print(type(price))
print(type(quantity))

#Print statment by talking user input
name = input("What is your name:")
age = input("What is your age:")
print("The student enrolled first is :" + name + " with age " + age)

# Type Conversion
birthyear = input("What is your birth year: ")
year = 2022 - int(birthyear)
print("Total Age in year is :" + str(year))

# String
welcomemessage = "Hello Python"
print(welcomemessage[0])   # Print H
print(welcomemessage[0:5]) # Print Hello
print(welcomemessage[-1]) # Print n from right

#Formatted String
firstname = 'AHSAN'
lastname = 'UL HAQ'
msg = f'{firstname} {lastname} is a begineer python programmer'
print(msg)

