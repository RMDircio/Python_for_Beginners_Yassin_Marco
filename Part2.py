# ------------------------------------- #
##        Utility of Functions         ##
# ------------------------------------- #

# # what do you love function
# def love(name):
#     print(f'I love {name}')

# love('Muffin')

# # write a monologe
# def person_1(name):
#     print(f'{name}: Hello, how can help you?')


# def person_2(food, drink, dessert, name):
#     name = input('What is your name? ')
#     food = input('What would you like to eat? ')
#     drink = input('What would like to drink? ')
#     dessert = input('What would like for dessert? ')
#     print(f'{name}: I would like {food}, and {drink} to drink and for dessert, {dessert}, please')

# def person_1_1(name):
#     print(f'{name}: Yes, of course, thank you.')


# person_1('Cashier')
# person_2('food', 'drink', 'dessert', 'name')
# person_1_1
# print('-------------------------------')


# ------------------------------------- #
##      Use the Return Statement       ##
# ------------------------------------- #

# def calculation(a,b,c):
#     print(a + b + c) # if 'return' is placed here, lines below will not print
#     print(a - b -c)
#     print(a * b * c)

# calculation(2,2,2)
# print('-------------------------------')


# ------------------------------------- #
##    Understanding the IF Statement   ##      
##               Part 1                ##
# ------------------------------------- #

# # boolean values
# hungry = False
# thirsty = True

# # using IF 
# if hungry: # --> 'if hungry is True'
#     print("Let's grab take out!")
# else:
#     print("I'll drink some water.")

# # using IF with AND
# if hungry and thirsty: # --> 'if hungry and thirsty is True'
#     print("You grab take out and I'll get some drinks.")
# else:
#     print('Should we go for a walk?')

# # using IF with OR
# if hungry or thirsty: # --> 'if hungry or thirsty is True'
#     print("You grab take out and I'll get some water for me.")
# else:
#     print('How about a movie?')

# # using TWO IF statements in sequence - needs and else at the end
# if hungry:
#     print('I have homemade soup and bread for you.')
# elif thirsty:
#     print('Would you like red or white wine?')
# else:
#     print("Oh, let's take the dog for a walk then.")

# # flipping statements around
# if not hungry: # --> if hungry is False
#     print('I will come back later')

# print('-------------------------------')


# ------------------------------------- #
##    Understanding the IF Statement   ##
##               Part 2                ##
# ------------------------------------- #

# # compairing numbers
# var_1 = 1
# var_2 = 5
# var_3 = 1

# if var_1 == var_2 != var_3: # if var_1 equals var_2 but does not equal var_3 (
#     print('Yes, they are equal.') # if True
# else:
#     print('No, they are NOT equal.') # if False

# if var_1 > var_2:
#     print('It is greater than.')
# else:
#     print('It is NOT greater than.')

# # comparing strings - mind caps!
# color1 = 'blue'
# color2 = 'red'
# color3 = 'black'
# color4 = 'yellow'

# if color1 == color2:
#     print('Yes, they are the same color')
# else:
#     print('No, they are different colors')

# # who is the richest person

# person1 = input('What is your name? ')
# person1_wallet = input('How much money to you have? ')

# person2 = input('What is your name? ')
# person2_wallet = input('How much money to you have? ')

# person3 = input('What is your name? ')
# person3_wallet = input('How much money to you have? ')

# if float(person1_wallet) > float(person2_wallet) and float(person1_wallet) > float(person3_wallet):
#     print(f'{person_1} is the richest.')

# elif float(person2_wallet) > float(person1_wallet) and float(person2_wallet) > float(person3_wallet):
#     print(f'{person_2} is the richest.')
    
# elif float(person3_wallet) > float(person1_wallet) and float(person3_wallet) > float(person2_wallet):
#     print(f'{person3} is the richest.')

# print('-------------------------------') 


# ------------------------------------- #
##    Understanding the IF Statement   ##
##               Part 3                ##
# ------------------------------------- #

# # converstation between two people

# # rules
# def questions():
#     rules = input("Please answer all questions. Reply with 'yes' or 'no'")
#     if rules != 'yes': # stop
#         return print('Try again.')
#     else:
#         print('Next question:')
#     question1 = input('Are you hungry? ')
#     if question1 != 'yes': # stop
#         return print('Okay, shall we go for a walk?')
#     else:
#         print('Next Question')
#     question2 = input('Would you like to eat at a restaurant? ')
#     if question2 != 'yes':
#         return print('Come eat at my place then.')
#     else:
#         print('Next Question')
#     question3 = input('Should we have tacos? ')
#     if question3 != 'yes':
#         return print('What would you like instead?')
#     else:
#         print("Let's go!")

# questions()

# print('-------------------------------') 


# ------------------------------------- #
##          Working with Lists         ##
# ------------------------------------- #

# foods = ['apples', 'bananas', 'melons', 'strawberries', 'grapes']

# print(foods) # prints all
# print('First element is:', foods[0]) # prints first element
# print(foods[1]) # prints second element
# print(foods[2]) # prints third element

