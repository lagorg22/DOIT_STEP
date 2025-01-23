create database deposit_management;

SET DateStyle TO 'ISO, DMY';

create table deposits(
    deposit_id serial primary key,
    deposit_owner_name varchar(30),
    date_of_birth date,
    city varchar(100),
    street_name varchar(100),
    deposit_amount float,
    interest varchar(100),
    commission float,
    total float
);

insert into deposits (deposit_owner_name, date_of_birth, city, street_name)
values ('lasha gorgodze', '21-01-2004', 'tbilis', 'beliashvili'),
       ('gocha kirvalidze', '11-02-1982', 'batumi', 'rustaveli'),
       ('saba kavelashvili', '11-11-2000', 'poti', 'guramishvili');

insert into Deposits (deposit_owner_name, date_of_birth, deposit_amount, commission, total)
values
    ('John Doe', '01/01/1990', 1000.00, 5.0, 1050.00),
    ('Jane Smith', '15/05/1985', 2000.00, 4.5, 2045.00),
    ('Alice Johnson', '23/08/1982', 3000.00, 6.0, 3180.00),
    ('Bob Brown', '10/11/1975', 1500.00, 5.2, 1578.00),
    ('Charlie White', '22/03/1995', 2500.00, 4.8, 2620.00),
    ('David Black', '09/09/1980', 1200.00, 5.1, 1261.20),
    ('Eve Green', '03/06/1992', 2800.00, 4.7, 2931.60),
    ('Frank Blue', '17/01/1978', 2200.00, 5.3, 2316.00),
    ('Grace Red', '12/12/1987', 3500.00, 4.9, 3671.50),
    ('Hank Purple', '21/07/1993', 1800.00, 5.4, 1897.20);


select * from deposits;

