drop table if exists Customers;
create table Customers (Id integer, Name VARCHAR(100));
        insert into Customers (Id, Name) values (1, 'Joe');
        insert into Customers (Id, Name) values (2, 'Henry');
        insert into Customers (Id, Name) values (3, 'Sam');
        insert into Customers (Id, Name) values (4, 'Max');

drop table if exists Orders;
create table Orders (Id integer, CustomerId integer);
        insert into Orders (Id, CustomerId) values (1, 3);
        insert into Orders (Id, CustomerId) values (2, 1);

select Customers.name as Customers from Customers where Customers.id not in (select CustomerId from orders);
