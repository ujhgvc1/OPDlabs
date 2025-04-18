import logging
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
# Токен бота
API_TOKEN = '8186309192:AAG66mRrPY8slxt9fpZVZFaE9xeAHfiDjwU'
# Настройка логирования
logging.basicConfig(level=logging.INFO)
# Создаем объект бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# Словарь для хранения данных о пользователях
users_data = {}
# Команда /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Привет! Я помогу записать тебя на марафон. Напиши свое ФИО.")
# Обработка введенного ФИО
@dp.message_handler(lambda message: len(message.text.split()) >= 2)
async def process_fio(message: types.Message):
    # Сохраняем ФИО пользователя
    users_data[message.from_user.id] = {"fio": message.text}
    await message.reply("Отлично, теперь выбери тип забега: 5 км, 10 км, или марафон (42 км).")
# Обработка типа забега
@dp.message_handler(lambda message: message.text.lower() in ['5 км', '10 км', 'марафон'])
async def process_race_type(message: types.Message):
    user_id = message.from_user.id
    if user_id in users_data:
        # Сохраняем тип забега
        users_data[user_id]["race_type"] = message.text
        fio = users_data[user_id]["fio"]
        race_type = users_data[user_id]["race_type"]
        await message.reply(f"Спасибо, {fio}. Ты записан на забег: {race_type}.")
# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
