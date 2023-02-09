import asyncio

import aioschedule

from commands import smoke, lunch_start, lunch_end, go_home


async def friday():
    aioschedule.every().friday.at('9:10').do(smoke)
    aioschedule.every().friday.at("10:10").do(smoke)
    aioschedule.every().friday.at("11:20").do(smoke)
    aioschedule.every().friday.at("12:30").do(smoke)
    aioschedule.every().friday.at("13:00").do(lunch_start)
    aioschedule.every().friday.at("13:30").do(lunch_end)
    aioschedule.every().friday.at("14:45").do(smoke)
    aioschedule.every().friday.at("15:50").do(smoke)
    aioschedule.every().friday.at("16:30").do(go_home)
