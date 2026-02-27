numbers = [10,28,12,25,18]
fruits = ['apple','banana','cherry']
cars = ['toyota','honda','tesla']
name= ['andi','budi','ahmad','taufik']

print(type(numbers))
print(len(numbers))

print(type(cars))
print(len(cars))

print(fruits)
print(fruits[1])
print(fruits[2])

print(name[2])

print(cars[0])

fruits[2] = 'durian'
print(fruits)

fruits.append('melon')
print(fruits)

fruits.remove('banana')
print(fruits)

fruits.clear()
print(fruits)

country = list(("indonesia","malaysia","jepang"))
print(country)
print(type(country))

print(20*'=')
print('tupple')

animals = ("fish","lion","tutle")
print(animals)
print(type(animals))

koordinat = (-90,123,103.678)

print(animals[0])
print(animals[2])

#koordinat[0] = 80.567

koordinat_list =  list(koordinat)
print(koordinat_list)
koordinat_list[0] = 80.567
print(koordinat_list)

koordinat = tuple(koordinat_list)
print(koordinat)