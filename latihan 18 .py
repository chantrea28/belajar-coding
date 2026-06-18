def factorial(number):
    if number <=1 :
        return 1
    else:
        result = number * factorial (number - 1)
        return result
    


angka = int(input('ENTER FIRST NUMBER: '))
hasil = factorial(angka)
print("hasil factorialnya adalah",hasil)
