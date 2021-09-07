drop table if exists Employee;
create table Employee (Id integer, Name VARCHAR(100), Salary integer, ManagerId integer);
		insert into Employee (Id, Name, Salary, ManagerId) values (1, 'Joe', 70000, 3);
		insert into Employee (Id, Name, Salary, ManagerId) values (2, 'Henry', 80000, 4);
	    insert into Employee (Id, Name, Salary) values (3, 'Sam', 60000);
	    insert into Employee (Id, Name, Salary) values (4, 'Max', 90000);
	    
select Name as Employee from Employee as e where e.Salary > (select Salary from Employee where Id = e.ManagerId);