create table customers(
    customer_id serial primary key,
    customer_name varchar(100),
    customer_phone varchar(25),
    delivery_address varchar(100)
);

drop table customers;

insert into customers (customer_id, customer_name, customer_phone, delivery_address)
values
(1, 'Alice Brown', '555-1234', '123 Elm Street'),
(2, 'Bob Green', '555-5678', '456 Oak Avenue'),
(3, 'Charlie Smith', '555-7890', '789 Pine Road'),
(4, 'Diane White', '555-3456', '456 Oak Avenue');

create table products(
    product_id serial primary key,
    product_name varchar(100),
    product_category varchar(100),
    product_category_type varchar(100),
product_price float
);

drop table products;

insert into products (product_id, product_name, product_category, product_category_type, product_price)
values
(1, 'MacBook Air M2', 'Electronics', 'Laptop', 1200),
(2, 'iPhone 14 Pro', 'Electronics', 'Smartphone', 1100),
(3, 'Herman Miller Chair', 'Furniture', 'Office Chair', 1500),
(4, 'Dell XPS 13', 'Electronics', 'Laptop', 1000),
(5, 'Samsung Galaxy S23', 'Electronics', 'Smartphone', 900),
(6, 'Logitech MX Master 3', 'Electronics', 'Computer Accessory', 99.99),
(7, 'Sony WH-1000XM5', 'Electronics', 'Headphones', 349.99),
(8, 'Ikea Bekant Desk', 'Furniture', 'Office Desk', 299.99);

create table orders (
    order_id serial primary key ,
    customer_id int not null references customers(customer_id),
    product_id int not null references products(product_id),
    quantity int not null ,
    order_date date not null
);

insert into  orders (order_id, customer_id, product_id, quantity, order_date)
values
(1, 1, 1, 1, '2025-01-01'),
(2, 2, 2, 2, '2025-01-02'),
(3, 1, 3, 1, '2025-01-03'),
(4, 2, 4, 1, '2025-01-04'),
(5, 1, 5, 1, '2025-01-05'),
(6, 3, 6, 2, '2025-01-06'),
(7, 4, 7, 1, '2025-01-07'),
(8, 3, 8, 1, '2025-01-08');


