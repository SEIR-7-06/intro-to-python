####################################################
# VARIABLES

shop_name = 'Tribute Pizza'
total_pizzas = 12.0
store_is_open = True
store_is_open = False
pizzas_by_the_slice = ['cheese', 'supreme', 'pepperoni']
order = {
  'name': 'Chris',
  'price': 15.5
}

# print(shop_name)
# print(total_pizzas)
# print(store_is_open)

# print(type(shop_name))
# print(type(total_pizzas))
# print(type(pizzas_by_the_slice))
# print(type(order))

####################################################
# COMPARISON OPERATORS

# print(shop_name != 'Maria\'s Pizzas')

# > < <= >= == !=
# print(total_pizzas < 10)

# # + - * / %
# print(total_pizzas * 3)
# print(total_pizzas // 2)
# print(6.0 == 6)

####################################################
# STRINGS
person_name = 'Philip'
last_name = 'Smith'
dogs_name = 'Spot'

greeting = f'Hello, my name is {person_name} {last_name}'

# print(greeting)

new_greeting = greeting + f'and my dog\'s name is {dogs_name}'
# print(new_greeting)

#####################################################
# BOOLEANS

it_is_monday = False
it_is_tuesday = False
it_is_cloudy = True

# JavaScript - && ||
# Python - and or not
# print(not it_is_monday)
# print(not it_is_tuesday and it_is_cloudy)
# print(it_is_monday or it_is_tuesday)

# JavaScript - 0, undefined, null, '', NaN, false
# Python - 0, 0.0, '', None, [], {}, False

# print('Monday' or 'Tuesday')
# print('Monday' and '')

# it_is_tuesday and print('Ordering Pizza Dough')

#####################################################
# CONDITIONAL LOGIC

"""
in JavaScript
if (pet === 'dog) {
  console.log('You will need to train your pet')
} else if (pet === 'cat') {

} else {

}
"""

# pet = 'dog'
# age = 3

# if pet == 'dog':
#   print('You will need to train your pet')
# elif age == 3:
#   print('You won\'t need to train your pet too much')
# else:
#   print('We don\'t have that pet in our records')

# pet == 'dog' and print('You will need to train your pet')

#####################################################
# LOOPS

# count = 0

# while count < 5:
#   print(count, 'is less than 5')
#   count += 1

# count = 15

# for number in range(1, count + 1):
#   if number % 2 == 0:
#     print(number)
# else:
#   print('done')

"""
JavaScript

function getGreeting(personName) {
  return `Hello, my name is ${personName}`;
}
"""

def get_greeting(person_name):
  return f'Hello, nice to meet you. My name is {person_name}'

greeting = get_greeting('Michael')

# print(greeting)

"""
Write a function that will count from 1-99 printing 1 of four things for each number. If the number is divisible by 3, print "fizz". If the number is divisible by 5, print "buzz". If the number is divisible by 3 and 5, print "fizzbuzz". And otherwise, just print the number.
"""

def fizzbuzz(last_number):
  for i in range(1, last_number + 1):
    if i % 3 == 0 and i % 5 == 0:
      print('fizzbuzz')
    elif i % 3 == 0:
      print('fizz')
    elif i % 5 == 0:
      print('buzz')
    else:
      print(i)

# fizzbuzz(10)

####################################################################
# LIST (SIMILAR TO AN ARRAY IN JAVASCRIPT)
secret_files = ['a top secret', 'another top secret']
# JavaScript - secretFile.length
files_length = len(secret_files)

# print(files_length)

# for file in secret_files:
#   print(file)

capulets = ['Greg', 'Maria', 'Clyde', 'Suzy']
montagues = ['Sally', 'Frank', 'Ana', 'Tim']

happy_family = capulets + montagues

# print(happy_family)

happy_family.append('Hubert')
happy_family.extend(['Jaime', 'Kelly'])

# print(happy_family)

# for family_member in happy_family:
#   print(family_member)

###########################################
# DICTIONARIES
student = {
  'student_name': 'Sally',
  'course': 'SEI',
  'current_week': 6,
  'date_of_birth': 'May 6 1986'
}

name = student['student_name']

student['backpack_color'] = 'blue'

# date_of_birth = student['date_of_birth']
date_of_birth = student.get('date_of_birth')

# print(date_of_birth)

fav_color = input('What is your favorite color?\n')

# print(fav_color)