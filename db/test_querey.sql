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

select * from acts where act_id like '%3ea2b318%';

select * from episodes;

select acts.*, episodes.episode_name
from acts
join episodes on acts.episode_id = episodes.episode_id;

select * from matches;

select * from dim_periods;


