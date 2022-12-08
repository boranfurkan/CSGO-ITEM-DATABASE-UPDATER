import requests


class Empire:
    def __init__(self):
        self.dict = {}
        self.checker()

    def checker(self):
        for page in range(1, 10):
            response = requests.get(
                f"https://csgoempire.gg/api/v2/trading/items?per_page=2500&page={page}&price_min=5000&price_max=300000&price_max_above=9999&sort=asc&order=market_value",
                headers=headers).json()

            for item in response["data"]:
                item_name = item["market_name"]
                item_price = item["market_value"]

                if len(str(item_price)) == 4:
                    item_price = f"{str(item_price)[:2]}." + f"{str(item_price)[2:]}"
                elif len(str(item_price)) == 5:
                    item_price = f"{str(item_price)[:3]}." + f"{str(item_price)[3:]}"
                elif len(str(item_price)) == 6:
                    item_price = f"{str(item_price)[:4]}." + f"{str(item_price)[4:]}"
                item_price = float(item_price).__round__(2)

                if item_name in self.dict:
                    self.dict[item_name]["count"] += 1
                    if self.dict[item_name]["price"] > item_price:
                        self.dict[item_name]["price"] = item_price
                else:
                    self.dict[item_name] = {}
                    self.dict[item_name]["price"] = item_price
                    self.dict[item_name]["count"] = 1