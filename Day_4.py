# Looping & using if/else condition


cars = ['audi', 'bmw', 'subaru', 'toyota']

print(f"You have {len(cars)} cars")

for car in cars:
  if car == 'bmw':
    print(car.upper())
  else:
    print(car.title())

# Checking for inequality

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
  print('Hold the anchovies!')
else:
  print('I have anchovies for you!')

# Checking multiple conditions
# Using and keyword

age_0 = 18
age_1 = 22

age_0 >= 21 and age_1 >= 21

# Both variables need to meet the expression in order to return True otherwise it will return False

# Checking multiple conditions
# Using and keyword

age_0 = 18
age_1 = 22

age_0 >= 21 or age_1 >= 21

# Either or both variables need to meet the expression in order to return True otherwise it will return False

#Check  whether a value in list

requested_toppings = ['pepperoni', 'sausage', 'bacon', 'cheese', 'jalapeno']

#Returns false because mushroom is not in the list. Also, note how a string can be written out without assigning it to a variable
'mushroom' in requested_toppings

# Check Whether a Value is Not in List

banned_users = ['andrew', 'carolina', 'david']

user = 'maggie'

# not in can be used in if/else
if user not in banned_users:
  print(f"Congratulations {user.title()}, you are not on the banned list")

car = 'subaru'

print("Is car == 'subarau' ? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi' I predict False.")
print(car == 'audi')

names = ['Phillip', 'Valerie', 'TJ']

'Neisha' in names

# Simple if Statements

# if conditional_statement:
#  do something

age  = 17
if age >= 18:
  print("You are old enough to vote!")
  print("Have you registered to vote!")
else:
  print("Sorry you are too young to vote")
  print("Please register to vote as you turn 18!")


# if else chain

age = 12

if age < 4:
  price = 0
elif age < 18:
  price = 25
else:
  price = 40

print(f"Your admission price is ${price}.")

# Omitting the else block

age = 12

if age < 4:
  price = 0
elif age < 18:
  price = 25
elif age < 65:
  price = 40
elif age >= 65:
  price = 20

print(f"Your admission price is ${price}")


# Testing multiple conditions

requested_toppings = ['mushrooms', 'extra cheese']



if 'mushrooms' in requested_toppings:
  print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
  print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
  print("Adding extra cheese.")

print("\nFinished making your pizza")

alien_color = input('What color would you like to choose? Green, Yellow, or Red ').lower()

if alien_color == 'green':
  score = 5
elif alien_color == 'yellow':
  score = 10
elif alien_color == 'red':
  score = 15

print(f"Congratulations Player. You have earned {score} points")

#Stages of life

import random

age = random.randint(1, 101)

if age >= 65:
  print(f"This person's age is {age}, is an elder")
elif age < 65 and age >= 20:
  print(f"This person's age is {age}, an adult")
elif age < 20 and age >= 13:
  print(f"This person's age is {age}, is a teenager")
elif age < 13 and age >= 4:
  print(f"This person's age is {age}, is a kid")
else:
  print(f"This person's age is {age},is a baby")


# Favorite Fruit

fruits = ['banana', 'blueberries']

if 'blueberries' in fruits:
  print("You really like Blueberries")

if 'banana' in fruits:
  print("You really like bananas")

if 'cherry' in fruits:
  print("You really like cherries")

if 'watermelon' in fruits:
  print("You really like watermelon")


# Using if statements with lists

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
  print(f"Adding {requested_topping}.")


print(f"\nFinished making your pizza!")

# Using if statements with If-else statement

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
  if requested_topping == 'green peppers':
    print("Sorry we are out of green peppers!")
  else:
    print(f"Adding {requested_topping}.")


print(f"\nFinished making your pizza!")

# Checking the list is not empty

requested_toppings = []

if requested_toppings:
  print("Sure I will have the pizza ready for you")
else:
  print("Are you sure you want a plain pizza")


# Using multiple lists

avaible_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
  if requested_topping in avaible_toppings:
    print(f"Adding {requested_topping}.")
  else:
    print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza")

user_names = ['jjohns87', 'jpjohnson36844', 'pjdesigns', 'admin', '423jpjohnson', 'mike888']

for user_name in user_names:
  if user_name == 'admin':
    print(f"Hello, {user_name} would you like to see a status report")
  else:
    print(f"Hello, {user_name} thank you for logging in again")


user_names = []

if user_names:
  print("There are user names")
else:
  print("We need to add user names to the list")


current_users = ['jjohns87', 'jpjohnson36844', 'pjdesigns', 'admin', '423jpjohnson', 'mike888']

new_users = ['jjohns87', 'jpjohnson36844', 'jpj2127', 'jp2127', 'eric']

for new_user in new_users:
  if new_user in current_users:
    print("Username is not available, Please try again!")
  else:
    print("Username is available")

numbers = list(range(1,10))

for number in numbers:
  if number == 1:
    print(f"{number}st")
  elif number == 2:
    print(f"{number}nd")
  elif number == 3:
    print(f"{number}rd")
  else:
    print(f"{number}th")

