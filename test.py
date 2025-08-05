"""
Path: test.py
"""
import os
from pathlib import Path
import sys
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
model_path = os.getenv("MODEL_PATH")
if not model_path or not os.path.isfile(model_path):
    print(f"[ERROR] Modelo no encontrado. MODEL_PATH='{model_path}'", file=sys.stderr)
    models_dir = BASE_DIR / "models"
    candidates = sorted(models_dir.glob("*.tar.gz"), key=lambda p: p.stat().st_mtime, reverse=True)
    model_path = str(candidates[0]) if candidates else None
print(f"Modelo encontrado: {model_path}")


TG_TOKEN = os.getenv("TG_TOKEN")

if not TG_TOKEN:
    print(f"[ERROR] Token de Telegram no encontrado. TG_TOKEN='{TG_TOKEN}'", file=sys.stderr)
    sys.exit(1)

print(f"Token de Telegram: {TG_TOKEN}")
