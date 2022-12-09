import requests


class Shadow:
    def __init__(self, SHADOWPAY_USER_TOKEN):
        self.URI = f"https://api.shadowpay.com/api/v2/user/items/prices?token={SHADOWPAY_USER_TOKEN}"
        self._dict = {}

    async def get_items(self):
        print("running shadowpay")
        response = requests.get(self.URI).json()
        for item in response["data"]:
            item_name = item["steam_market_hash_name"]
            item_price = float(item["price"])
            item_count = int(item["volume"])

            self._dict[item_name] = {}
            self._dict[item_name]["price"] = item_price
            self._dict[item_name]["count"] = item_count

    def get_dict(self):
        return self._dict

    def set_empty_dict(self):
        self._dict = {}
