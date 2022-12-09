import requests


class Market:
    def __init__(self):
        self.URI = "https://market.csgo.com/api/v2/prices/USD.json"
        self._dict = {}

    async def get_items(self):
        print("running market")
        response = requests.get(self.URI).json()
        for item in response["items"]:
            item_name = item["market_hash_name"]
            item_count = int(item["volume"])
            item_price = float(item["price"]).__round__(2)

            self._dict[item_name] = {}
            self._dict[item_name]["price"] = item_price
            self._dict[item_name]["count"] = item_count
        return self._dict

    def get_dict(self):
        return self._dict

    def set_empty_dict(self):
        self._dict = {}