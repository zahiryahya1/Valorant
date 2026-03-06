CREATE TABLE player_period_stats (
    period_type TEXT,
    period_id TEXT,
    player_puuid TEXT,

    matches_played INT,
    wins INT,
    losses INT,
    win_rate FLOAT,

    total_kills INT,
    total_deaths INT,
    total_assists INT,
    kd_ratio FLOAT,

    total_damage INT,

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

    PRIMARY KEY (period_type, period_id, player_puuid)
);


CREATE TABLE player_agent_period_stats (
    period_type TEXT,
    period_id TEXT,
    player_puuid TEXT,
    agent TEXT,

    matches_played INT,
    wins INT,
    losses INT,
    win_rate FLOAT,

    kills INT,
    deaths INT,
    assists INT,

    kd_ratio FLOAT,

    avg_damage FLOAT,

    PRIMARY KEY (period_type, period_id, player_puuid, agent)
);



CREATE TABLE player_map_period_stats (
    period_type TEXT,
    period_id TEXT,
    player_puuid TEXT,
    map_name TEXT,

    matches_played INT,
    wins INT,
    losses INT,
    win_rate FLOAT,

    kills INT,
    deaths INT,
    assists INT,

    PRIMARY KEY (period_type, period_id, player_puuid, map_name)
);


CREATE TABLE player_weapon_period_stats (
    period_type TEXT,
    period_id TEXT,
    player_puuid TEXT,
    weapon TEXT,

    kills INT,
    headshots INT,
    bodyshots INT,
    legshots INT,

    headshot_percent FLOAT,

    PRIMARY KEY (period_type, period_id, player_puuid, weapon)
);


CREATE TABLE player_highlight_period_stats (
    period_type TEXT,
    period_id TEXT,
    player_puuid TEXT,

    best_match_id TEXT,
    best_match_kills INT,
    best_match_damage INT,

    longest_match_id TEXT,
    longest_match_minutes INT,
    longest_match_rounds INT,

    total_multikills INT,
    clutch_wins INT,

    PRIMARY KEY (period_type, period_id, player_puuid)
);


