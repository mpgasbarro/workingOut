-- settings.sql
CREATE DATABASE workout;
CREATE USER workoutuser WITH PASSWORD 'workout';
GRANT ALL PRIVILEGES ON DATABASE workout TO workoutuser;