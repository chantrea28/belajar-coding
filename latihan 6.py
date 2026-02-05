a = 10
b = 15

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a != b)
print(a <= b)

print(a > 20 and a < 30)
print(a > 7 and a < 12)
print(a > 20 or a < 30)
print(a > 20 or a == 30)
user = input ('masukan username/email:')
pwd = input ('masukan password:')             


if (user == "admin" or user == 'admin@gmail.com') and pwd == '123456':
    print ('berhasil login')
else:
    print('login gagal. ussername atau password salah.')


