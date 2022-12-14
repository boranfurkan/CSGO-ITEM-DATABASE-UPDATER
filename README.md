# CSGO-ITEM-DATABASE-UPDATER
- Real time price updater for CSGO item database.
- Price comparison bot for most CSGO marketplaces.

#### Swagger UI
- Documentation can be found in "https://csgo-items--api.herokuapp.com/api-docs/"

#### Setup

```bash
pip install -r requirements.txt && python3 main.py
```

#### Environment Variables

- MONGO_URI // Mongodb atlas connection url. (CAN BE CREATED FREE)
- DATABASE_NAME // Database name in connected cluster.
- COLLECTION_NAME // Collection name in connected database.
- PRICE_EMPIRE_TOKEN // "https://pricempire.com" api token. (PAID)
- SHADOWPAY_USER_TOKEN // "https://shadowpay.com" user api token. (FREE)
- CSGO_EMPIRE_TOKEN // "https://csgoempire.com" api token. (FREE)