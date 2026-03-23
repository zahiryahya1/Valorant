-- ==========================================
-- PLAYER PERIOD STATS (FINAL VERSION)
-- ==========================================

TRUNCATE TABLE player_period_stats;

INSERT INTO player_period_stats (
    period_type,
    period_id,
    puuid,
    queue_scope,
    initial_rank,
    peak_rank,
    end_rank,
    median_rank,
    matches_played,
    wins,
    losses,
    win_rate,
    total_rounds,
    total_hours,
    total_kills,
    total_deaths,
    total_assists,
    total_damage,
    kd_ratio,
    bombs_planted,
    bombs_defused,
    headshots,
    bodyshots,
    legshots,
    headshot_percent,
    first_bloods,
    aces,
    match_mvps,
    team_mvps,
    avg_kills_per_match,
    avg_damage_per_match,
    highest_kill_game,
    highest_damage_game,
    last_updated
)

WITH base AS (
    SELECT
        pms.puuid,
        pms.match_id,
        pms.agent,
        pms.rank,
        r.rank_value,
        pms.won,

        pms.kills,
        pms.deaths,
        pms.assists,
        pms.damage,

        pms.headshots,
        pms.bodyshots,
        pms.legshots,

        m.map,
        m.game_mode,
        m.rounds_played,
        m.game_length_sec,
        m.date_played,

        dp.period_type,
        dp.period_id,
		
		COALESCE(rnd.bombs_planted,0) AS bombs_planted,
        COALESCE(rnd.bombs_defused,0) AS bombs_defused

    FROM player_match_stats pms
    JOIN matches m 
        ON pms.match_id = m.match_id
    JOIN dim_periods dp 
        ON m.date_played BETWEEN dp.start_date AND dp.end_date
    LEFT JOIN dim_ranks r
        ON pms.rank = r.rank_name
	LEFT JOIN rounds rnd
		ON rnd.match_id = pms.match_id
),

scoped AS (
    SELECT *, 'all' AS queue_scope FROM base
    UNION ALL
    SELECT *, 'competitive' AS queue_scope
    FROM base
    WHERE game_mode = 'Competitive'
),

ranked_matches AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY period_type, period_id, puuid, queue_scope
            ORDER BY date_played ASC
        ) AS rn_first,

        ROW_NUMBER() OVER (
            PARTITION BY period_type, period_id, puuid, queue_scope
            ORDER BY date_played DESC
        ) AS rn_last

    FROM scoped
),

aggregated AS (
    SELECT
        period_type,
        period_id,
        puuid,
        queue_scope,

        MAX(CASE WHEN rn_first = 1 THEN rank END) AS initial_rank,
        MAX(CASE WHEN rn_last = 1 THEN rank END) AS end_rank,

        MAX(rank_value) AS peak_rank_value,

        PERCENTILE_CONT(0.5)
        WITHIN GROUP (ORDER BY rank_value) AS median_rank_value,

        COUNT(DISTINCT match_id) AS matches_played,
        SUM(CASE WHEN won THEN 1 ELSE 0 END) AS wins,
        SUM(CASE WHEN NOT won THEN 1 ELSE 0 END) AS losses,
        ROUND(AVG(CASE WHEN won THEN 1.0 ELSE 0.0 END), 2) AS win_rate,

        SUM(rounds_played) AS total_rounds,
        ROUND( SUM(game_length_sec) / 3600.0, 2) AS total_hours,

        SUM(kills) AS total_kills,
        SUM(deaths) AS total_deaths,
        SUM(assists) AS total_assists,
        SUM(damage) AS total_damage,

        SUM(kills)::FLOAT / NULLIF(SUM(deaths), 0) AS kd_ratio,

        SUM(bombs_planted) AS bombs_planted,
		SUM(bombs_defused) AS bombs_defused,

        SUM(headshots) AS headshots,
        SUM(bodyshots) AS bodyshots,
        SUM(legshots) AS legshots,

		SUM(headshots)::FLOAT /
        	NULLIF(SUM(headshots + bodyshots + legshots), 0) AS headshot_percent,

        0 AS first_bloods,
        0 AS aces,
        0 AS match_mvps,
        0 AS team_mvps,

        ROUND( AVG(kills), 0) AS avg_kills_per_match,
        ROUND( AVG(damage), 0) AS avg_damage_per_match,

        MAX(kills) AS highest_kill_game,
        MAX(damage) AS highest_damage_game,

        NOW() AS last_updated

    FROM ranked_matches
    GROUP BY
        period_type,
        period_id,
        puuid,
        queue_scope
),

final AS (
    SELECT
        a.period_type,
        a.period_id,
        a.puuid,
        a.queue_scope,

        a.initial_rank,
        pr.rank_name AS peak_rank,
        a.end_rank,
        mr.rank_name AS median_rank,

        a.matches_played,
        a.wins,
        a.losses,
        a.win_rate,

        a.total_rounds,
        a.total_hours,

        a.total_kills,
        a.total_deaths,
        a.total_assists,
        a.total_damage,
        a.kd_ratio,

        a.bombs_planted,
        a.bombs_defused,

        a.headshots,
        a.bodyshots,
        a.legshots,
        a.headshot_percent,

        a.first_bloods,
        a.aces,
        a.match_mvps,
        a.team_mvps,

        a.avg_kills_per_match,
        a.avg_damage_per_match,

        a.highest_kill_game,
        a.highest_damage_game,

        a.last_updated

    FROM aggregated a
    LEFT JOIN dim_ranks pr
        ON a.peak_rank_value = pr.rank_value
    LEFT JOIN dim_ranks mr
        ON a.median_rank_value = mr.rank_value
)

SELECT
    period_type,
    period_id,
    puuid,
    queue_scope,
    initial_rank,
    peak_rank,
    end_rank,
    median_rank,
    matches_played,
    wins,
    losses,
    win_rate,
    total_rounds,
    total_hours,
    total_kills,
    total_deaths,
    total_assists,
    total_damage,
    kd_ratio,
    bombs_planted,
    bombs_defused,
    headshots,
    bodyshots,
    legshots,
    headshot_percent,
    first_bloods,
    aces,
    match_mvps,
    team_mvps,
    avg_kills_per_match,
    avg_damage_per_match,
    highest_kill_game,
    highest_damage_game,
    last_updated
FROM final;

select * from player_period_stats
where puuid = 'f9f26d15-776c-57a0-b6bf-be1fc1d3c443';