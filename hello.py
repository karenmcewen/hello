print('hello world!')
name = input('what is your name?')
print('hello ' + name)
year = int(input('what year were you born?'))
age = 2018 - year
print('you are ' + str(age) + ' years old.')
print('You are learning Python!')
# let's do some math
retireYear = year + 65
print('You will retire in ' + str(retireYear))
print('Don\'t forget to push to GitHub!')

# creating a function???
number1 = int(input('enter a number: '))


def square(number1):
    """

    :type number1: int
    """
    return number1 * number1


n2 = square(number1)
print('your number was: ' + str(number1) +' and the square is: ' + str(n2))
