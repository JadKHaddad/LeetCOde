drop table if exists Person;
create table Person (PersonId integer NOT NULL PRIMARY KEY, FirstName varchar(100), LastName varchar(100));
		insert into Person (PersonId, FirstName, LastName) values (1, 'albert', 'einstein');
		insert into Person (PersonId, FirstName, LastName) values (2, 'isaac', 'newton');
		insert into Person (PersonId, FirstName, LastName) values (3, 'marie', 'curie');

drop table if exists Address;       
create table Address (AddressId integer NOT NULL PRIMARY KEY, PersonId integer, City varchar(100), State varchar(100));
		insert into Address (AddressId, PersonId, City, State) values (1, 2, 'London', 'UK');
		insert into Address (AddressId, PersonId, City, State) values (3, 1, 'Honk-Kong', 'Honk-Kong');

select Person.FirstName, Person.LastName, Address.City, Address.State from Person left join Address on Person.PersonId = Address.PersonId