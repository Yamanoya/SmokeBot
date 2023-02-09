from aiogram.utils import executor

from commands import dp
from on_startup import on_startup

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
