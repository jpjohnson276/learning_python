# Variables and Types
# Variables are labes that you can assign to values
# The value of a variable can be changed at any time
# Avoid python keywords and function names as variable name

message = 'Hello Python World!'
print(message)


first_name = 'James'
last_name = 'Johnson'

# This is called an F string. F stands for Format and Python formats the string by replacing the name of any variable in braces with its value.
full_name = f"{first_name} {last_name}"
print(full_name)

#Adding Whitespace to Strings with Tabs or New Lines


print('Python')
# '\t' adds a tab
print('\tPython')
# '\n' adds a new line
print('Python\nJavaScript')

favorite_pizza = 'pepperoni '
print(favorite_pizza)

#integer ** represents power therefore it is 3^2
3 **2

# importing this tells explains the the Zen of Python
import this

# Exercises

# 2.3

# Use a variable to represent a person's name and print a message to that person. The message should be

name = input('What is your name? ')

print(f"Hello {name}, would you like to learn some python today?")

# 2.4

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

full_name = first_name + " " + last_name
print(full_name.lower())
print(full_name.upper())
print(full_name.title())

# 2.5 / 2.6

author = 'Beyonce'
quote = '"I think it’s healthy for a person to be nervous. It means you care—that you work hard and want to give a great performance. You just have to channel that nervous energy into the show."'

print(f"{author} once said, {quote}")

# Stripping White Space

favorite_language = 'python '
favorite_language.rstrip()
print(favorite_language)

# Removing prefixes

nostarch_url = 'https://nostarch.com'
simple_url =nostarch_url.removeprefix('https://')

print(simple_url)

formal_name = 'Mr.Johnson'
print(formal_name.removeprefix('Mr.'))

# Removing suffixes

filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))

# Underscores in numbers

universe_age = 15_000_000

print(universe_age)

#multiple assignment - use this technique most often when intializing a set of numbers

x,y,z = 0,2,4

print(x)
print(y)
print(z)


# Constants
"""
constant is a variable whose value stays the same throughout the life of a program.
Python doesnt have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant
"""

MAX_CONNECTIONS = 5000

print(MAX_CONNECTIONS)

#addition
print(5+3)

#subtraction
print(10 - 2)

#multiply
print(4 * 2)

#Division
print(round(16 / 2))