import sys

numb = input('enter a number between 1 and 25.  \n')
numb = numb.strip()

def inputTypeChek(input):
    try:
        if not input:
            raise ValueError('I need a value u DumAss')

        if not str.isdigit(input):
            raise ValueError('Where is my number u trash?')

        if int(numb) < 1 or int(numb) > 25:
            raise ValueError('Go check a Dr. ur number ' + numb + ' is invalid')

        return 'You got a GoodOne : ' + numb
    except ValueError as e:
        return e
        sys.exit(1)


print(inputTypeChek(numb))
