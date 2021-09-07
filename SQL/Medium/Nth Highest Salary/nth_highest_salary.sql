drop table if exists Employee;
create table Employee (Id integer, Salary integer);
		insert into Employee (Id, Salary) values (1, 300);
		insert into Employee (Id, Salary) values (2, 500);
		insert into Employee (Id, Salary) values (3, 900);

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET n = N - 1;
    RETURN (
        select max(Salary) as getNthHighestSalary from Employee where Salary <= (select Salary from Employee group by Salary order by Salary desc limit n, 1)
    ); 
END

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET n = N - 1;
    RETURN (
        select Salary from Employee group by Salary order by Salary desc limit n, 1
    ); 
END