select 
	acts.act_name as act_name,
	episodes.episode_name,
	episodes.episode_id
from acts
join episodes
on acts.episode_id = episodes.episode_id
where is_active = true;

select act_name from acts 
where is_active = true;

select * from episodes;

select * from acts;

select * from player_period_stats;
select * from acts;
