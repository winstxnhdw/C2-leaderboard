@echo off

set app_name=leaderboard-app

docker load --input bin\postgres-alpine.tar
docker load --input bin\leaderboard-app.tar

docker-compose down
docker-compose up -d