#positional argument
def addition(a,b):
    hasil = a + b
    return hasil

print(addition (10,40))
print(addition (70,30))
print(addition (12,82))
print(addition (57,12))
print(addition (25,18))

#arbitrary argument *
def sumnumbers(*numbers):
    result = 0
    for num in numbers:
        result += num

    return result

print(sumnumbers(1,2,3,4,5,6,7,8))
print(sumnumbers(10,20,30,40,50))