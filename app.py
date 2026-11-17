import streamlit as st

from utils.data_manager import initialize_data_files

# ==================================================
# 1. APPLICATION CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="PrintDesk",
    page_icon="🖨️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ==================================================
# 2. INITIALIZE DATA FILES
# ==================================================

initialize_data_files()


# ==================================================
# 3. DEFINE APPLICATION PAGES
# ==================================================

dashboard = st.Page("pages/0_Dashboard.py", title="Dashboard", icon="🏠", default=True)

job_register = st.Page("pages/1_Job_Register.py", title="Job Register", icon="📋")

billing = st.Page("pages/2_Billing.py", title="Billing", icon="🧾")

inventory = st.Page("pages/3_Inventory.py", title="Inventory", icon="📦")


# ==================================================
# 4. SIDEBAR NAVIGATION
# ==================================================

pages = {"PrintDesk": [dashboard, job_register, billing, inventory]}

navigation = st.navigation(pages)


# ==================================================
# 5. RUN SELECTED PAGE
# ==================================================

navigation.run()
