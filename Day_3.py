# Day 3

# using for loop to loop through list

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  print(magician)

for magician in magicians:
  print(f"{magician.title()} did an amazing job!")
  print(f"I can't wait to see your next trick {magician.title()}. \n")

print(f"Thank you for attending the show")

pizzas = ['pepperoni', 'bacon', 'cheese']

for pizza in pizzas:
  print(f"I really love {pizza} pizza!")

print('I really enjoy pizza')

animals = ['tiger', 'dog', 'owl']

for animal in animals:
  print(f"I love {animal}")

# Using range

# prints numbers between 1 and 5
for value in range(1, 5):
  print(value)

# Will print from 0 up to until the number inside the range function
for num in range(7):
  print(num)

# Creating a list of numbers using list function
numbers = list(range(0,5))

print(numbers)

# using range to skip numbers by using the 3rd argument

even_numbers = list(range(2, 20, 2))
print(even_numbers)

# square root

squares = []

for value in range(1,11):
  squares.append(value ** 2)

print(squares)

# Basic statistics

digits = [1,2,3,4,5,6,7,8,9,0]

print(f"The minimum is {min(digits)}")
print(f"The maximum is {max(digits)}")
print(f"The sum is {sum(digits)}")

# List comprehensions

squares = [value ** 2 for value in range(1, 11)]
print(squares)

# Try it yourself

for num in range(1,21):
  print(num)

numbers = list(range(1, 1_000_001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

number_by_threes = []

for value in range(3, 30):
 digits = value * 3
 number_by_threes.append(digits)

print(number_by_threes)


# cube comprehension
cubes = [value ** 3 for value in range(1, 10)]
print(cubes)

# Working with part of a list
#Slicing from index 0 to 2

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

#Slicing from index 1 to 4
print(players[1:4])

# Slicing from index 1 to end
print(players[1:])

#Slicing from start up to index 3
print(players[:4])

# prints last 3 of the index

print(players[-3:])


#Looping through a slice

print("Here are the first three players of the game:")
for player in players[:3]:
  print(player.title())


# Copying list

favorite_foods = ['pizza', 'falafel', 'sushi']

friends_favorite_foods = favorite_foods[:]

print('My favorite foods are: ')
print(favorite_foods)

print("My friend's favorite foods are: ")
print(friends_favorite_foods)


favorite_foods.append('dumplings')
friends_favorite_foods.append('ice cream')

# Using [:] creates a copy of the list. Doesn't make changes to the original list you copy from

print(favorite_foods)
print(friends_favorite_foods)

# Slice practice with fruits

my_fruits = ['banana', 'strawberry', 'cherry', 'blueberry', 'apple', 'watermelon']
print("Here are the first three fruits:")

#Slicing first three
for fruit in my_fruits[:3]:
  print(fruit)

print("Here are the middle fruits: ")
for fruit in my_fruits[2:4]:
    print(fruit)

print("Here are the last 3 fruits: ")
for fruit in my_fruits[-3:]:
    print(fruit)

# copying list practice

print(pizzas)

friends_pizza = pizzas[:]
print(friends_pizza)

pizzas.append('sausage')
friends_pizza.append('jalapeno')

print(pizzas)
print(friends_pizza)

# Tuple - similar to lists but are immutable (cannot be changed)

buffet = ('steak', 'chicken', 'veggies')

#accessing an idex
print(f" Buffet item 1: {buffet[0]}")

# looping through

for food in buffet:
  print(food)
