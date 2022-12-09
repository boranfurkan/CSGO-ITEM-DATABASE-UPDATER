import asyncio
import os
import time
from dotenv import load_dotenv, find_dotenv
from buff import Buff
from csgoempire import Empire
from csgomarket import Market
from hellcase import Hellcase
from shadowpay import Shadow
from shadowpay_all_items import ShadowAll

load_dotenv(find_dotenv())
SHADOWPAY_USER_TOKEN = os.environ.get("SHADOWPAY_USER_TOKEN")
PRICE_EMPIRE_TOKEN = os.environ.get("PRICE_EMPIRE_TOKEN")
CSGO_EMPIRE_TOKEN = os.environ.get("CSGO_EMPIRE_TOKEN")

buff, csgo_empire, csgo_market, hellcase, shadowpay, shadowpay_all_items = \
    Buff(PRICE_EMPIRE_TOKEN), Empire(CSGO_EMPIRE_TOKEN), Market(), Hellcase(), Shadow(SHADOWPAY_USER_TOKEN), ShadowAll(
        SHADOWPAY_USER_TOKEN)


async def get_all_items():
    print(f"started at {time.strftime('%X')}")
    task1 = asyncio.create_task(buff.get_items())
    task2 = asyncio.create_task(csgo_empire.get_items())
    task3 = asyncio.create_task(csgo_market.get_items())
    task4 = asyncio.create_task(hellcase.get_items())
    task5 = asyncio.create_task(shadowpay.get_items())
    task6 = asyncio.create_task(shadowpay_all_items.get_items())
    await asyncio.gather(task1, task2, task3, task4, task5, task6)
    print(f"finished at {time.strftime('%X')}")


asyncio.run(get_all_items())