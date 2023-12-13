# dictionary ==> hash table (buổi 5)
product = {
    "id": 1,
    "name": 1,
    "price": 1
}
print(product["price"])
# List dictionary
products = [
    {
        "id": 1,
        "name": "car SUV",
        "price": 4378
    },
    {
        "id": 2,
        "name": "car Extra",
        "price": 2312
    }, {
        "id": 3,
        "name": "car VIP",
        "price": 43
    }
]


for item in products:
    print(f"{item['name']} có giá là {item['price']}")


products = [product for product in products if product["id"] != 2]
print('products: ', products)

# xoá list
