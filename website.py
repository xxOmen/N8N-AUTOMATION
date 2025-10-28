import streamlit as st
import pandas as pd
import requests
import os
import random
from datetime import datetime

# ======================================================
# CONFIGURATION
# ======================================================
st.set_page_config(
    page_title="ShopVerse PK — Streamlit E-Commerce Demo",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("🛍️ ShopVerse PK — Mock E-Commerce Site")

# ======================================================
# CONSTANTS
# ======================================================
ORDERS_FILE = "orders.csv"
WEBHOOK_URL = "https://omenkit.app.n8n.cloud/webhook/order-confirmation"

# ======================================================
# INITIAL SETUP
# ======================================================
if "cart" not in st.session_state:
    st.session_state.cart = []
if "page" not in st.session_state:
    st.session_state.page = "home"

# Ensure CSV file exists
if not os.path.exists(ORDERS_FILE):
    pd.DataFrame(columns=[
        "OrderID", "Name", "Email", "Address",
        "PaymentMethod", "Items", "Total", "Date"
    ]).to_csv(ORDERS_FILE, index=False)

# ======================================================
# PRODUCT DATABASE
# ======================================================
def load_products():
    """Return a randomized list of demo products with valid images."""
    product_catalog = [
        {"name": "Wireless Earbuds", "price": 12999, "category": "Audio",
         "image": "https://images.unsplash.com/photo-1580894732444-8ecded7900cd?auto=format&fit=crop&w=600&q=80",
         "description": "Compact noise-cancelling earbuds with charging case."},
        {"name": "Smartwatch X", "price": 17999, "category": "Wearables",
         "image": "https://images.unsplash.com/photo-1606813902791-45b2ef2e4b8e?auto=format&fit=crop&w=600&q=80",
         "description": "Fitness tracker with OLED display and heart-rate monitor."},
        {"name": "Gaming Keyboard RGB", "price": 10499, "category": "Accessories",
         "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=600&q=80",
         "description": "Mechanical keyboard with customizable RGB lighting."},
        {"name": "4K Drone Mini", "price": 32499, "category": "Cameras",
         "image": "https://images.unsplash.com/photo-1523966211575-eb4a01e7dd51?auto=format&fit=crop&w=600&q=80",
         "description": "Lightweight drone with 4K camera and GPS stabilization."},
        {"name": "Bluetooth Speaker Pro", "price": 7999, "category": "Audio",
         "image": "https://images.unsplash.com/photo-1583225252835-9e2e96a3ff4f?auto=format&fit=crop&w=600&q=80",
         "description": "Portable speaker with deep bass and waterproof body."},
        {"name": "USB-C Hub 8-in-1", "price": 5999, "category": "Accessories",
         "image": "https://images.unsplash.com/photo-1612831455546-1e9b4a3a4f91?auto=format&fit=crop&w=600&q=80",
         "description": "Expand your laptop ports with HDMI, USB, and SD slots."},
        {"name": "Smart Lamp RGB", "price": 6999, "category": "Home Tech",
         "image": "https://images.unsplash.com/photo-1524231757912-21f4b89f2e5c?auto=format&fit=crop&w=600&q=80",
         "description": "App-controlled smart lamp with voice assistant support."},
        {"name": "Portable SSD 1TB", "price": 18999, "category": "Storage",
         "image": "https://images.unsplash.com/photo-1570824100810-473f2a9d8f5f?auto=format&fit=crop&w=600&q=80",
         "description": "High-speed USB-C SSD for travel and backup."},
        {"name": "Ergonomic Mouse", "price": 4499, "category": "Accessories",
         "image": "https://images.unsplash.com/photo-1606813902788-7d16d81e2b08?auto=format&fit=crop&w=600&q=80",
         "description": "Comfortable wireless mouse with silent clicks."},
        {"name": "Smart Plug WiFi", "price": 2999, "category": "Home Tech",
         "image": "https://images.unsplash.com/photo-1616628182509-cba8e8fb763b?auto=format&fit=crop&w=600&q=80",
         "description": "Control appliances remotely via app or Alexa."},
        {"name": "Fitness Band Lite", "price": 6999, "category": "Wearables",
         "image": "https://images.unsplash.com/photo-1554284126-aa88f22d8b74?auto=format&fit=crop&w=600&q=80",
         "description": "Track steps, calories, and heart rate easily."},
        {"name": "Laptop Stand", "price": 3499, "category": "Accessories",
         "image": "https://images.unsplash.com/photo-1589183056223-094d3c76fe1d?auto=format&fit=crop&w=600&q=80",
         "description": "Aluminum laptop stand with adjustable height."},
        {"name": "Noise Cancelling Headphones", "price": 15999, "category": "Audio",
         "image": "https://images.unsplash.com/photo-1606813902791-45b2ef2e4b8e?auto=format&fit=crop&w=600&q=80",
         "description": "Over-ear wireless headphones with ANC technology."},
        {"name": "Action Camera 4K", "price": 24999, "category": "Cameras",
         "image": "https://images.unsplash.com/photo-1574539322703-1c2a7d7f9b8c?auto=format&fit=crop&w=600&q=80",
         "description": "Capture your adventures in crisp 4K UHD."},
        {"name": "Gaming Chair", "price": 27999, "category": "Furniture",
         "image": "https://images.unsplash.com/photo-1616628182509-cba8e8fb763b?auto=format&fit=crop&w=600&q=80",
         "description": "Ergonomic gaming chair with lumbar and neck support."}
    ]
    random.shuffle(product_catalog)
    return product_catalog


PRODUCTS = load_products()

# ======================================================
# HELPER FUNCTIONS
# ======================================================
def navigate(page: str):
    """Switch pages."""
    st.session_state.page = page

def save_order(order: dict):
    """Append order to CSV file."""
    df = pd.read_csv(ORDERS_FILE)
    df = pd.concat([df, pd.DataFrame([order])], ignore_index=True)
    df.to_csv(ORDERS_FILE, index=False)

def send_webhook(order: dict):
    """Send order confirmation to n8n webhook."""
    try:
        response = requests.get(WEBHOOK_URL, params=order, timeout=10)
        if response.status_code == 200:
            st.toast("✅ Order sent to n8n successfully!")
        else:
            st.warning(f"⚠️ Webhook returned status {response.status_code}")
    except Exception as e:
        st.error(f"❌ Webhook failed: {e}")

# ======================================================
# SIDEBAR
# ======================================================
with st.sidebar:
    st.header("Navigation")
    if st.button("🏠 Home"):
        navigate("home")
    if st.button("💳 Checkout"):
        navigate("checkout")
    st.write("---")
    st.header("Your Cart")
    if st.session_state.cart:
        total = sum(i["price"] for i in st.session_state.cart)
        for item in st.session_state.cart:
            st.caption(f"{item['name']} — Rs {item['price']:,}")
        st.markdown(f"**Total: Rs {total:,}**")
    else:
        st.info("Your cart is empty.")

# ======================================================
# HOME PAGE
# ======================================================
if st.session_state.page == "home":
    st.subheader("✨ Featured Products")
    cols = st.columns(3)
    for i, product in enumerate(PRODUCTS):
        with cols[i % 3]:
            st.image(product["image"], use_container_width=True)
            st.subheader(product["name"])
            st.caption(product["category"])
            st.write(product["description"])
            st.markdown(f"**Price:** Rs {product['price']:,}")
            if st.button("Add to Cart 🛍️", key=f"add_{i}"):
                st.session_state.cart.append(product)
                st.success(f"Added {product['name']} to cart!")

# ======================================================
# CHECKOUT PAGE
# ======================================================
elif st.session_state.page == "checkout":
    st.header("💳 Checkout")

    if not st.session_state.cart:
        st.warning("Your cart is empty. Please add some products first.")
        if st.button("⬅️ Back to Home"):
            navigate("home")
    else:
        total = sum(item["price"] for item in st.session_state.cart)
        st.subheader("🧾 Order Summary")
        for item in st.session_state.cart:
            st.markdown(f"- **{item['name']}** — Rs {item['price']:,}")
        st.markdown(f"### **Total: Rs {total:,}**")
        st.divider()

        # Customer Information Form
        st.subheader("👤 Customer Information")
        name = st.text_input("Full Name *")
        email = st.text_input("Email *")
        address = st.text_area("Shipping Address *")
        payment = st.selectbox("Payment Method", ["Cash on Delivery", "Credit/Debit Card", "Bank Transfer"])

        if st.button("Confirm Order ✅"):
            if name and email and address:
                order = {
                    "OrderID": f"ORD{datetime.now().strftime('%Y%m%d%H%M%S')}",
                    "Name": name,
                    "Email": email,
                    "Address": address,
                    "PaymentMethod": payment,
                    "Items": ", ".join([i["name"] for i in st.session_state.cart]),
                    "Total": total,
                    "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                save_order(order)
                send_webhook(order)
                st.success(f"🎉 Order Confirmed! Thank you, {name}. Your order ID is {order['OrderID']}")
                st.balloons()
                st.session_state.cart = []
            else:
                st.error("⚠️ Please fill all required fields before confirming.")

# ======================================================
# FOOTER
# ======================================================
st.markdown("---")
st.caption("© 2025 ShopVerse PK | Built with ❤️ using Streamlit | Connected to n8n Webhook")
