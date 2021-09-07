drop table if exists courses;
create table courses (student varchar(100), class varchar(100));
		insert into courses (student, class) values ('A', 'Math');
        insert into courses (student, class) values ('B', 'English');
        insert into courses (student, class) values ('C', 'Math');
        insert into courses (student, class) values ('D', 'Biology');
        insert into courses (student, class) values ('E', 'Math');
        insert into courses (student, class) values ('F', 'Computer');
        insert into courses (student, class) values ('G', 'Math');
        insert into courses (student, class) values ('H', 'Math');
        insert into courses (student, class) values ('I', 'Math');
	
select class from courses group by class having count(distinct(student)) >= 5;