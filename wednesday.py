import asyncio

import aioschedule

from commands import smoke, lunch_start, lunch_end, go_home


async def wednesday():
    aioschedule.every().wednesday.at('9:10').do(smoke)
    aioschedule.every().wednesday.at("10:10").do(smoke)
    aioschedule.every().wednesday.at("11:20").do(smoke)
    aioschedule.every().wednesday.at("12:30").do(smoke)
    aioschedule.every().wednesday.at("13:00").do(lunch_start)
    aioschedule.every().wednesday.at("13:30").do(lunch_end)
    aioschedule.every().wednesday.at("14:45").do(smoke)
    aioschedule.every().wednesday.at("15:50").do(smoke)
    aioschedule.every().wednesday.at("17:00").do(smoke)
    aioschedule.every().wednesday.at("17:45").do(go_home)
