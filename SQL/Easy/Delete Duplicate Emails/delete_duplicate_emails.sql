drop table if exists Person;
create table Person (Id integer, Email VARCHAR(100));
        insert into Person (Id, Email) values (1, 'john@example.com');
        insert into Person (Id, Email) values (2, 'bob@example.com');
        insert into Person (Id, Email) values (3, 'john@example.com');

delete from person 
    where id not in(select min(id) as id from (select * from person) as t1 group by email having count(id) > 1) 
    and email in(select email from (select * from person) as t2 group by email having count(id) > 1);