drop table if exists Person;
create table Person (Id integer, Email VARCHAR(100));
        insert into Person (Id, Email) values (1, 'a@b.com');
        insert into Person (Id, Email) values (2, 'c@d.com');
        insert into Person (Id, Email) values (3, 'a@b.com');

select email from person group by email having count(id) > 1;