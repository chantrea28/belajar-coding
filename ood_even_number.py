num_start = int(input('enter start number:'))
end_start = int(input('enter end number:'))

for i in range(num_start, end_start):

    if i % 2 == 0:
        print(f'{i} is even number')
    else:
        print(f'{i} is odd number')