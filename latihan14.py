number = 1

while  number < 1000:
    print('i like pyhton')
    number += 1

colors = {'red','blue','green','yellow'}
print(colors)
for color in colors:
    print(color)

for i in range(1,11):
    if i ==5:
        break
    else:
        print(i)
        print('I like pyhton') 
for i in range(20):
    if i == 15:
        continue
    print(i)
else:
    print('finished')
for i in range(100):
    pass  


    fruits = {'apple','mango','banana'}

for color in colors:
    for fruit in fruits:
        print(f'{color} {fruits}')

