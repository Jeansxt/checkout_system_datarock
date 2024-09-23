
### README for Datarock - Shopping Cart Checkout System

## Overview
This project implements a flexible checkout system that handles item scanning, applies pricing rules, and processes various types of deals (e.g., bundle deals, bulk discounts, "buy X get Y" offers). The system is designed to be easily extendable for different promotions by allowing deal rules to be passed during checkout initialization.

## Features
- **Item Scanning**: Add items to the cart by scanning, with adjustable quantities.
- **Dynamic Pricing**: Each item has a base price, which can be adjusted by applying different deals.
- **Opening Day Deals**: Includes several predefined promotions:
  - **3 for 2 Deal on Apple TVs**: Buy 3, pay for 2.
  - **Bulk Discount on iPads**: Buy more than 4, each iPad is priced at $499.99.
  - **Bundle Deal for MacBook Pro and VGA Adapter**: Buy a MacBook Pro and get a VGA adapter for free.
- **Flexible Future Deals**: Easily swap or add new deal rules to support future promotions.

## Technologies
- **Python 3.x**

## Structure

### Classes

1. **Deal**: 
   - Contains static methods for handling different types of deals:
     - `three_for_two_deal`: Handles "3 for 2" offers.
     - `bulk_buy_deal`: Handles bulk discount offers.
     - `bundle_deal`: Handles bundling of items (e.g., free item with purchase of another).
   
2. **Checkout**:
   - Handles the main checkout logic, including item scanning and total price calculation.
   - Allows passing in dynamic deal rules at initialization for flexibility.

## Usage

### 1. Clone the repository
```
git clone https://github.com/Jeansxt/checkout_system_datarock.git
cd  checkout_system_datarock
```

### 2. Install dependencies
There are no additional dependencies required for this project.

### 3. How to run the checkout system

In the `checkout.py` file, we define the base item prices and the opening day deals. The checkout system scans items, applies the deals, and calculates the total price.

#### Example Usage:

```python
if __name__ == "__main__":
    from deal_controller import opening_day_deals
    checkout = Checkout(opening_day_deals())

    checkout.scan("mbp")
    checkout.scan("vga")
    checkout.scan("ipd")

    item_summary, total_price = checkout.total()

    print("Item Summary:")
    for item, quantity in item_summary.items():
        print(f"{item}: Quantity = {quantity}")
    
    print(f"Total Price: ${total_price:.2f}")

```

### 4. Running the script
Run the `checkout.py` file in your terminal or Python IDE.
or simply run 'main_app.py' for a test run.

```bash
python main_app.py
```


### 5. Adding Future Deals

To modify or add new deals:
1. Define new deal functions in the `Deal` class.
2. Update or replace the `opening_day_deals()` function to reflect new deals.
3. Pass the updated deal rules into the `Checkout` class when initializing it.

## Extensibility
- **Pricing Rules**: Change the base price of an item by modifying the `pricing_rules` dictionary.
- **Deals**: New promotions can be implemented by adding or modifying deal functions inside the `Deal` class and passing them into the checkout system during initialization.
