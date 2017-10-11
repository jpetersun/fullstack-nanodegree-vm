-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here, test.

create table players (
  name varchar(20) not null,
  wins integer default 0,
  matches integer default 0,
  id serial primary key
);

create table matches (
  winner text not null,
  loser text not null
);
