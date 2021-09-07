drop table if exists Employee;
create table Employee (Id integer, Name VARCHAR(100), Salary integer, DepartmentId integer);
        insert into Employee (Id, Name, Salary, DepartmentId) values (1, 'Joe', 85000, 1);
        insert into Employee (Id, Name, Salary, DepartmentId) values (2, 'Henry', 80000, 2);
        insert into Employee (Id, Name, Salary, DepartmentId) values (3, 'Sam', 60000, 2);
        insert into Employee (Id, Name, Salary, DepartmentId) values (4, 'Max', 90000, 1);
        insert into Employee (Id, Name, Salary, DepartmentId) values (5, 'Janet', 69000, 1);
        insert into Employee (Id, Name, Salary, DepartmentId) values (6, 'Randy', 85000, 1);
        insert into Employee (Id, Name, Salary, DepartmentId) values (7, 'Will', 70000, 1);

drop table if exists Department;
create table Department (Id integer, Name VARCHAR(100));
        insert into Department (Id, Name) values (1, 'IT');
        insert into Department (Id, Name) values (2, 'Sales');

select department.name as department, e.name as employee, e.salary as salary from employee as e, department where e.departmentid = department.id
    and e.salary in(select * from (select employee.salary from employee where employee.departmentid = e.departmentid group by employee.salary order by employee.salary desc limit 0, 3) as s);
