from models import Product, CartItem, Order, OrderItem, session
from datetime import datetime

def display_cart():
    cart_items_products: list[tuple[CartItem, Product]] = list(session.query(CartItem, Product).join(Product, CartItem.product_id == Product.id))

    if len(cart_items_products) == 0:
        print('Cart is empty!\n')
    else:
        print('Cart:')
        total = 0
        for cart_item, item in cart_items_products:
            print(f'id: {cart_item.id}, name: {item.name}, quantity: {cart_item.quantity}, price: {item.price * cart_item.quantity}')
            total += item.price * cart_item.quantity
        print(f'\nTotal: {total}\n')

def add_item():
    item_id = int(input('Enter item id: '))
    quantity = int(input('Enter the quantity: '))
    products: list[Product]= list(session.query(Product).all())
    try:
        item: Product = list(filter((lambda product: product.id == item_id), products))[0]
        if item.quantity_in_stock < quantity:
            print(f'Not enough in stock! theres only {item.quantity_in_stock} left.\n')
        else:
            cart_item = CartItem(product_id=item_id, quantity=quantity)
            session.add(cart_item)
            # item.quantity_in_stock -= quantity
            session.commit()
    except:
        print('Incorrect id.\n')

def remove_item():
    cart_item_id = int(input('Enter cart item id: '))
    item_to_remove = session.query(CartItem).filter(CartItem.id == cart_item_id).first()
    session.delete(item_to_remove)
    session.commit()
    print('item removed successfully.\n')

def place_order():
    cart_items_products: list[tuple[CartItem, Product]] = list(session.query(CartItem, Product).join(Product, CartItem.product_id == Product.id).all())
    if not cart_items_products:  # Corrected empty cart check
        print('Your cart is empty.\n')
        return

    order = Order(order_date=datetime.now(), total_amount=0)
    session.add(order)
    session.commit()

    order_items = []
    total = 0
    for cart_item, product in cart_items_products:
        order_item = OrderItem(order_id=order.id, product_id=product.id, quantity=cart_item.quantity, price_per_item=product.price)
        order_items.append(order_item)
        total += order_item.price_per_item * order_item.quantity

        product.quantity_in_stock -= cart_item.quantity
        session.delete(cart_item)

    order.total_amount = total
    session.add_all(order_items)
    session.commit()

    print("Order placed successfully!\n")

def view_orders():
    orders: list[Order] = list(session.query(Order).all())
    if len(orders) == 0:
        print('You don\'t have any orders yet.\n')
    else:
        print('Here are all of your orders:')
        for order in orders:
            print(f'\n{order.order_date}: {order.total_amount}')
            order_items = session.query(OrderItem).all()
            for oi in order_items:
                if oi.order_id == order.id:
                    print(oi)

def display_products():
    products = session.query(Product).all()
    print('Here are the products available in the store:\n')
    for p in products:
        print(p)
    print()

def show_commands():
    print('\nplease enter one of this commands to proceed:\n'
          'to see cart: dc\n'
          'to add item: ai\n'
          'to remove item: ri\n'
          'to place order: po\n'
          'to view orders: vo\n'
          'to display products: dp\n'
          'to show commands: sc\n'
          'to exit anything else.\n')

commands = {
    'dc': display_cart,
    'ai': add_item,
    'ri': remove_item,
    'po': place_order,
    'vo': view_orders,
    'dp': display_products,
    'sc': show_commands
}

show_commands()

while True:
    command = input('Enter command:')
    if command in commands.keys():
        commands[command]()
    else:
        print('have a nice day\n')
        break




