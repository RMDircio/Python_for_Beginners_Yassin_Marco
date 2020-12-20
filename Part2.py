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

def calculation(a,b,c):
    print(a + b + c) # if 'return' is placed here, lines below will not print
    print(a - b -c)
    print(a * b * c)

calculation(2,2,2)
print('-------------------------------')


# ------------------------------------- #
##    Understanding the IF Statement   ##      
##               Part 1                ##
# ------------------------------------- #

# boolean values
hungry = False
thirsty = True

# using IF 
if hungry: # --> 'if hungry is True'
    print("Let's grab take out!")
else:
    print("I'll drink some water.")

# using IF with AND
if hungry and thirsty: # --> 'if hungry and thirsty is True'
    print("You grab take out and I'll get some drinks.")
else:
    print('Should we go for a walk?')

# using IF with OR
if hungry or thirsty: # --> 'if hungry or thirsty is True'
    print("You grab take out and I'll get some water for me.")
else:
    print('How about a movie?')

# using TWO IF statements in sequence - needs and else at the end
if hungry:
    print('I have homemade soup and bread for you.')
elif thirsty:
    print('Would you like red or white wine?')
else:
    print("Oh, let's take the dog for a walk then.")

# flipping statements around
if not hungry: # --> if hungry is False
    print('I will come back later')

print('-------------------------------')


# ------------------------------------- #
##    Understanding the IF Statement   ##      
##               Part 2                ##
# ------------------------------------- #

























































