import asyncio
import os
import time
from dotenv import load_dotenv, find_dotenv
from .buff import Buff
from .csgoempire import Empire
from .csgomarket import Market
from .hellcase import Hellcase
from .shadowpay import Shadow
from .shadowpay_all_items import ShadowAll
from db.schema import fill_schema

load_dotenv(find_dotenv())
SHADOWPAY_USER_TOKEN = os.environ.get("SHADOWPAY_USER_TOKEN")
PRICE_EMPIRE_TOKEN = os.environ.get("PRICE_EMPIRE_TOKEN")
CSGO_EMPIRE_TOKEN = os.environ.get("CSGO_EMPIRE_TOKEN")

buff, csgo_empire, csgo_market, hellcase, shadowpay, shadowpay_all = \
    Buff(PRICE_EMPIRE_TOKEN), Empire(CSGO_EMPIRE_TOKEN), Market(), Hellcase(), Shadow(SHADOWPAY_USER_TOKEN), ShadowAll(
        SHADOWPAY_USER_TOKEN)


async def get_all_items():
    all_schemas = []
    print(f"started at {time.strftime('%X')}")
    task1 = asyncio.create_task(buff.get_items())
    task2 = asyncio.create_task(csgo_empire.get_items())
    task3 = asyncio.create_task(csgo_market.get_items())
    task4 = asyncio.create_task(hellcase.get_items())
    task5 = asyncio.create_task(shadowpay.get_items())
    task6 = asyncio.create_task(shadowpay_all.get_items())
    await asyncio.gather(task1, task2, task3, task4, task5, task6)
    print(f"finished at {time.strftime('%X')}")
    buff_items = task1.result()
    csgo_empire_items = task2.result()
    csgo_market_items = task3.result()
    hellcase_items = task4.result()
    shadowpay_items = task5.result()
    shadowpay_all_items = task6.result()

    intersection = set.intersection(set(buff_items.keys()), set(hellcase_items.keys()), set(shadowpay_all_items.keys()))
    for item in intersection:
        item_name = item
        hellcase_suggested = hellcase_items[item_name]
        shadow_suggested = shadowpay_all_items[item_name]["suggested_price"]

        if item_name in shadowpay_items:
            shadowpay_cheapest = shadowpay_items[item_name]["price"]
            shadowpay_count = shadowpay_items[item_name]["count"]
        else:
            shadowpay_cheapest = ""
            shadowpay_count = ""

        if item_name in csgo_market_items:
            csgo_market_cheapest = csgo_market_items[item_name]["price"]
            csgo_market_count = csgo_market_items[item_name]["count"]
        else:
            csgo_market_cheapest = ""
            csgo_market_count = ""

        if item_name in csgo_empire_items:
            csgo_empire_cheapest = csgo_empire_items[item_name]["price"]
            csgo_empire_count = csgo_empire_items[item_name]["count"]
        else:
            csgo_empire_cheapest = ""
            csgo_empire_count = ""

        listing = buff_items[item_name]["buff163"]
        listing7 = buff_items[item_name]["buff163_avg7"]
        listing30 = buff_items[item_name]["buff163_avg30"]
        listing60 = buff_items[item_name]["buff163_avg60"]
        listing90 = buff_items[item_name]["buff163_avg90"]
        buy_order = buff_items[item_name]["buff163_quick"]
        item_image_url = shadowpay_all_items[item_name]["icon"]

        new_schema = fill_schema(
            name=item_name,
            hellcaseSuggested=hellcase_suggested,
            shadowSuggested=shadow_suggested,
            shadowpay=shadowpay_cheapest,
            csgoMarket=csgo_market_cheapest,
            csgoEmpire=csgo_empire_cheapest,
            shadowCount=shadowpay_count,
            csgoMarketCount=csgo_market_count,
            csgoEmpireCount=csgo_empire_count,
            listing=listing,
            listing7=listing7,
            listing30=listing30,
            listing60=listing60,
            listing90=listing90,
            buyOrder=buy_order,
            itemImageURI=item_image_url)

        all_schemas.append(new_schema)
    return all_schemas
