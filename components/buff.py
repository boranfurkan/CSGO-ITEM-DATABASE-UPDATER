import requests


class Buff:
    def __init__(self, PRICE_EMPIRE_TOKEN):
        self._dict = {}
        self._URI = f"https://api.pricempire.com/v2/getAllItems?token={PRICE_EMPIRE_TOKEN}&source=buff163," \
                    "buff163_quick,buff163,buff163_avg7,buff163_avg30,buff163_avg60,buff163_avg90&currency=USD"
        self.__base_attributes = ["buff163", "buff163_avg7", "buff163_avg30", "buff163_avg60", "buff163_avg90",
                                  "buff163_quick"]

    async def get_items(self):
        print("running buff")

        def price_beautify(item_price):
            item_price_str = str(item_price)
            item_price_len = len(item_price_str)
            item_price_converted = f"{str(item_price_str)[:(item_price_len - 2)]}." + f"{item_price_str[item_price_len - 2:]}"
            return float(item_price_converted).__round__(2)

        response = requests.get(self._URI).json()
        for name, response_attr in response.items():
            item_name = name
            self._dict[item_name] = {}
            difference = self.get_difference(response_attr)
            for attr in self.__base_attributes:
                if attr not in difference:
                    self._dict[item_name][attr] = price_beautify(response_attr[attr])
                else:
                    self._dict[item_name][attr] = 0
        return self._dict

    def get_dict(self):
        return self._dict

    def get_url(self):
        return self._URI

    def get_base_attributes(self):
        return self.__base_attributes

    def get_difference(self, item_dict):
        return list(set(self.__base_attributes) - set(list(item_dict.keys())))

    def set_empty_dict(self):
        self._dict = {}