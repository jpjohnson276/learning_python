# Dictionaries Collection of key-value pairs

alien_0 = {
    'color': 'green',
    'points': 5
    }
#prints the type
print(type(alien_0))
#prints the dictionary itself
print(alien_0)

#Accessing Values in Dictionary
print(alien_0['color'])

#Adding New Key-Values
alien_0['x_position'] = 0
alien_0['y_position'] = 25

#Printing the dictionary
print(alien_0)

#Printing the value of color
print(alien_0['color'])

# Utilizing empty dictionaries

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 25

print(alien_0)

points_accumulation = alien_0['points'] * 100

#Testing to see if I can take an integer value from a dictionary and multiply to an int
print(points_accumulation)

#modifying the key

print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'Yellow'
print(f"The alien color is now {alien_0['color']}.")

# Tracking an alien moving at different speeds

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right
# Determine how faar to move the alien based on its current speed

alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
  x_increment = 1
elif alien_0['speed'] == 'medium':
  x_increment = 2
else:
  # This must be a fast alien
  x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment



print(f"New position is: {alien_0['x_position']} and the speed is {alien_0['speed']}")

# Deleting a key

alien_0 = {'x_position': 0, 'y_positions': 25, 'speed': 'medium','color': 'purple'}

print(alien_0)

# add del then choose the key you want to delete
del alien_0['color']

print(alien_0)

# Dictionary of Similar Objects

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

language = favorite_languages['sarah'].title() # .title() will print a capital S i.e Sarah
print(f"Sarah's favorite language is {language}")

# Using get() to Access Values

# Receiving an error becuase points is not listed in the dictionary
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])


# get() method requires a key as a first argument. As a second option argument, you can pass the value to be returned if the key doesn't exist
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)



person = {
    'first_name' : 'Alex',
    'last_name' : 'Brown',
    'age' : 35,
    'city' : 'White Plains'

}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])


friends = {
    'Michelle': 2,
    'Vince': 77,
    'Gerry': 23
}

print(friends['Michelle'])
print(friends['Vince'])
print(friends['Gerry'])

# Glossary

programming_languages = {
    'python': 'Python is a popular programming language.Python can be used on a server to create web applications.',
    'sql' : 'SQL is a standard language for storing, manipulating and retrieving data in databases. Our SQL tutorial will teach you how to use SQL in: MySQL, SQL Server, MS Access, Oracle, Sybase, Informix, Postgres, and other database systems',
    'javascript': "JavaScript is the world's most popular programming language."
}

print(programming_languages['python'])

# Looping through a dictionary

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
  print(f"\nKey: {key}")
  print(f"Value: {value}")

for name, language in favorite_languages.items():
  print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping through dicitionay
for name, language in favorite_languages.items():
  print(f"{name.title()}'s favorite language is {language.title()}.")

for key in programming_languages.keys():
  print(key)

# Creating list

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
  # Printing each key
  print(f"Hi {name.title()}.")


# Checks to see name (key) is in the list of friends
  if name in friends:
    language = favorite_languages[name].title()
    #prints names and their languages
    print(f"\t{name.title()}, I see you love {language}!\n")


if 'erin' not in favorite_languages.keys():
  print("Please take your poll Erin")

#looping through dictionary keys in a particular order


# keep in mind sorted is a function
for name in sorted(favorite_languages.keys()):
  print(f"{name.title()}, thank you for taking the poll.\n")


# Looping through values only

print("The following languages have been mentioned:")

for language in favorite_languages.values():
  print(language.title())

# Using set - identifies the unique items in the collection and builds a set from those items
for language in set(favorite_languages.values()):
  print(language.title())

# Sets are able to be built with just single value curly braces (no need for key)
languages = {'python', 'rust', 'python', 'c'}
print(languages)

data_tools = {
    'database': 'postgres',
    'scripting': 'python',
    'cloud': 'aws'

}

for key, value in data_tools.items():
  print(f"For {key.title()}, we will use {value.title()}")

rivers = {
    'nile': 'egypt',
    'mississippi': 'usa',
    'amazon': 'brazil',
    'lena': 'river'

}

# printing keys
for key in rivers.keys():
  print(key)

#printing values
for value in rivers.values():
  print(value)

for k,v in rivers.items():
  print(f"The {k.title()} river is located in {v.title()}")

if 'phil' not in favorite_languages.keys():
  print("Please take pool")
else:
  print("Thank you for taking it")

# Nesting

alien_0 = {'color': 'green','points': 5}
alien_1 = {'color': 'yellow','points': 10}
alien_2 = {'color': 'red','points': 15}

aliens = [alien_0, alien_1, alien_2]

# loops through the list of aliens - alien's list contains three dictionaries
for alien in aliens:
  print(alien)

#Making an empty list for storing aliens

aliens = []

#Making 30 green aliens

for alien_number in range(30):
  new_alien = {'color':'green', 'points': 5, 'speed': 'slow'}
  aliens.append(new_alien)

#show the first 5 aliens
for alien in aliens[:5]:
  print(alien)

print("...")

#Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

#Making an empty list for storing aliens

aliens = []

#Making 30 green aliens

for alien_number in range(30):
  new_alien = {'color':'green', 'points': 5, 'speed': 'slow'}
  aliens.append(new_alien)

#show the first 5 aliens
for alien in aliens[:5]:
  print(alien)

print("...")

#Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

#Making an empty list for storing aliens
#Changing the first 3 to yellow with a for loop

#Selecting the first 3
for alien in aliens[:3]:
  # if the color is green then:
  if alien['color'] == 'green':
    # change to this
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10

print(aliens)

# A list in a dictionary

# Store information about a pizza being ordered.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(pizza)

print(f"You have ordered a pizza with {pizza['crust']}-crust pizza with the following toppings:")

# to access list of items, include the key that holds the list
for topping in pizza['toppings']:
  # \t is for tab
  print(f"\t{topping}")

favorite_languages_v2 = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages_v2.items():
  print(f"\n{name.title()}'s favorite language are:")
  for language in languages:
    print(f"\t{language.title()}")


# A Dictionary in a Dictionary

users = {
    'aeinstein' : {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
  print(f"\nUsername: {username}")
  full_name = f"{user_info['first']} {user_info['last']}"
  location = user_info['location']

  print(f"\tFull name: {full_name.title()}")
  print(f"\tLocation: {location.title()}")

person_1 = {
    'name': 'michelle',
    'age': 32,
    'neighborhood': 'bushwick'
}


person_2 = {
    'name': 'vince',
    'age': 32,
    'neighborhood': 'sunnyside'
}

person_3 = {
    'name': 'jose',
    'age': 34,
    'neighborhood': 'jersey city'
}

person_4 = {
    'name': 'gerry',
    'age': 41,
    'neighborhood': 'greenpoint'
}

people = [person_1, person_2, person_3, person_4]

for person in people:
  print(person)

chance = {
    'owner': 'Phillip',
    'type': 'cat'
}


zoe = {
    'owner': 'gerry',
    'type': 'dog'
}

snoopy = {
    'owner': 'moises',
    'type': 'dog'
}

pets = [chance, zoe, snoopy]

for pet in pets:
  print(pet)


about_me = {
    'name': 'phillip',
    'places_lived': ['gaithersburg', 'hagerstown', 'frederick', 'germantown', 'brooklyn', 'manhattan', 'the bronx']
}

about_me['places_lived'].append('sunny side')

print(about_me)



