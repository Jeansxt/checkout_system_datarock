
# Initialize checkout system with pricing rules and opening day deals
from deal_controller import opening_day_deals
from checkout import Checkout
checkout = Checkout(opening_day_deals())

# # Simulate scanning items
# checkout.scan("atv", 3)  # 3 Apple TVs
# checkout.scan("ipd", 5)  # 5 Super iPads
# checkout.scan("mbp", 2)  # 2 MacBook Pros
# checkout.scan("vga", 3)  # 3 VGA Adapters

# checkout.scan("atv")
# checkout.scan("ipd")
# checkout.scan("ipd")
# checkout.scan("atv")
# checkout.scan("ipd")
# checkout.scan("ipd")
# checkout.scan("ipd")

checkout.scan("mbp")
checkout.scan("vga")
checkout.scan("ipd")

item_summary, total_price = checkout.total()

print("Item Summary:")
for item, quantity in item_summary.items():
    print(f"{item}: Quantity = {quantity}")

print(f"Total Price: ${total_price:.2f}")
