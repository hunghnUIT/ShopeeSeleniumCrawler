# import motor.motor_asyncio
import pymongo

client = pymongo.MongoClient(
    "mongodb://localhost:27017", serverSelectionTimeoutMS=10000
    )

try:
    info = client.server_info()
    db_shopee = client['SHOPEE']
    col_item = db_shopee['ItemsShopee']
    col_item_price = db_shopee['ItemPriceShopee']
    col_category = db_shopee['CategoriesShopee']
    db_user = client['USER']
    col_tracked_item = db_user['TrackedItemsShopee']
    db_server = client['SERVER']
    col_config = db_server['Configs']
except Exception:
    print("Unable to connect to the server.")