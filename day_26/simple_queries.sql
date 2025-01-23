select * from deposits where deposit_amount > 1500;

select * from deposits where city = 'tbilisi' and street_name = 'rustaveli';

select * from deposits where
                           city = 'batumi' and
                           street_name = 'gorgasali' and
                           deposit_amount between 1000 and 2000;

select * from deposits where substring(deposit_owner_name, 1, 1) = 'd';

select * from deposits;

update deposits set commission = 0 where date_of_birth < '1-1-1980';

delete from deposits where total is null;

truncate deposits;

drop table deposits;


