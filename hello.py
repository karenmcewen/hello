# basic input and output

print('hello world!')
name = input('what is your name?')
print('hello ' + name)

year = int(input('what year were you born?'))
age = 2018 - year
print('you are ' + str(age) + ' years old.')

# let's do some math
retireYear = year + 65
print('You will retire in ' + str(retireYear))

# creating a function - function def needs to be before the function is called

def square(number1):
    """

    :type number1: int
    """
    return number1 * number1
# two lines separate a function from the rest of the program


# back to the main program
number1 = int(input('enter a number: '))
n2 = square(number1)
print('your number was: ' + str(number1) + ' and the square is: ' + str(n2))
print()
print('You are learning Python!')
print('Don\'t forget to push to GitHub!')