# # change out items
# foods[2] = 'avocados'
# print(foods)

# # selecting certain elements
# print(foods[0:2]) # [inclusive : exclusive]
# print(foods[3:]) # last two elements, leaving empty grabs everything till end

# print('-------------------------------') 


# ------------------------------------- #
##     Using Functions with Lists      ##
# ------------------------------------- #


# food = ['hamburger', 'juice', 'pizza', 'juice', 'fries', 'juice', 'hamburger', 'sushi']
# prices = [5.64, 3.92, 7.29, 4.95, 3.20]

# # put something into the list - add to the list
# food.insert(5, 'cake') # insert(index, object)


# # merge two lists together
# food.extend(prices) # param is list to be added

# # find the index of a certain item
# print('The index of juice is:',food.index('juice')) 

# # count how many times an item is in the list
# print('How many times is juice in the list?:', food.count('juice'))

# # copy a list
# new_food = food.copy() + prices.copy() # new list that is a merge of food and prices twice

# print(food)
# print(new_food)

# # delete everything from the list
# food.clear()

# print('-------------------------------') 


# ------------------------------------- #
##          Difference Between          ##
##           List and Tuples            ##
# ------------------------------------- #

# # lists - can manipulate
# list1 = [1,2,3,4] # brackets
# print(list1)

# # tuple - can NOT manipulate
# tuple1 = (1,2,3,4) # parentheses
# print(tuple1)

# # example
# colors = ('blue', 'yellow', 'red')
# shapes = ('square', 'triangle', 'circle')

# new_tuple = colors + shapes
# print(new_tuple)

# print('-------------------------------')


# ------------------------------------- #
##        What is a Dictionary         ##
##              in Python              ##
# ------------------------------------- #

# # dictionary need curved brackets {}
# # keys need to be unique
# colors = {
#             'B' : 'Blue', # key : value
#             'R' : 'Red',
#             'O' : 'Orange'
# }

# # get the value from the key
# print(colors.get('B', 'Stop')) # .get(what you want, default value if item is not in dictionary)
# print(colors.get('G', 'Nope'))
# print(colors.get('b', 'Nope'))

# # create employee numbers and look them up
# company_empolyees= {
#                     555 : 'Nelson',
#                     146 : 'Okan',
#                     895 : 'Yesgi',
#                     648 : 'Opeian',
#                     721 : 'Hinesh'
# }

# print(company_empolyees.get(202, 'Employee is invalid'))


# print('-------------------------------')


# ------------------------------------- #
##        Introduce the While          ##
##           Loop Structure            ##
# ------------------------------------- #

# var1 = 25
# var2 = 2000

# # while loops need a break out point
# while var1 < var2:
#     print('var1 is:', var1)
#     print('var1 is less than var2')
#     var1 = var1 + 5 # this is a long running break

# print('-------------------------------')


# ------------------------------------- #
##       Understanding For Loops       ##
# ------------------------------------- #

# colors = ['blue', 'red', 'yellow', 'orange', 'black']

# # print out each color septerate
# for each_color in colors:
#     print(each_color)

# # print out each letter in string
# for letter in 'Blue':
#     print(letter)

# # print only certain elements
# for each_color in colors:
#     print(each_color)
#     if each_color == 'orange': # stop at 'orange', inclusive
#         break

# for number in range(6): # exclusive stops at 5
#     print(number)

# for number in range (0,10): # exclusive - stops at 9
#     print(number)

# print('-------------------------------')


# ------------------------------------- #
##   Creating and Blocking Passwords   ##
# ------------------------------------- #

# user_password = 'pass123'
# user_answer = ''
# num_attempts = 0 # counter --> starts at zero
# max_attempts = 3 # number of attempts allowed
# max_attempts_reached = 'Not Reached'

# # as long as user_password is wrong, run code
# while user_answer != user_password and max_attempts_reached != 'Reached':
#     if num_attempts < max_attempts: # attempts less than allowed , continue code
#         user_answer = input('Enter your password: ')
#         num_attempts += 1 # plus one to counter
        
#     # when the counter gets to max level
#     else:
#         max_attempts_reached = 'Reached'

# # print statement for when max attempts
# if max_attempts_reached == 'Reached':
#     print('You have attempted the maximum allowed attempts for loging in, try again tomorrow.')

# # if the entered password is correct
# else:
#     print('Access Granted.')

# print('-------------------------------')


# ------------------------------------- #
##              Pratice:               ##
##        Testing Combinations         ##
# ------------------------------------- #


print('-------------------------------')

# get all the combinations with nested loops
meal = ['pizza', 'burger', 'spaghetti']
drinks = ['water', 'juice', 'soda']
dessert = ['cake', 'ice cream', 'cookies']

# nested loop
for m in meal: # level 1
    for d in drinks: # level 2
        for ss in dessert: # level 3
            print(f'I will have {m} as my meal. Also I will have {d} as my drink. Dessert will be {ss}.')

print('-------------------------------')