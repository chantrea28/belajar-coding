total_belanja = input ('total belanja:')
status = input ('apakah anda punya member?:')    

total_belanja = int(total_belanja)
if (total_belanja >200000 or status == "ya"):
    print('anda mendapatkan promo')
else:
    print('anda tidak mendapatkan promo')

