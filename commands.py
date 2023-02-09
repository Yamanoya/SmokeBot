from aiogram import Bot, Dispatcher

BOT_TOKEN = '5635299388:AAF6umyajuGVMZYgIKo9HbH6cKJRtnD0I64'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


async def lunch_start():
    await bot.send_message(chat_id=-877920808, text="🍔🚬СЕЙЧАС НУЖНО ИДТИ КУШАЦ И КУРИТЬ🍔🚬")


async def lunch_end():
    await bot.send_message(chat_id=-877920808, text="🔴🖥ПОРА РАБОТАТЬ, НАДЕЮСЬ ТЫ УЖЕ ЗА КОМПЬЮТЕРОМ🖥🔴")


async def smoke():
    await bot.send_message(chat_id=-877920808, text="🚬🚬ПЕРЕКУР ДАМЫ И ГОСПОДА🚬🚬")


async def go_home():
    audio = open("C:\TimeToSmokeBot\OKLETSGO.mp3", "rb")
    await bot.send_audio(chat_id=-877920808, audio=audio, caption='OKAAYYYYY LETS GOOOOOO')
    audio.close()
