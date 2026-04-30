def greeting():
    print('selamat malam')


greeting()
greeting()
greeting()
greeting()
greeting()

def sayHello(name):
    print(f'Hello {name}')

sayHello('ahmad')
sayHello('salma')
sayHello('fatih')  

def add_print(number1, number2):
    hasil = number1 + number2
    print(hasil)

c = add_print(10,30)

def add_return(number1,number2):
    hasil = number1 + number2
    return hasil
    
d = add_return (20,30)
e = d + 100
print(e)

def subs(number1,number2):
    hasil = number1 - number2
    return hasil

print(subs(100,74))

def kali(number1,number2):
    hasil = number1 * number2
    return hasil 
print(kali(2,5))

def bagi (number1,number2):
    hasil = number1 / number2
    return hasil 
print(bagi(200,4))