# Tsoha-project

## Forum

The subject of the project is a forum. Just a simple forum that one can log into and make/view posts and commend etc.
Sike, we are doing a database for time trial-times in video games.
The main functionality is that one can add times to specific games and/or tracks and get a rank based on those
times (see https://www.mariokart64.com/mkdd/standardc.php)

## Database

The database will be PostgreSQL-based database hosted on fly.io.

### Tables (at least)
* users
* games
* tracks
* standards
* times

### Fancier db things
* authenticated user can add times and edit old ones
* other boring user/account things, can login
* can sort times by game, track, time and other things

## Deployment

The site is being deployed at https://tsoha-flask.fly.dev/

### GET https://tsoha-flask.fly.dev/
Just to test if the site works

### GET https://tsoha-flask.fly.dev/db
[Just](Just) to test if the db works (cue applause)
