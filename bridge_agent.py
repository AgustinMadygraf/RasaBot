"""
Path: bridge_agent.py
"""

import os
import logging
import asyncio
from pathlib import Path
from telegram.ext import Updater, MessageHandler, Filters
from rasa.core.agent import Agent
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)

BASE_DIR = Path(__file__).resolve().parent
model_path = os.getenv("MODEL_PATH")
TG_TOKEN   = os.getenv("TG_TOKEN")
if not model_path:
    models_dir = BASE_DIR / "models"
    candidates = sorted(models_dir.glob("*.tar.gz"), key=lambda p: p.stat().st_mtime, reverse=True)
    model_path = str(candidates[0]) if candidates else None

if not model_path:
    raise RuntimeError("No se encontró MODEL_PATH ni modelos en ./models/*.tar.gz")

logging.info("Usando modelo: %s", model_path)
agent = Agent.load(model_path)

loop = asyncio.get_event_loop()

def handle_message(update, context):
    " Maneja los mensajes de texto del usuario y los envía a Rasa"
    user_id = str(update.effective_user.id)
    text = update.message.text or ""
    # Ejecutamos inferencia del modelo Rasa
    responses = loop.run_until_complete(agent.handle_text(text, sender_id=user_id))
    for r in responses:
        if "text" in r:
            context.bot.send_message(chat_id=update.effective_chat.id, text=r["text"])

def main():
    " Inicia el bot de Telegram y escucha mensajes"
    if not TG_TOKEN:
        raise RuntimeError("Falta TG_TOKEN en variables de entorno")
    updater = Updater(TG_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
