"""
Path: run_rasa.py
"""

import asyncio
import sys
from rasa.__main__ import main

# Workaround para Windows: usar SelectorEventLoop en lugar de Proactor
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Ejecuta como: rasa run --enable-api --cors "*"
sys.argv = ["rasa", "run", "--enable-api", "--cors", "*"]
if __name__ == "__main__":
    main()
