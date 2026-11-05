select * from raw_cookie_cats;

select 
	version,
	count(sum_gamerounds) as total_usuarios,
    round(avg(sum_gamerounds), 2) as media_rodadas_jogadas,
    round(sum(retention_1) * 100 / count(userid), 2) as taxa_retencao_d1_pct,
    round(sum(retention_7) * 100 / count(userid), 2) as taxa_retencao_d7_pct
from raw_cookie_cats
group by version;