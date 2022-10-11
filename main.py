import random
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from config import bot, dp
import logging
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(f'Приветствую {message.from_user.full_name}')
@dp.message_handler(commands=['mem'])
async def mem_command(message: types.Message):
    mem_photo = open("media/mem-3.jpg", "rb")
    number = random.randint(1, 4)
    if number == 1:
        mem_photo = open("media/mem-1.jpg", "rb")
    if number == 2:
        mem_photo = open("media/mem-2.jpg", "rb")
    await bot.send_photo(message.chat.id, mem_photo)
@dp.message_handler(commands=["quiz"])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("След.", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Сколько областей есть в Кыргызстане?"
    answers = [
        '2',
        '7',
        '12',
        '8',
        '5',
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="",
        open_period=30,
        reply_markup=markup
    )
@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    question = "Сколько будет 200-20?"
    answers = [
        "130",
        "180",
        "-180",
        "170"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="",
        open_period=10
    )
@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await message.answer(int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)