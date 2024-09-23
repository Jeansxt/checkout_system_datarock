
class Checkout:
    def __init__(self, deal_rules=None):
        # Pricing rules passed in during initialization (dynamic deals)
        from deal_controller import  load_skus_from_config
        self.pricing_rules = load_skus_from_config()
        self.deal_rules = deal_rules or {}  # Optional: deal rules (can be opening day or future deals)
        self.scanned_items = {}

    def scan(self, item, quantity=1):
        # Add item and its quantity to the scanned items dictionary
        if item in self.scanned_items:
            self.scanned_items[item] += quantity
        else:
            self.scanned_items[item] = quantity

    def total(self):
        from deal import Deal
        total_price = 0
        item_summary = {}

        # First, handle bundles to avoid double-counting
        for item, quantity in self.scanned_items.items():
            # Check if this item has a bundle deal defined in the deal rules
            if item in self.deal_rules and "bundle_with" in self.deal_rules[item]:
                bundle_item = self.deal_rules[item]["bundle_with"]
                bundle_quantity = self.scanned_items.get(bundle_item, 0)

                # Apply the bundle deal dynamically based on the rules
                total_price += Deal.bundle_deal(
                    self.pricing_rules[item],
                    self.pricing_rules[bundle_item],
                    quantity,
                    bundle_quantity
                )
                # Mark items as processed in summary
                item_summary[item] = quantity
                item_summary[bundle_item] = bundle_quantity

        # Now, handle regular pricing and other deals (non-bundled items)
        for item, quantity in self.scanned_items.items():
            # Skip if item was already processed in a bundle
            if item in item_summary:
                continue

            # Apply the pricing rule for non-bundled items
            if item in self.deal_rules:
                # Deal rule is applied if defined in deal_rules
                rule = self.deal_rules[item]
                price = rule["deal"](self.pricing_rules[item], quantity, *rule.get("args", []))
            else:
                # No deal, use regular price
                price = self.pricing_rules[item] * quantity

            total_price += price
            item_summary[item] = quantity

        return item_summary, total_price




if __name__ == "__main__":

    # Initialize checkout system with pricing rules and opening day deals
    from deal_controller import opening_day_deals
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
