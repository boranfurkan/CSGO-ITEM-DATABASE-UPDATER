document_schema = {
    "name": str,
    "suggestedPrice": float,
    "itemCheapest": {
        "shadowpay": float,
        "csgoMarket": float,
        "csgoEmpire": float
    },
    "itemCount": {
        "shadowpay": int,
        "csgoMarket": int,
        "csgoEmpire": int,
    },
    "buff": {
        "listing": float,
        "buyOrder": float
    },
    "itemImageURI": str,
    "updatedAt": str
}