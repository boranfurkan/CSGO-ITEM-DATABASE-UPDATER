import gspread


def connect_spreadsheet():
    service_account = gspread.service_account(filename="../hellcase_keys.json")
    sheet = service_account.open("Hellcase Data")
    worksheet = sheet.worksheet("Sheet1")
    return worksheet.get_all_records()


class Hellcase:
    def __init__(self):
        self._dict = {}

    async def get_items(self):
        print("running hellcase")
        for item in connect_spreadsheet():
            item_name = item["ITEM"]
            item_price = item["PRICE"]
            self._dict[item_name] = item_price

    def get_dict(self):
        return self._dict

    def set_empty_dict(self):
        self._dict = {}
