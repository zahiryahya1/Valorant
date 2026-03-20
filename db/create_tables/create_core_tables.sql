

-- ==========================================
-- PLAYERS
-- ==========================================
-- Stores unique players. Even if you only
-- track yourself now, this allows scaling
-- later for multiple users.

CREATE TABLE players (
    puuid TEXT PRIMARY KEY,
    game_name TEXT,
    tag TEXT
);


-- ==========================================
-- MATCHES
-- ==========================================
-- Stores match level metadata

CREATE TABLE matches (
    match_id TEXT PRIMARY KEY,
    date_played TIMESTAMP NOT NULL,
    map TEXT NOT NULL,
    game_mode TEXT NOT NULL,
    season_id TEXT,
    season_name TEXT,
    act_id TEXT,
    act_name TEXT,
    game_start TIMESTAMP NOT NULL,
    game_length_sec INT,
    rounds_played INT
);


-- ==========================================
-- PLAYERS MATCH STATS
-- ==========================================
-- One row per player per match

CREATE TABLE player_match_stats (
    match_id TEXT,
    puuid TEXT,
    team TEXT,
    agent TEXT,
    rank TEXT,
    won BOOLEAN,

    kills INT,
    deaths INT,
    assists INT,
    score INT,
    damage INT,

    headshots INT,
    bodyshots INT,
    legshots INT,

    afk_rounds INT,
    friendly_fire_incoming INT,
    friendly_fire_outgoing INT,

    PRIMARY KEY (match_id, puuid),
    FOREIGN KEY (match_id) REFERENCES matches(match_id),
    FOREIGN KEY (puuid) REFERENCES players(puuid)
);


-- ==========================================
-- ROUNDS
-- ==========================================
-- Stores each round within a match

CREATE TABLE rounds (
    match_id TEXT,
    round_number INT,
    winning_team TEXT,
    round_end_reason TEXT,
    bomb_planted_player TEXT, -- puuid of player who planted/defused, or NULL
    bomb_defused_player TEXT, -- puuid of player who planted/defused, or NULL

    PRIMARY KEY (match_id, round_number),
    FOREIGN KEY (match_id) REFERENCES matches(match_id)
);


-- ==========================================
-- KILL EVENTS
-- ==========================================
-- Stores every kill event in a match

CREATE TABLE kill_events (
    match_id TEXT,
    round_number INT,
    kill_time_in_round INT,

    killer_puuid TEXT,
    victim_puuid TEXT,

    killer_team TEXT,
    victim_team TEXT,

    weapon TEXT,

    PRIMARY KEY (
            match_id,
            round_number,
            kill_time_in_round,
            killer_puuid,
            victim_puuid
        ),

    FOREIGN KEY (match_id) REFERENCES matches(match_id)
);


-- ==========================================
-- DAMAGE EVENTS
-- ==========================================
-- Stores every damage instance

CREATE TABLE damage_events (
    match_id TEXT,
    round_number INT,

    attacker_puuid TEXT,
    receiver_puuid TEXT,

    damage INT,
    headshots INT,
    bodyshots INT,
    legshots INT,

    PRIMARY KEY (
        match_id,
        round_number,
        attacker_puuid,
        receiver_puuid
    )
);


-- ==========================================
-- SESSIONS
-- ==========================================
-- A gameplay session is defined as a group
-- of matches with less than 30 minutes gap

CREATE TABLE sessions (
    session_id SERIAL PRIMARY KEY,
    puuid TEXT,

    start_time TIMESTAMP,
    end_time TIMESTAMP,

    total_matches INT,
    total_minutes INT
);


-- ==========================================
-- SESSION MATCHES
-- ==========================================
-- Links matches to sessions

CREATE TABLE session_matches (
    session_id INT,
    match_id TEXT,

    PRIMARY KEY (session_id, match_id),

    FOREIGN KEY (session_id) REFERENCES sessions(session_id),
    FOREIGN KEY (match_id) REFERENCES matches(match_id)
);

-- ==========================================
-- EPISODES
-- ==========================================
CREATE TABLE episodes (
    episode_id TEXT PRIMARY KEY,
    episode_name TEXT NOT NULL
);


-- ==========================================
-- ACTS
-- ==========================================
CREATE TABLE acts (
    act_id TEXT PRIMARY KEY,
    act_name TEXT NOT NULL,
    episode_id TEXT NOT NULL,
    is_active BOOLEAN,
    is_previous BOOLEAN,
    FOREIGN KEY (episode_id) REFERENCES episodes(episode_id)
);