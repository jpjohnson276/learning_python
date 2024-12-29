# Rental car
rental_car = input("What kind of rental car would you like?\n")
print(f"Let me see if I can find you a {rental_car}")

# Restaurant Seating
guests = int(input("How many guests will be joining you for dinner?\n"))
if guests > 8:
  print("The wait time will be 20 - 30 minutes.")
else:
  print("Your table is ready")

# Multiples of 10
number = int(input("What number would you like to check?\n"))
if number % 10 == 0:
  print(f"{number} is multiples of 10")
else:
  print(f"Sorry, {number} is not multiples of 10")

# While Loop

current_number = 1

# will continue to print as long as the condition is true, will stop once the condition is false
while current_number <= 5:
  print(current_number)
  current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program "

message = ""

#Will continue until the message says 'quit'
while message != "quit":
  message = input(prompt).lower()
  # Will display messages that are not 'quit'
  if message != 'quit':
    print(message)

# Using a flag

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program "

active = True
while active:
  message = input(prompt)

  if message == 'quit':
    active = False
  else:
    print(message)


# Using a break to Exit a Loop

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program "

while True:
  city = input(prompt)

  if city == 'quit':
    break
  else:
    print(f"I'd love to go to {city.title()}!")

# Using continue loop

current_number = 0
while current_number < 10:
  current_number += 1
  if current_number % 2 == 0:
    continue # Skip the iteration if current_number % 2, but continue with the next iteration:
  print(current_number)


prompt = "\nWhat type of toppings would like to add to your pizza?:"
prompt += "\n Enter 'quit' to end the program "

message = ""

#Will continue until the message says 'quit'
while message != "quit":
  message = input(prompt).lower()
  print(f"We will add {message}, anything else? ")
  # Will display messages that are not 'quit'
  if message != 'quit':
    print(message)

# Using while loops in dictionaries

# A for loop is effective for looping through a list, but shouldnt modify a list inside a for loop because Python will have trouble
# keeping track of the items in the list


# Moving items from One list to Another

#Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each other until there are no more unconfirmed users.
# Move each verfied user into the list of confirmed users.

while unconfirmed_users:
  current_user = unconfirmed_users.pop()

  print(f"Verifying user: {current_user.title()}")
  confirmed_users.append(current_user)

# Display all confirmed users

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
  print(confirmed_user.title())

# Removing all instances of Specifiic Values from a List

#remove() functions removes a  value from a list

pets = ['dog', 'cat', 'dog', 'fish', 'bird', 'dog', 'goat']

while 'dog' in pets:
  pets.remove('dog')

print(pets)



