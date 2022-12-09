import datetime


def fill_schema(name: str, hellcaseSuggested: float, shadowSuggested: float, shadowpay: float, csgoMarket: float,
                csgoEmpire: float, shadowCount: int, csgoMarketCount: int, csgoEmpireCount: int, listing: float,
                listing7: float, listing30: float, listing60: float, listing90: float,
                buyOrder: float, itemImageURI: str):
    document_schema = {
        "name": name,
        "suggestedPrice": {
            "hellcase": hellcaseSuggested,
            "shadowpay": shadowSuggested
        },
        "itemCheapest": {
            "shadowpay": shadowpay,
            "csgoMarket": csgoMarket,
            "csgoEmpire": csgoEmpire
        },
        "itemCount": {
            "shadowpay": shadowCount,
            "csgoMarket": csgoMarketCount,
            "csgoEmpire": csgoEmpireCount,
        },
        "buff": {
            "listing": listing,
            "listing7": listing7,
            "listing30": listing30,
            "listing60": listing60,
            "listing90": listing90,
            "buyOrder": buyOrder
        },
        "itemImageURI": itemImageURI,
        "updatedAt": datetime.datetime.now()
    }
