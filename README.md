# C2-leaderboard

During the event, internet access will be unavailable. The leaderboard has to run locally on a Windows 10 system.

## Requirements

You will need to install Docker Desktop for Windows 10 before you can run the following batch script.

- Windows 10/11
- [Docker Installer](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe)

## Installation

Install Docker. Select the WSL 2 backend.

> If you use Hyper-V, you may run into a file sharing permission issue that will cause the database to crash.

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

```yaml
POSTGRES_PASSWORD=<POSTGRES_PASSWORD>
POSTGRES_USER=<POSTGRES_USER>
POSTGRES_DB=<POSTGRES_DB>
SECRET_KEY=<SECRET_KEY>
```

## Usage

```ps1
.\launch.bat
```
