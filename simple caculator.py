print("simple caculator")
print(20*"=")

number1 = input('Enter first number:')
number2 = input("Enter second number:")

number1 = int(number1)
number2 = int(number2)

add = number1 + number2
print(f'{number1} + {number2} = {add}')

subs = number1 - number2
print(f'{number1} - {number2} = {subs}')

multi = number1 * number2
print(f'{number1} * {number2} = {multi}')

div = number1 / number2
print(f'{number1}  / {number2} = {div}')

