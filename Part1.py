print('Hello World')

# ------------------------------------- #
##  playing with string and variables  ##
# ------------------------------------- #

print('-------------------------------')

# variables
person_name = 'Mr. Jack'

object1 = 'car'
object1_color = 'red'

object2 = 'house'
object2_age = '20 years'

# add variables to print statements

print('Hello ' + person_name ) # mind the spaceing
print(f'I am very interested in your {object1}, is it {object1_color}?')
print('Also, ' + person_name + ' is your ' + object2 + ' older than ' + object2_age + '?') # mind spacing
print('Thank you, ' + person_name )


# ------------------------------------- #
##     playing with Boolean values     ##
# ------------------------------------- #

print('-------------------------------')

having_a_house = True

if having_a_house:
    print('I own a small house')

print('-------------------------------')


# ------------------------------------- #
##         String Manipulation         ##
# ------------------------------------- #

sentence = 'It is Taco Time yet?'

# make every character uppercase
print('This is all uppercase:', sentence.upper())

# make every character lowercase
print('This is all lowercase:', sentence.lower())

# verify that all characters are lowercase
print('Are all the characters in "sentence", lowercase?:', sentence.islower())

# chain the commands to make a true case for lowercase
print('With chaining, are all the characters in "sentence", lowercase?:', sentence.lower().islower())

# what is the length of 'sentence'?
print('How many characters are in "sentence"?:', len(sentence))

# replace a word in "sentence"
# replace('word_to_take_out', 'word_to_step_in)
print('Using replace here:', sentence.replace('yet?', 'Now!')) # string must be EXACT

# get the index of a character
# only gets the first instance
print('What is the index for character "t":', sentence.index('t'))

# get the index of a word
print('What is the index for "yet?"?:', sentence.index('yet?'))

# split up the text
print('Using the "\ n" here \n makes a line break' )

print('-------------------------------')


# ------------------------------------- #
##    Different Number Manipulation    ##
# ------------------------------------- #

# arithmetic for python - * grabs everything from library
from math import *

print('What is 10 + 10?:', 10 + 10)

print('What is 10 + 10, times 3?:', (10 + 10)*3)

print('What is 10 + 10, times 3, then divided by 45?:', ((10 + 10)*3)/45)

print('What is 10 + 10, times 3, then divided by 45, minus 32?:', (((10 + 10)*3)/45)-32)

# print an integer, not a string
print(505)

# manipulate numbers as variables
age = 25

print('Hello, my age is', age)

print('Hello, my age is', age+2)
print('-------------------------------')


# ------------------------------------- #
##      Functions with Numbers         ##
# ------------------------------------- #

# dataset of numbers
print(1,5,6,2,9,4,-30)

# which number is the highest?
print(max(1,5,6,2,9,4,-30), 'is the largest number')

# which is the smallest number?
print(min(1,5,6,2,9,4,-30), 'is the smallest number')

# calculating powers
print('5 to the second power is:', pow(5,2)) # pow(base,power)

# round down the number
print('5 to the second power, rounded is:', round(pow(5,2))) # pow(base,power)

# get the absolute value
print('The absolute value of -505 is:', abs(-505))

# get the square root 
print('The square root of 505 is:', sqrt(505))
print('-------------------------------')


# ------------------------------------- #
##      Advanced Math Functions        ##
# ------------------------------------- #

# smallest integral value, bigger than the number
print('The smallest integral value, bigger than the number, 23.999999 is', ceil(23.999999))

# largest integral value, bigger than the number
print('The largest integral value, bigger than the number, 23.999999', floor(23.999999))

# factorials
print('The factorial of 5 is:', factorial(5))
print('-------------------------------')


# ------------------------------------- #
##    Understanding input function     ##
# ------------------------------------- #

age = input('What is your age?')
print('My age is:', age)

name = input('What is your name?')
age = input('What is your age?')
food = input('What would like to eat?')
beverage = input('What would like to drink?')

print(f'Hello, my name is {name}, I am {age} years old.' +
f'I would like to eat {food} with a {beverage}.')
print('-------------------------------')


# ------------------------------------- #
##          Pratice Part 1              ##
# ------------------------------------- #

# create a app for the product we would like to buy
# need to calculate price and quantity

price_1 = input('What is the price for product One? ')
quantity_1 = input('How many of product One, would you like?' )

price_2 = input('What is the price for product Two? ')
quantity_2 = input('How many of product Two, would you like? ')

price_3 = input('What is the price for product Three? ')
quantity_3 = input('How many of product Three, would you like? ')

# results from above - Need to cast as numbers - 'input' makes them strings
result_1 = float(price_1) * int(quantity_1)
result_2 = float(price_2) * int(quantity_2)
result_3 = float(price_3) * int(quantity_3)

# show results
print(result_1)
print(result_2)
print(result_3)

# get the total
sum = result_1 + result_2 + result_3
print('The total price, before tax and shipping is:', sum)
print('-------------------------------')


# ------------------------------------- #
##         Pratice Part 2              ##
# ------------------------------------- #

# friends dividing the amount owed for pizza by amount consumed

# people
name_1 = input('Person sitting in chair One, what is your name? ')
name_2 = input('Person sitting in chair Two, what is your name? ')
name_3 = input('Person sitting in chair Three, what is your name? ')

# pizza info
slices_total = input('Everyone, how many slices did the pizza have? ')
pizza_price = input('Everyone, how much did the pizza cost? ')

# amounts consumed
name_1_ate = input(f'{name_1}, How many slices of pizza did you eat? ')
name_2_ate = input(f'{name_2}, How many slices of pizza did you eat? ')
name_3_ate = input(f'{name_3}, How many slices of pizza did you eat? ')

# percents ---> consumed/total slices
name_1_percent = float(name_1_ate) / float(slices_total)
name_2_percent = float(name_2_ate) / float(slices_total)
name_3_percent = float(name_3_ate) / float(slices_total)

# amount to pay ---> percent * pizza price
name_1_pay = name_1_percent * float(pizza_price)
name_2_pay = name_2_percent * float(pizza_price)
name_3_pay = name_3_percent * float(pizza_price)

print('The total bill is $', round(name_1_pay + name_2_pay + name_3_pay))
print(f'{name_1}, you owe $', round(name_1_pay))
print(f'{name_2}, you owe $', round(name_2_pay))
print(f'{name_3}, you owe $', round(name_3_pay))
