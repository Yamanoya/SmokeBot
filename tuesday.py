import asyncio

import aioschedule

from commands import smoke, lunch_start, lunch_end, go_home


async def tuesday():
    aioschedule.every().tuesday.at('9:10').do(smoke)
    aioschedule.every().tuesday.at("10:10").do(smoke)
    aioschedule.every().tuesday.at("11:20").do(smoke)
    aioschedule.every().tuesday.at("12:30").do(smoke)
    aioschedule.every().tuesday.at("13:00").do(lunch_start)
    aioschedule.every().tuesday.at("13:30").do(lunch_end)
    aioschedule.every().tuesday.at("14:45").do(smoke)
    aioschedule.every().tuesday.at("15:50").do(smoke)
    aioschedule.every().tuesday.at("17:00").do(smoke)
    aioschedule.every().tuesday.at("17:45").do(go_home)

