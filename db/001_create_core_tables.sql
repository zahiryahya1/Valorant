

-- ==========================================
-- PLAYERS
-- ==========================================
-- Stores unique players. Even if you only
-- track yourself now, this allows scaling
-- later for multiple users.

CREATE TABLE players (
    player_puuid TEXT PRIMARY KEY,
    game_name TEXT,
    tag_line TEXT
);


-- ==========================================
-- MATCHES
-- ==========================================
-- Stores match level metadata

CREATE TABLE matches (
    match_id TEXT PRIMARY KEY,
    date_played TIMESTAMP NOT NULL,
    map_name TEXT NOT NULL,
    game_mode TEXT NOT NULL,
    season_id TEXT,
    act_id TEXT,
    game_start TIMESTAMP NOT NULL,
    game_length_seconds INT
);


-- ==========================================
-- MATCH PLAYERS
-- ==========================================
-- One row per player per match

CREATE TABLE match_players (
    match_id TEXT,
    player_puuid TEXT,
    team TEXT,
    agent TEXT,
    rank INT,
    won BOOLEAN,

    kills INT,
    deaths INT,
    assists INT,
    score INT,
    damage INT,

    headshots INT,
    bodyshots INT,
    legshots INT,

    PRIMARY KEY (match_id, player_puuid),
    FOREIGN KEY (match_id) REFERENCES matches(match_id),
    FOREIGN KEY (player_puuid) REFERENCES players(player_puuid)
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

    PRIMARY KEY (match_id, round_number),
    FOREIGN KEY (match_id) REFERENCES matches(match_id)
);


-- ==========================================
-- KILL EVENTS
-- ==========================================
-- Stores every kill event in a match

CREATE TABLE kill_events (
    kill_id SERIAL PRIMARY KEY,

    match_id TEXT,
    round_number INT,
    timestamp_ms INT,

    killer_puuid TEXT,
    victim_puuid TEXT,

    killer_team TEXT,
    victim_team TEXT,

    weapon TEXT,
    headshot BOOLEAN,

    FOREIGN KEY (match_id) REFERENCES matches(match_id)
);


-- ==========================================
-- DAMAGE EVENTS
-- ==========================================
-- Stores every damage instance

CREATE TABLE damage_events (
    damage_id SERIAL PRIMARY KEY,

    match_id TEXT,
    round_number INT,

    attacker_puuid TEXT,
    receiver_puuid TEXT,

    damage INT,
    headshot INT,
    bodyshot INT,
    legshot INT,

    FOREIGN KEY (match_id) REFERENCES matches(match_id)
);


-- ==========================================
-- SESSIONS
-- ==========================================
-- A gameplay session is defined as a group
-- of matches with less than 30 minutes gap

CREATE TABLE sessions (
    session_id SERIAL PRIMARY KEY,
    player_puuid TEXT,

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
-- PLAYER WEAPON KILLS
-- ==========================================
-- Stores kills by weapon per player per match


CREATE TABLE player_weapon_kills (
    match_id TEXT,
    player_puuid TEXT,
    weapon TEXT,
    kills INT,

    damage INT,
    headshot INT,
    bodyshot INT,
    legshot INT,

    PRIMARY KEY (match_id, player_puuid, weapon)
);


