products = []
while True:
    name = input('name')
    if name == 'q':
        break
    price = input('price')
    products.append([name, price])
print(products)