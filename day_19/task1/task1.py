import json
from faker import Faker
import random

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price}, {self.quantity}'

products = [Product(Faker().color_name(), random.randint(10, 190), random.randint(10, 140)) for _ in range(100)]

def ser(product: Product):
    return {'name': product.name,
            'price': product.price,
            'quantity': product.quantity
            }


with open('result.json', 'w') as f:
    json.dump(products, f, default=ser, indent=4)

def deser(data: dict):
    return Product(data['name'], data['price'], data['quantity'])

with open('result.json', 'r') as f:
    data = json.load(f, object_hook=deser)

for p in data:
    print(p)


