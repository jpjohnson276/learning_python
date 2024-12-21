#Creating a list - use []

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)

# Accessing elements in a list '[0]' represents the first index
print(bicycles[0])
# -1 represents the last number of the list
print(bicycles[-1])
#Using title case for list element
print(bicycles[1].title())
# Using F string for list element
print(f"{bicycles[0]} is the bike of choice today")

#Utilizing for loop to itereate list -

for bicycle in bicycles:
  print(f"{bicycle} is awesome")


# List practice

names = ['phillip', ' michelle', 'vince', 'mariel', 'emelie']

for name in names:
  print(f"Hello {name.title()}!")

cars = ['Tesla', 'Honda', 'Toyota']

for car in cars:
    print(f"I want a {car}. They are awesome!")

# Modifying, Adding and Removing Elements

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#changing lists - select index/position then name it
motorcycles[0] = 'ducati'
print(motorcycles)

#adding to list
motorcycles.append('Toyota')
print(motorcycles)

# creating empty list then appending to empty list

fruits = []
fruits.append('apple')
fruits.append('oranges')
fruits.append('banana')

print(fruits)

# inserting elements in a list

fruits.insert(2, 'cherry')

print(fruits)

# Using del will delete an item from the list. Be sure to include index number as well
del fruits[0]
print(fruits)

# Pop method removes the last index from the list
last_item_from_list = motorcycles.pop()
print(f"The last motorcycle I owned was {last_item_from_list}")

print(motorcycles)
print(motorcycles.pop(0))

 Try it yourself

dinner_guests = ['Obama', 'Oprah', 'Beyonce']

print(f"Congratulations {dinner_guests[0]}, you have been selected to join us for dinner")
print(f"Congratulations {dinner_guests[1]}, you have been selected to join us for dinner")
print(f"Congratulations {dinner_guests[2]}, you have been selected to join us for dinner")

guest_removed = dinner_guests.pop()
print(f"{guest_removed} won't be able to attend the dinner. Lets invite another guest")

dinner_guests.append('Alex')
print(f"Congratulations {dinner_guests[0]}, you have been selected to join us for dinner")
print(f"Congratulations {dinner_guests[1]}, you have been selected to join us for dinner")
print(f"Congratulations {dinner_guests[2]}, you have been selected to join us for dinner")

# New Guests

dinner_guests.insert(0, 'Michelle')
dinner_guests.insert(1, 'Vince')
dinner_guests.append('Mariel')

print(dinner_guests)

dinner_guests.pop()
dinner_guests.pop()
dinner_guests.pop()
dinner_guests.pop()

print(dinner_guests)

print(f"Congratulations to {dinner_guests[0]} and {dinner_guests[1]} for coming to the dinner")

del dinner_guests[0]
# repeating this because the last name will become index 0
del dinner_guests[0]
print(dinner_guests)

# Sorting a list Permanently with the sort() Method - sort() changes list permanently
cars = ['bmw', 'audi', 'toyota', 'subaru']
# Sorting lists alphabetically
cars.sort()
print(cars)

# Sorting list reverse - alphabetically, add reverse argument into .sort()
cars.sort(reverse=True)
print(cars)

# Sorting list temporarily with sorted() function

sports = ['soccer', 'basketball', 'football', 'cricket', 'kickball']

print("Here is the original list:")
print(sports)

print("\n Here is the sorted list:")
print(sorted(sports))

print("Here is the original list again:")
print(sports)

# Using reverse in list

cookies = ['choclate chip', 'oatmeal raisin', 'peanut butter']

cookies.reverse()
print(cookies)
cookies.reverse()
print(cookies)

#length of cookies
print(len(cookies))

#5 places I would like to travel to
places_to_visit = ['Bali', 'Austin', 'Tokyo', 'Signapore', 'Austrailia']
# Sorts alphabetical order without changing the the orginial order
sorted(places_to_visit)
# printing to console to confirm things are still the same
print(places_to_visit)

# Reverses sorted list 'Z to A'
sorted(places_to_visit, reverse=True)

places_to_visit.reverse()
print(places_to_visit)

places_to_visit.sort()
print(places_to_visit)

places_to_visit.sort(reverse=True)
print(places_to_visit)

friends = ['Morgan', 'Michelle', 'Vince', 'Mickey']

print(f"There are {len(friends)} friends invited to dinner")

# index errors

print(friends[-1])