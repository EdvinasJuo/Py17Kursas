def finding_pincode():
    count = 1
    while True:
        yield f'{count:04}'
        count += 1

generator = finding_pincode()

secret_pincode = '0512'

for x in range(9999):
    pincode = next(generator)
    print(pincode)
    if pincode == secret_pincode:
        print(f'Your PIN code is: {pincode}')
        break