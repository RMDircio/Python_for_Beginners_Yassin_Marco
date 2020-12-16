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