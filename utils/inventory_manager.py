import pandas as pd

from utils.data_manager import load_stock, save_stock

# --------------------------------------------------
# GENERATE UNIQUE STOCK ID
# --------------------------------------------------


def generate_stock_id():
    """Generate IDs such as STK001, STK002."""

    stock = load_stock()

    if stock.empty:
        return "STK001"

    numbers = []

    for stock_id in stock["product_id"].astype(str):
        if stock_id.startswith("STK") and stock_id[3:].isdigit():
            numbers.append(int(stock_id[3:]))

    next_number = max(numbers, default=0) + 1

    return f"STK{next_number:03d}"


# --------------------------------------------------
# VALIDATE QUANTITY
# --------------------------------------------------


def validate_quantity(quantity, field_name):
    """Ensure quantity is a non-negative integer."""

    if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity < 0:
        raise ValueError(f"{field_name} must be a non-negative integer.")


# --------------------------------------------------
# ADD NEW STOCK ITEM
# --------------------------------------------------


def add_stock_item(product_name, current_quantity, minimum_quantity):
    """Add a new stationery product to the stock register."""

    if not isinstance(product_name, str) or not product_name.strip():
        raise ValueError("Product name cannot be empty.")

    validate_quantity(current_quantity, "Current quantity")
    validate_quantity(minimum_quantity, "Minimum quantity")

    stock = load_stock()

    # Prevent duplicate product names
    if not stock.empty:
        existing_names = stock["product_name"].astype(str).str.strip().str.lower()

        if product_name.strip().lower() in existing_names.values:
            raise ValueError("This product already exists.")

    item = {
        "product_id": generate_stock_id(),
        "product_name": product_name.strip(),
        "current_quantity": current_quantity,
        "minimum_quantity": minimum_quantity,
    }

    updated_stock = pd.concat([stock, pd.DataFrame([item])], ignore_index=True)

    save_stock(updated_stock)

    return item


# --------------------------------------------------
# GET ALL STOCK ITEMS
# --------------------------------------------------


def get_all_stock():
    """Return all stationery stock records."""

    return load_stock()


# --------------------------------------------------
# UPDATE STOCK QUANTITY
# --------------------------------------------------


def update_stock_quantity(product_id, new_quantity):
    """Update the current quantity of a stock item."""

    validate_quantity(new_quantity, "New quantity")

    stock = load_stock()

    matching_items = stock["product_id"] == product_id

    if not matching_items.any():
        raise ValueError(f"Product ID {product_id} not found.")

    stock.loc[matching_items, "current_quantity"] = new_quantity

    save_stock(stock)

    return True


# --------------------------------------------------
# GET LOW STOCK ITEMS
# --------------------------------------------------


def get_low_stock_items():
    """
    Return products whose current quantity
    is less than or equal to minimum quantity.
    """

    stock = load_stock()

    if stock.empty:
        return stock

    low_stock = stock[stock["current_quantity"] <= stock["minimum_quantity"]]

    return low_stock.reset_index(drop=True)
