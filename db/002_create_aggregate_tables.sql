-- ==========================================
-- PERIOD TYPE 
-- ==========================================
--  Recap period

CREATE TABLE dim_periods (
    period_type TEXT,   -- act, episode, year
    period_id TEXT,

    start_date DATE,
    end_date DATE,

    episode TEXT,
    act TEXT,
    year INT,
    month INT,
    
    PRIMARY KEY (period_type, period_id)

);

-- ==========================================
-- PLAYER PERIOD SUMMARY
-- ==========================================
-- Core recap statistics for a player over a period

CREATE TABLE player_period_stats (
    period_type TEXT,
    period_id TEXT,
    puuid TEXT,

    queue_scope TEXT, -- 'all' or 'competative'
    initial_rank TEXT,
    peak_rank TEXT,
    end_rank TEXT,
    median_rank TEXT,
    
    matches_played INT,
    wins INT,
    losses INT,
    win_rate FLOAT,

    total_rounds INT,
    total_hours FLOAT,

    total_kills INT,
    total_deaths INT,
    total_assists INT,
    total_damage INT,
    kd_ratio FLOAT,

    bombs_planted INT,
    bombs_defused INT,

    headshots INT,
    bodyshots INT,
    legshots INT,
    headshot_percent FLOAT,

    first_bloods INT,
    aces INT,

    match_mvps INT,
    team_mvps INT,

    avg_kills_per_match FLOAT,
    avg_damage_per_match FLOAT,

    highest_kill_game INT,
    highest_damage_game INT,

    PRIMARY KEY (period_type, period_id, puuid, queue_scope)
);


-- ==========================================
-- PLAYER AGENT PERFORMANCE
-- ==========================================

CREATE TABLE player_agent_period_stats (
    period_type TEXT,
    period_id TEXT,
    puuid TEXT,
    agent TEXT,
    queue_scope TEXT, -- 'all' or 'competative'
    
    pick_count INT,
    matches_played INT,
    wins INT,
    losses INT,
    win_rate FLOAT,

    kills INT,
    deaths INT,
    assists INT,

    kd_ratio FLOAT,

    avg_damage FLOAT,

    PRIMARY KEY (period_type, period_id, puuid, agent, queue_scope)
);


-- ==========================================
-- PLAYER MAP PERFORMANCE
-- ==========================================

CREATE TABLE player_map_period_stats (
    period_type TEXT,
    period_id TEXT,
    puuid TEXT,
    map_name TEXT,
    queue_scope TEXT, -- 'all' or 'competative'

    matches_played INT,
    wins INT,
    losses INT,
    win_rate FLOAT,

    kills INT,
    deaths INT,
    assists INT,
    kd_ratio FLOAT,
    damage INT,
    score INT,

    match_mvp_count INT,
    team_mvp_count INT,

    PRIMARY KEY (period_type, period_id, puuid, map_name, queue_scope)
);



-- ==========================================
-- PLAYER WEAPON PERFORMANCE
-- ==========================================

CREATE TABLE player_weapon_period_stats (
    period_type TEXT,
    period_id TEXT,
    puuid TEXT,
    weapon TEXT,
    queue_scope TEXT, -- 'all' or 'competative'

    kills INT,
    headshots INT,
    bodyshots INT,
    legshots INT,

    headshot_percent FLOAT,

    PRIMARY KEY (period_type, period_id, puuid, weapon, queue_scope)
);


-- ==========================================
-- ROUNDS PERFORMANCE
-- ==========================================
-- determine prefered side. 

CREATE TABLE player_side_period_stats (
    period_type TEXT,
    period_id TEXT,
    puuid TEXT,
    side TEXT,
    queue_scope TEXT, -- 'all' or 'competative'

    rounds_played INT,
    rounds_won INT,
    round_win_rate FLOAT,

    kills INT,
    deaths INT,
    assists INT,
    damage INT,

    PRIMARY KEY (period_type, period_id, puuid, side, queue_scope)
);



-- ==========================================
-- HIGHLIGHT / FUN METRICS
-- ==========================================

CREATE TABLE player_highlight_period_stats (
    period_type TEXT,
    period_id TEXT,
    puuid TEXT,
    queue_scope TEXT, -- 'all' or 'competative'

    best_match_id TEXT,
    best_match_kills INT,
    best_match_damage INT,

    longest_match_id TEXT,
    longest_match_minutes INT,
    longest_match_rounds INT,
    longest_win_streak INT,
    longest_loss_streak INT,
    overtime_matches INT,

    comeback_wins INT,
    total_multikills INT,
    clutch_wins INT,
    total_aces INT,

    PRIMARY KEY (period_type, period_id, puuid, queue_scope)
);
