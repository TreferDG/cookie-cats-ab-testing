select * from raw_cookie_cats;

select
	count(*) as total_linhas,
	count(distinct userid) as total_usuarios
from raw_cookie_cats;

select 
	userid,
    version,
    sum_gamerounds,
    retention_1,
    retention_7
from raw_cookie_cats
where retention_7 is null;

select 
	version,
    count(userid)
from raw_cookie_cats
group by version;