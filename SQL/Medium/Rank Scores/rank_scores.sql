drop table if exists scores;
create table scores (id integer, score DECIMAL(2,1));
        insert into scores (id, score) values (1, 3.50);
        insert into scores (id, score) values (2, 3.65);
        insert into scores (id, score) values (3, 4.00);
        insert into scores (id, score) values (4, 3.85);
        insert into scores (id, score) values (5, 4.00);
        insert into scores (id, score) values (6, 3.65);

select scores.score as score, t2.r as `Rank` 
    from scores, (select t.* , ROW_NUMBER() OVER (ORDER BY t.score desc) as r 
        from (select score 
            from scores group by score order by score desc) as t) as t2 
                where scores.score = t2.score order by scores.score desc;