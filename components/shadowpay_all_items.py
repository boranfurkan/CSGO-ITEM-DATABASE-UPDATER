import requests


class ShadowAll:
    def __init__(self, SHADOWPAY_USER_TOKEN):
        self.URI = f"https://api.shadowpay.com/api/v2/user/items/steam?token={SHADOWPAY_USER_TOKEN}"
        self._dict = {}

    async def get_items(self):
        print("running shadowall")
        response = requests.get(self.URI).json()
        for item in response["data"]:
            item_name = item["steam_market_hash_name"]
            suggested_price = float(item["suggested_price"])
            icon = item["icon"]
            if suggested_price > 35:
                if item_name[:7] != "Sticker":
                    self._dict[item_name] = {}
                    self._dict[item_name]["suggested_price"] = suggested_price
                    self._dict[item_name]["icon"] = icon
        return self._dict

    def get_dict(self):
        return self._dict

    def set_empty_dict(self):
        self._dict = {}
