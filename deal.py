class Deal:
    def three_for_two_deal(item_price, quantity):
        # 3 for 2 deal logic: buy 3, pay for 2
        if not isinstance(item_price, (int, float)):
            raise ValueError("item_price must be a number (int or float).")
        eligible_sets = quantity // 3
        remainder = quantity % 3
        total_price = (eligible_sets * 2 * item_price) + (remainder * item_price)
        return total_price

    def bulk_buy_deal(item_price, quantity, discount_threshold, discounted_price):
        if not isinstance(item_price, (int, float)) and not isinstance(discounted_price, (int, float)) :
            raise ValueError("price must be a number (int or float).")
        # Bulk buy discount logic: if more than threshold, apply discount
        if quantity >= discount_threshold:
            return quantity * discounted_price
        else:
            return quantity * item_price

    def bundle_deal(main_item_price, bundle_item_price, main_quantity, bundle_quantity):
        if not isinstance(main_item_price, (int, float)) and not isinstance(bundle_item_price, (int, float)) :
            raise ValueError("price must be a number (int or float).")
        # For each main item, one bundle item is free
        # Charge for extra bundle items beyond the number of main items
        free_items = min(main_quantity, bundle_quantity)
        extra_bundle_items = bundle_quantity - free_items
        return (main_quantity * main_item_price) + (extra_bundle_items * bundle_item_price)
    


if __name__ == "__main__":
    three_for_two_deal = Deal.three_for_two_deal(1,6)
    print(three_for_two_deal)

    bulk_buy_deal = Deal.bulk_buy_deal(2,4,4,1)
    print(bulk_buy_deal)

    bundle_deal = Deal.bundle_deal(1,1,1,2)
    print(bundle_deal)

