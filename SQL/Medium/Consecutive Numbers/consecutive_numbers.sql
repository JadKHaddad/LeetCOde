drop table if exists Logs;
create table Logs (Id integer, num VARCHAR(100));
        insert into Logs (Id, num) values (1, '1');
        insert into Logs (Id, num) values (2, '1');
        insert into Logs (Id, num) values (3, '1');
        insert into Logs (Id, num) values (4, '2');
        insert into Logs (Id, num) values (5, '1');
        insert into Logs (Id, num) values (6, '2');
        insert into Logs (Id, num) values (7, '2');

select distinct num as ConsecutiveNums from logs 
    where (select count(*) from (select l.num from logs as l 
        where l.num = logs.num and (l.id = logs.id + 1 or l.id = logs.id - 1)) as t ) > 1;
