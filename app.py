from flask import Flask
import os
import json
import asyncio
from fastapi import FastAPI, Request
import uvicorn
from aiogram import F, Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    FSInputFile,
    WebAppInfo,
    Message
)


# === КОНФИГУРАЦИЯ ===
MINI_APP_URL = os.getenv("MINI_APP_HTTP")  # Должен быть URL Render-приложения!


# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Определяем маршрут для главной страницы
@app.route('/')

def get_main_reply_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🏨 Выбрать гостиницу"),
                KeyboardButton(text="📤 Отправить заявку")
            ],
            [
                KeyboardButton(text="🎫 Мои брони"),
                KeyboardButton(text="📞 Связаться с админом")
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )

#def get_webapp_reply_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📅 Забронировать номер", web_app=WebAppInfo(url=MINI_APP_URL))]
        ],
        resize_keyboard=True
    )    

# Эта часть нужна, чтобы запустить сервер, когда мы запускаем файл напрямую
if __name__ == '__main__':
    # Важный момент: host='0.0.0.0' делает сервер видимым
    # за пределами контейнера.

    app.run(host='0.0.0.0', port=5000)

