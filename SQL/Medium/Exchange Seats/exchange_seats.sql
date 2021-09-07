drop table if exists seat;
create table seat (id integer, student varchar(100));
		insert into seat (id, student) values (1, 'Abbot');
        insert into seat (id, student) values (2, 'Doris');
        insert into seat (id, student) values (3, 'Emerson');
        insert into seat (id, student) values (4, 'Green');
		insert into seat (id, student) values (5, 'Jeames');

with
    odd as(select id + 1 as id, student from seat where id % 2 = 1 and id + 1 in (select id from seat)),
    even as(select id - 1 as id, student from seat where id % 2 = 0),
    uni as(select id, student from odd union ALL select id, student from even)
        select id, student from uni union ALL select id, student from seat where id % 2 = 1 and id + 1 not in(select id from seat) order by id asc;