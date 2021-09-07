drop table if exists Employee;
create table Employee (Id integer, Salary integer);
		insert into Employee (Id, Salary) values (1, 300);
		insert into Employee (Id, Salary) values (2, 500);
		insert into Employee (Id, Salary) values (3, 900);

select max(Salary) as SecondHighestSalary from Employee where Salary < (select max(Salary) from Employee);