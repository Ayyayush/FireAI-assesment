import streamlit as st

from utils.billing import calculate_cost, format_bill

# ==================================================
# 1. PAGE HEADER
# ==================================================

st.title("🧾 Billing Calculator")

st.write(
    "Calculate printing and photocopying charges " "using the shop's actual rates."
)

st.divider()


# ==================================================
# 2. DISPLAY PRINTING RATES
# ==================================================

st.subheader("Shop Printing Rates")

col1, col2 = st.columns(2)

col1.metric("Printout", "₹5 / page")

col2.metric("Photocopy", "₹3 / page")

st.divider()


# ==================================================
# 3. BILL CALCULATOR
# ==================================================

st.subheader("Calculate Customer Bill")

with st.form("billing_form"):

    col1, col2 = st.columns(2)

    with col1:

        print_type = st.selectbox("Select Printing Type", ["Printout", "Photocopy"])

        pages = st.number_input(
            "Number of Pages", min_value=1, max_value=10000, value=1, step=1
        )

    with col2:

        copies = st.number_input(
            "Number of Copies", min_value=1, max_value=1000, value=1, step=1
        )

    calculate_button = st.form_submit_button("Calculate Bill", use_container_width=True)


# ==================================================
# 4. CALCULATE AND DISPLAY BILL
# ==================================================

if calculate_button:

    try:

        bill = calculate_cost(
            pages=int(pages), copies=int(copies), print_type=print_type
        )

        st.session_state["current_bill"] = bill

    except ValueError as error:

        st.error(str(error))


# ==================================================
# 5. BILL SUMMARY
# ==================================================

if "current_bill" in st.session_state:

    bill = st.session_state["current_bill"]

    st.divider()

    st.subheader("📄 Bill Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Pages", bill["pages"])

    col2.metric("Copies", bill["copies"])

    col3.metric("Rate Per Page", f"₹{bill['rate_per_page']}")

    st.success(f"Total Amount: ₹{bill['total']}")

    # Generate readable bill
    bill_text = format_bill(bill)

    st.text_area("Bill Details", value=bill_text, height=150)

    st.download_button(
        label="Download Bill",
        data=bill_text,
        file_name="printdesk_bill.txt",
        mime="text/plain",
        use_container_width=True,
    )

    if st.button("Clear Bill", use_container_width=True):

        del st.session_state["current_bill"]

        st.rerun()


# ==================================================
# 6. FOOTER
# ==================================================

st.divider()

st.caption("PrintDesk | Billing and Cost Estimation")
