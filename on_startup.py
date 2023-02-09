import asyncio

import aioschedule

from friday import friday
from monday import monday
from thursday import thursday
from tuesday import tuesday
from wednesday import wednesday


async def on_startup(_):
    await asyncio.create_task(monday())
    await asyncio.create_task(tuesday())
    await asyncio.create_task(wednesday())
    await asyncio.create_task(thursday())
    await asyncio.create_task(friday())
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)