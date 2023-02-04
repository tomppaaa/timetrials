CREATE TABLE IF NOT EXIXST users (
  id int primary key,
  name varchar(80),
  password varchar(80),
);

CREATE TABLE IF NOT EXIST games (
  id int primary key,
  name varchar(80),
);

CREATE TABLE IF NOT EXIST courses (
  id int primary key,
  name varchar(80),
  game_id int references games(id),
);

CREATE TABLE IF NOT EXIST standards (
  id int primary key,
  name varchar(50),
  tier varchar(3),
  points numeric,
  game_id int references games(id),
  course_id int references courses(id),
);

CREATE TABLE IF NOT EXIST times (
  id int primary key,
  game_id int references games(id),
  course_id int references courses(id),
  timems varchar(80),
  date date,
);
