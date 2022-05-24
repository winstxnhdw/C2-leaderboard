@echo off

set app_name=leaderboard-app

docker-compose down
docker rm %app_name%
docker build -t %app_name% .
docker save --output bin\%app_name%.tar %app_name%