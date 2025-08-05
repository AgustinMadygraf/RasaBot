#!/bin/bash
set -euo pipefail
cd ~/RasaBot
source .venv/bin/activate
exec python -u run.py
