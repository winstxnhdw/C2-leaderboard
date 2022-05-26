@echo off

set app_name=leaderboard-app
set port=5000

docker-compose rm -f -s -v

docker load --input bin\postgres-alpine.tar
docker load --input bin\leaderboard-app.tar

docker-compose up -d
start http://localhost:%port%

docker-compose logs -f -t
