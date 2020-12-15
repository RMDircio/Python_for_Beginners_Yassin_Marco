print('Hello World')

# ------------------------------------- #
##  playing with string and variables  ##
# ------------------------------------- #

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

having_a_house = True

if having_a_house:
    print('I own a small house')