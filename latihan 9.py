numbers = { 1,2,3,4,5,3,2,9}

print(numbers)
print(type(numbers))
print(len(numbers))

animals = {'panda','cat','lion','bird'}
print(animals)
print(len(animals))

#print(animals[0])  -> error

for i in animals:
    print(i)

animals.add ("python")
print(animals)

animals.discard('panda')
print(animals)

animals.discard('mouse')
print(animals)

animals.remove('bird')
 #animals.remove('dog')--> error karena dog tidak ada di dalam sets animals

animals.pop()
print(animals)

fruits = {'apple','manggo','melon'}

fruits_list = {'durian','banana'}

print(fruits)

fruits.update(fruits_list)
print(fruits)

cars = set (('honda','suzuki','toyota'))
print(cars)