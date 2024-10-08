## Configuration env
```bash
cp .env.example .env
```
## Virtualenv
```bash
python3 -m venv .venv     # Create virtualenv
source .venv/bin/activate # Activate virtualenv
```
## Build container
```bash
docker-compose up -d
```
## Create network
```bash
docker network create traefik_network
```
## Commands
```bash
pylint .
ENV=test pytest
alembic revision --autogenerate -m "create users table"
alembic upgrade head
```
