from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


host = 'localhost'
port = '5432'
user = 'postgres'
password = 'lashaL001'
database = 'doit_step'

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, nullable=False)
    quantity_in_stock = Column(Integer, nullable=False)

    def  __str__(self):
        return f'id: {self.id}, name: {self.name}, price: {self.price}, quantity available: {self.quantity_in_stock}'

class CartItem(Base):
    __tablename__ = 'cartitems'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1    )


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_date = Column(DateTime, nullable=False)
    total_amount = Column(Float, nullable=False)


class OrderItem(Base):
    __tablename__ = 'orderitems'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_per_item = Column(Float, nullable=False)
    product = relationship('Product')
    def __str__(self):
        return f'order id: {self.order_id}, product: {self.product.name}, quantity: {self.quantity}, price per item: {self.price_per_item}'

Session = sessionmaker(bind=engine)
session = Session()


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    p1 = Product(name='Snickers', price=2.49, quantity_in_stock=160)
    p2 = Product(name='Coca-Cola', price=1.8, quantity_in_stock=290)
    p3 = Product(name='Pepsi', price=1, quantity_in_stock=500)
    p4 = Product(name='Banana', price=2.4, quantity_in_stock=160)
    p5 = Product(name='Orange', price=4, quantity_in_stock=290)
    p6 = Product(name='Apple', price=1, quantity_in_stock=500)

    session.add_all([p1, p2, p3, p4, p5, p6])
    session.commit()

