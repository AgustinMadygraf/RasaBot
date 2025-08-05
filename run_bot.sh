#!/bin/bash
cd /home/agustinmadygraf/RasaBot
# cargar variables del .env
if [ -f .env ]; then
  set -a; . ./.env; set +a
fi
exec /home/agustinmadygraf/RasaBot/.venv/bin/python -u /home/agustinmadygraf/RasaBot/run.py
