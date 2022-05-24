# C2-leaderboard

This repository contains the leaderboard application for [C2](https://github.com/winstxnhdw/C2). There are two variations to the leaderboard.

## Serverless

Hosted on Heroku. Extremely portable.

### Installation

The installation script only supports Arch or Ubuntu. If you are on any other platform, you will have to install Docker manually [here](https://docs.docker.com/get-docker/).

```bash
sh requirements.sh
```

### Development

```bash
sh launch.sh
```

## Local

During the event, internet access will be unavailable. The leaderboard has to run locally on a Windows 10 system.

### Requirements

- Windows 10/11
- [Docker Installer](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe)

### Install

Install Docker

```ps1
.\requirements_docker.bat
```

## Environment Variables

Ensure that you set the following environment variable in a `.env` file within the root of this repository.

```yaml
POSTGRES_PASSWORD=<POSTGRES_PASSWORD>
POSTGRES_USER=<POSTGRES_USER>
POSTGRES_DB=<POSTGRES_DB>
SECRET_KEY=<SECRET_KEY>
```
