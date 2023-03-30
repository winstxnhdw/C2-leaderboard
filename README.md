# C2-leaderboard

During the event, internet access will be unavailable. The leaderboard has to run locally on a Windows 10 system.

## Requirements

You will need to install Docker Desktop for Windows 10 before you can run the following batch script.

- Windows 10/11
- [Docker Installer](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe)

## Installation

Install Docker and select the WSL 2 backend.

> **Warning**: If you use Hyper-V, you may run into a file sharing permission issue that will cause the database to crash.

```ps1
.\requirements_docker.bat
```

Pull and save `postgres:alpine` image.

```ps1
docker pull postgres:alpine
docker save --output bin\postgres-alpine.tar postgres:alpine
```

Build and save the leaderboard image.

```ps1
.\build.bat
```

Ensure that you set the following environment variable in a `.env` file within the root of this repository.

```bash
echo POSTGRES_PASSWORD=YOUR_POSTGRES_PASSWORD >> .env
echo POSTGRES_USER=YOUR_POSTGRES_USER >> .env
echo POSTGRES_DB=YOUR_POSTGRES_DB >> .env
echo SECRET_KEY=YOUR_SECRET_KEY >> .env
```

## Usage

Destroys any existing Docker containers and launches the leaderboard containers.

```ps1
.\launch.bat
```
