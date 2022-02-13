# ReadBarcodeBot ver 0.1
# Телеграм-бот для распознавания штрихкода: t.me/ReadBarcodeBot

from aiogram import Bot, Dispatcher, executor, types  # основной aiogram
import tokens  # содержит токен (имя 'token' нельзя использовать)
import func    # мой модуль, функции


###################################################################################################
# Инициальзация бота
###################################################################################################
# Модкль token.py содержит две строки:
# readBarcodeBot_token = 'тут токен'
# test_token = 'тут токен'
# При разработке использеум test, для работы readBarcodeBot.
# в git его игнорируем, а в место пушим зашифрованный архив.
API_TOKEN = tokens.readBarcodeBot_token # рабочий бот
# API_TOKEN = tokens.test_token # тестовый бот


# Инициализация бота
# storage = MemoryStorage() # место хранения контекста в ОЗУ
bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot, storage=storage)
dp = Dispatcher(bot)


###################################################################################################
# Перехват сообщений
###################################################################################################
@dp.message_handler()
async def send_welcome(message: types.Message):
    """Отвечает на любые текстовые сообщения."""
    await message.answer('Отправь мне фотку со штрих-кодом.')


@dp.message_handler(content_types=['photo'])
async def send_welcome(message: types.Message):
    """Отвечает на любые фото сообщения."""
    await message.answer('Сейчас попробую распознать.')
    await message.photo[-1].download('img.jpg')
    mes = func.img_decode()
    await message.answer(mes)
###################################################################################################


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)