drop table if exists Employee;
create table Employee (Id integer, Name VARCHAR(100), Salary integer, DepartmentId integer);
		insert into Employee (Id, Name, Salary, DepartmentId) values (1, 'Joe', 70000, 1);
		insert into Employee (Id, Name, Salary, DepartmentId) values (2, 'Jim', 90000, 1);
		insert into Employee (Id, Name, Salary, DepartmentId) values (3, 'Henry', 80000, 2);
		insert into Employee (Id, Name, Salary, DepartmentId) values (4, 'Sam', 60000, 2);
		insert into Employee (Id, Name, Salary, DepartmentId) values (5, 'Max', 90000, 1);

drop table if exists Department;
create table Department (Id integer, Name VARCHAR(100));
        insert into Department (Id, Name) values (1, 'IT');
        insert into Department (Id, Name) values (2, 'Sales');

select department.name as department, e.name as employee, e.salary as salary from employee as e, department where e.departmentid = department.id
    and e.salary = (select max(salary) from employee where employee.departmentid = e.departmentid)
