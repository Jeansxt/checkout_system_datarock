from deal import Deal
import json

def load_skus_from_config(file_path='sku.json'):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config

def opening_day_deals():
    # Define deals for opening day promotions
    return {
        "atv": {
            "deal": Deal.three_for_two_deal  # Apply 3 for 2 deal for Apple TVs
        },
        "ipd": {
            "deal": Deal.bulk_buy_deal,  # Bulk deal for iPads
            "args": [4, 499.99]  # Buy more than 4, price drops to 499.99
        },
        "mbp": {
            "bundle_with": "vga"  # MacBook Pro bundles with VGA adapter
        }
    }