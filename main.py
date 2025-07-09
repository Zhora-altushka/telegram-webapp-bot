import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(
        text="📋 Записаться",
        web_app=WebAppInfo(url="https://zhora-altushka.github.io/booking-webapp-form/")
    ))
    await message.answer("Добро пожаловать! Нажмите кнопку ниже, чтобы заполнить анкету:", reply_markup=keyboard)

@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def webapp_data_handler(message: types.Message):
    data = message.web_app_data.data
    await message.answer("✅ Вы успешно записались! Спасибо 😊")
    await bot.send_message(ADMIN_ID, f"📬 Новая заявка:

{data}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)