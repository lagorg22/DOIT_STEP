from classes import Person, House

print('Initial setup.\n')
print('<====================================================================================>\n')
xvicha = Person('Xvicha')
gocha = Person('Gocha')

h1 = House('1234', 500)
h2 = House('321', 1400)

print(h1)
print(h2)
print(xvicha)
print(gocha)

print('<====================================================================================>\n')

print('Xvicha buys house1 successfully and Gocha Tries to buy house2 with insufficient loan amount.\n')
print('<====================================================================================>\n')

h1.sale(xvicha)
h2.sale(gocha, 200)

print(h1)
print(h2)
print(xvicha)
print(gocha)

print('<====================================================================================>\n')

print('Gocha buys house2 with appropriate amount of loan.\n')

print('<====================================================================================>\n')

h2.sale(gocha, 1000)

print(h1)
print(h2)
print(xvicha)
print(gocha)

print('<====================================================================================>\n')

print('Xvicha tries to buy house2 with insufficient balance.\n')

print('<====================================================================================>\n')

h2.sale(xvicha)

print(h1)
print(h2)
print(xvicha)
print(gocha)

print('<====================================================================================>\n')

print('Xvicha buys house2 from Gocha with appropriate loan amount.\n')

print('<====================================================================================>\n')

h2.sale(xvicha, 2000)

print(h1)
print(h2)
print(xvicha)
print(gocha)







