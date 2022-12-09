import asyncio

import requests


class Empire:
    def __init__(self, CSGO_EMPIRE_KEY):
        self._dict = {}
        self.__headers = {
            "Authorization": f"Bearer {CSGO_EMPIRE_KEY}"
        }

    async def get_items(self):
        print("running empire")

        def get_last_page_info():
            return requests.get("https://csgoempire.com/api/v2/trading/items?per_page=2500&page=1&price_min=4000"
                                "&price_max=400000&price_max_above=999&sort=desc&order=market_value",
                                headers=self.__headers).json()["last_page"]

        def price_beautify(item_price):
            item_price_str = str(item_price)
            item_price_len = len(item_price_str)
            item_price_converted = f"{str(item_price_str)[:(item_price_len - 2)]}." + f"{item_price_str[item_price_len - 2:]}"
            return float(item_price_converted).__round__(2)

        for page in range(1, get_last_page_info()):
            response = requests.get(
                f"https://csgoempire.com/api/v2/trading/items?per_page=2500&page={page}&price_min=4000&"
                f"price_max=400000&price_max_above=999&sort=desc&order=market_value", headers=self.__headers).json()

            for item in response["data"]:
                item_name = item["market_name"]
                item_price = price_beautify(item["market_value"])
                if item_name in self._dict:
                    self._dict[item_name]["count"] += 1
                    if self._dict[item_name]["price"] > item_price:
                        self._dict[item_name]["price"] = item_price
                else:
                    self._dict[item_name] = {}
                    self._dict[item_name]["price"] = item_price
                    self._dict[item_name]["count"] = 1
        await asyncio.sleep(0.5)
        return self._dict

    def set_empty_dict(self):
        self._dict = {}
