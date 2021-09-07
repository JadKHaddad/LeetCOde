drop table if exists Weather;
create table Weather (Id integer, recordDate date, temperature integer);
        insert into Weather (Id, recordDate, temperature) values (1, '2015-01-01', 10);
        insert into Weather (Id, recordDate, temperature) values (2, '2015-01-02', 25);
        insert into Weather (Id, recordDate, temperature) values (3, '2015-01-03', 20);
        insert into Weather (Id, recordDate, temperature) values (4, '2015-01-05', 30);

select id from weather 
    where temperature > (select w.temperature from weather as w 
        where w.recordDate = (select DATE_SUB(weather.recordDate, INTERVAL 1 DAY))  
    order by w.recordDate desc limit 1);