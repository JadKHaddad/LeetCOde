drop table if exists Trips;
create table Trips (Id integer, Client_Id integer, Driver_Id integer, City_Id integer, Status ENUM('completed','cancelled_by_driver','cancelled_by_client'), Request_at date);
        insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values (1, 1, 10, 1, 'completed', '2013-10-01');
        insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values (2, 2, 11, 1, 'cancelled_by_driver', '2013-10-01');
        insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values (3, 3, 12, 6, 'completed', '2013-10-01');
        insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values (4, 4, 13, 6, 'cancelled_by_client', '2013-10-01');
        insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values (5, 1, 10, 1, 'completed', '2013-10-02');
        insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values (6, 2, 11, 6, 'completed', '2013-10-02');
        insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values (7, 3, 12, 6, 'completed', '2013-10-02');
        insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values (8, 2, 12, 12, 'completed', '2013-10-03');
        insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values (9, 3, 10, 12, 'completed', '2013-10-03');
        insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values (10, 4, 13, 12, 'cancelled_by_driver', '2013-10-03');

drop table if exists Users;
create table Users (Users_id integer, Banned enum('Yes', 'No'), Role enum('client', 'driver', 'partner'));
        insert into Users(Users_id, Banned, Role) values (1, 'No', 'client');
        insert into Users(Users_id, Banned, Role) values (2, 'Yes', 'client');
        insert into Users(Users_id, Banned, Role) values (3, 'No', 'client');
        insert into Users(Users_id, Banned, Role) values (4, 'No', 'client');
        insert into Users(Users_id, Banned, Role) values (10, 'No', 'driver');
        insert into Users(Users_id, Banned, Role) values (11, 'No', 'driver');
        insert into Users(Users_id, Banned, Role) values (12, 'No', 'driver');
        insert into Users(Users_id, Banned, Role) values (13, 'No', 'driver');


with 
    not_banned_ as(select trips.* from trips left join users on Client_id = users_id where users.Banned = 'No'),
    not_banned as(select not_banned_.* from not_banned_ left join users on Driver_id = users_id where users.Banned = 'No'),
    all_trips as(select request_at, count(*) as all_trips from not_banned group by request_at),
    completed_trips as(select request_at, count(*) as completed_trips from not_banned where status = 'completed' group by request_at),
    info as(select all_trips.request_at, IFNULL(all_trips.all_trips, 0) as all_trips, IFNULL(completed_trips.completed_trips, 0) as completed_trips from all_trips left join completed_trips on all_trips.request_at = completed_trips.request_at),
    info2 as(select request_at as Day, ROUND((all_trips - completed_trips)/all_trips, 2) as `Cancellation Rate` from info)
        select * from info2 where `Cancellation Rate` is not null and Day between '2013-10-01' and '2013-10-03';


WITH tbl1 AS ( 
    SELECT users_id 
    FROM   users 
    WHERE  banned='No'
)
SELECT   Request_at as Day, round(sum(status != 'completed')/COUNT(*),2) as 'Cancellation Rate'
FROM     trips 
WHERE    client_id IN 
            ( 
                SELECT * 
                FROM   tbl1
            ) 
AND      driver_id IN 
            ( 
                SELECT * 
                FROM   tbl1
            ) 
AND      request_at BETWEEN '2013-10-01' AND '2013-10-03' 
GROUP BY 1