import asyncio
import requests


class Hellcase:
    def __init__(self):
        self._dict = {}

    async def get_items(self):
        print("Running Hellcase")

        def get_last_page_info(starttrak: bool):
            if not starttrak:
                count = requests.get("https://api.hellcase.com/item?exterior=&item_type=&range_from=30&range_to=3000"
                                     "&rarity=&search=&per_page=100&stattrak=0&sort=desc&gameTab=csgo&offset=0&game"
                                     "=csgo").json()["count"]
                last_page = (count / 100).__ceil__()
                return last_page

            else:
                count = requests.get("https://api.hellcase.com/item?exterior=&item_type=&range_from=30&range_to=3000"
                                     "&rarity=&search=&per_page=100&stattrak=1&sort=desc&gameTab=csgo&offset=0&game"
                                     "=csgo").json()["count"]
                last_page = (count / 100).__ceil__()
                return last_page

        for page in range(0, get_last_page_info(starttrak=False)):
            offset = page * 100
            response = requests.get(f"https://api.hellcase.com/item?exterior=&item_type=&range_from=30&range_to=3000"
                                    f"&rarity=&search=&per_page=100&stattrak=0&sort=desc&gameTab=csgo&offset={offset}"
                                    f"&game=csgo").json()
            for item in response["items"]:
                item_name = item["steam_market_hash_name"]
                price = item["steam_price_en"]
                self._dict[item_name] = price
            await asyncio.sleep(0.2)

        for page in range(0, get_last_page_info(starttrak=True)):
            offset = page * 100
            response = requests.get(f"https://api.hellcase.com/item?exterior=&item_type=&range_from=30&range_to=3000"
                                    f"&rarity=&search=&per_page=100&stattrak=1&sort=desc&gameTab=csgo&offset={offset}"
                                    f"&game=csgo").json()
            for item in response["items"]:
                item_name = item["steam_market_hash_name"]
                price = item["steam_price_en"]
                self._dict[item_name] = price
            await asyncio.sleep(0.15)

    def get_dict(self):
        return self._dict

    def set_empty_dict(self):
        self._dict = {}
