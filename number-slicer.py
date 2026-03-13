# create a variable called 'numbers'
# creat a list of numbers 1 - 250 using list(range())

# print a number from index 15


# print an eight number from the back
# clue : negative indexing


# print a group of numbers, start from 55 until 67



# print a group of even numbers, starts from 70 until 240
# clue : use step parameter



numbers = range(250)
print(list(numbers))

#start.stop 
numbers = range (1,250)
print(list(numbers))

print(numbers[15])
print(numbers[-8])

print(list(numbers[55:67]))

#start.stop.step
numbers = range(70,240,2)
print(list(numbers))