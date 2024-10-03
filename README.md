## Configuration env
```bash
cp .env.example .env
```
## Virtualenv
```bash
python3 -m venv .venv     # Create virtualenv
source .venv/bin/activate # Activate virtualenv
```
## Install
```bash
pip install -r requirements.txt
```
## Update requirements
```bash
pip freeze > requirements.txt
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
pylint app/ tests/
coverage report
alembic revision --autogenerate -m "create users table"
alembic upgrade head
```