import streamlit as st

from utils.inventory_manager import (
    add_stock_item,
    get_all_stock,
    update_stock_quantity,
    get_low_stock_items,
)

# ==================================================
# 1. PAGE HEADER
# ==================================================

st.title("📦 Inventory Management")

st.write(
    "Track stationery products, update available quantities "
    "and monitor low-stock items."
)

st.divider()


# ==================================================
# 2. LOAD INVENTORY
# ==================================================

stock = get_all_stock()
low_stock = get_low_stock_items()


# ==================================================
# 3. INVENTORY STATISTICS
# ==================================================

total_products = len(stock)
low_stock_count = len(low_stock)

col1, col2 = st.columns(2)

col1.metric("Total Products", total_products)

col2.metric("Low Stock Alerts", low_stock_count)


# ==================================================
# 4. ADD NEW PRODUCT
# ==================================================

st.divider()

st.subheader("➕ Add Stationery Product")

with st.form("add_stock_form", clear_on_submit=True):

    product_name = st.text_input("Product Name", placeholder="Example: Notebook")

    col1, col2 = st.columns(2)

    with col1:

        current_quantity = st.number_input(
            "Current Quantity", min_value=0, max_value=100000, value=0, step=1
        )

    with col2:

        minimum_quantity = st.number_input(
            "Minimum Stock Level", min_value=0, max_value=100000, value=5, step=1
        )

    submitted = st.form_submit_button("Add Product", use_container_width=True)

    if submitted:

        try:

            item = add_stock_item(
                product_name=product_name,
                current_quantity=int(current_quantity),
                minimum_quantity=int(minimum_quantity),
            )

            st.success(
                f"{item['product_name']} added successfully. "
                f"Product ID: {item['product_id']}"
            )

            st.rerun()

        except ValueError as error:

            st.error(str(error))


# ==================================================
# 5. DISPLAY INVENTORY
# ==================================================

st.divider()

st.subheader("📋 Current Stock")

stock = get_all_stock()

if stock.empty:

    st.info(
        "No stationery products recorded yet. " "Add products using the form above."
    )

else:

    st.dataframe(stock, use_container_width=True, hide_index=True)


# ==================================================
# 6. UPDATE PRODUCT QUANTITY
# ==================================================

st.divider()

st.subheader("🔄 Update Stock Quantity")

if stock.empty:

    st.info("Add a product before updating its quantity.")

else:

    product_ids = stock["product_id"].astype(str).tolist()

    selected_product = st.selectbox(
        "Select Product",
        product_ids,
        format_func=lambda product_id: (
            f"{product_id} - "
            f"{stock.loc[stock['product_id'] == product_id, 'product_name'].iloc[0]}"
        ),
    )

    current_quantity = int(
        stock.loc[stock["product_id"] == selected_product, "current_quantity"].iloc[0]
    )

    st.write(f"Current Quantity: **{current_quantity}**")

    new_quantity = st.number_input(
        "Enter New Quantity",
        min_value=0,
        max_value=100000,
        value=current_quantity,
        step=1,
        key="updated_quantity",
    )

    if st.button("Update Quantity", use_container_width=True):

        try:

            update_stock_quantity(
                product_id=selected_product, new_quantity=int(new_quantity)
            )

            st.success("Stock quantity updated successfully.")

            st.rerun()

        except ValueError as error:

            st.error(str(error))


# ==================================================
# 7. LOW STOCK ALERTS
# ==================================================

st.divider()

st.subheader("⚠️ Low Stock Alerts")

low_stock = get_low_stock_items()

if stock.empty:

    st.info("No inventory records available.")

elif low_stock.empty:

    st.success("All recorded products are above their minimum stock levels.")

else:

    st.warning(f"{len(low_stock)} product(s) need replenishment.")

    st.dataframe(low_stock, use_container_width=True, hide_index=True)


# ==================================================
# 8. FOOTER
# ==================================================

st.divider()

st.caption("PrintDesk | Stationery Inventory Management")
