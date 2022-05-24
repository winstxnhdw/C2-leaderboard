@echo off

set app_name=leaderboard-app

docker-compose down

docker load --input bin\postgres-alpine.tar
docker load --input bin\leaderboard-app.tar

docker-compose up -d