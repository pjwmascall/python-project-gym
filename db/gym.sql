-- createdb gym
-- psql -d gym -f db/gym.sql

DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS gym_classes;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    home_address VARCHAR(255),
    membership_type VARCHAR(255),
    is_active BOOLEAN
);

CREATE TABLE gym_classes (
    id SERIAL PRIMARY KEY,
    class_name VARCHAR(255),
    instructor VARCHAR(255),
    room VARCHAR(255),
    capacity INT,
    class_date DATE,
    class_start TIME,
    class_end TIME,
    is_active BOOLEAN
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    class_id INT REFERENCES gym_classes(id) ON DELETE CASCADE,
    attended BOOLEAN
);