
-- ==========================================
-- PERIOD TYPE 
-- ==========================================
--  Recap period

CREATE TABLE dim_periods (
    period_type TEXT,   -- act, episode, year
    period_id TEXT,

    start_date DATE,
    end_date DATE,

    episode_id TEXT,
    act_id TEXT,
    year INT,
    month INT,         -- is this needed?
    last_updated TIMESTAMP,
    
    PRIMARY KEY (period_type, period_id)

);


-- ==========================================
-- RANKS
-- ==========================================

CREATE TABLE dim_ranks (
    rank_name TEXT PRIMARY KEY,
    rank_value INT
);

INSERT INTO dim_ranks VALUES
('Iron 1', 1),
('Iron 2', 2),
('Iron 3', 3),
('Bronze 1', 4),
('Bronze 2', 5),
('Bronze 3', 6),
('Silver 1', 7),
('Silver 2', 8),
('Silver 3', 9),
('Gold 1', 10),
('Gold 2', 11),
('Gold 3', 12),
('Platinum 1', 13),
('Platinum 2', 14),
('Platinum 3', 15),
('Diamond 1', 16),
('Diamond 2', 17),
('Diamond 3', 18),
('Ascendant 1', 19),
('Ascendant 2', 20),
('Ascendant 3', 21),
('Immortal 1', 22),
('Immortal 2', 23),
('Immortal 3', 24),
('Radiant', 25);
