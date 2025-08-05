"""
Path: bridge_telegram_rasa.py
"""

import os
import logging
import requests
from telegram.ext import Updater, MessageHandler, Filters

TELEGRAM_TOKEN = os.getenv("TG_TOKEN")
if not TELEGRAM_TOKEN:
    raise ValueError("La variable de entorno TG_TOKEN no está definida.")

RASA_REST_URL = os.getenv("RASA_REST_URL")
if not RASA_REST_URL:
    raise ValueError("La variable de entorno RASA_REST_URL no está definida.")


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

def handle_message(update, _context):
    " Maneja los mensajes de texto del usuario y los envía a Rasa"
    user_id = str(update.effective_user.id)
    text = update.message.text or ""
    try:
        r = requests.post(RASA_REST_URL, json={"sender": user_id, "message": text}, timeout=10)
        r.raise_for_status()
        for msg in r.json():
            if "text" in msg:
                update.message.reply_text(msg["text"])
    except requests.exceptions.RequestException:
        logging.exception("Error llamando a Rasa")
        update.message.reply_text("Ups, hubo un problema hablando con el motor.")

def main():
    " Inicia el bot de Telegram y escucha mensajes"
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
