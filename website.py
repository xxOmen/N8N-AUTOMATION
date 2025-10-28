import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ======================================================
# SITE CONFIG
# ======================================================
st.set_page_config(page_title="ShopVerse PK — E-Commerce Demo", layout="wide")
st.title("🛒 ShopVerse PK — Streamlit E-Commerce Demo")

# ======================================================
# PRODUCT DATABASE
# ======================================================
PRODUCTS = [
    {"id": 1, "name": "Wireless Headphones", "price": 12999, "category": "Audio",
     "image": "https://images.unsplash.com/photo-1583225252835-9e2e96a3ff4f?auto=format&fit=crop&w=600&q=80",
     "description": "Noise-cancelling headphones with 24-hour battery life."},
    {"id": 2, "name": "Smartwatch Pro", "price": 18999, "category": "Wearables",
     "image": "https://images.unsplash.com/photo-1603791440384-56cd371ee9a7?auto=format&fit=crop&w=600&q=80",
     "description": "Track fitness, notifications, and heart rate. Waterproof design."},
    {"id": 3, "name": "Mechanical Keyboard RGB", "price": 10999, "category": "Accessories",
     "image": "https://images.unsplash.com/photo-1555617117-08fda9b8fdf8?auto=format&fit=crop&w=600&q=80",
     "description": "RGB mechanical keyboard with tactile blue switches."},
    {"id": 4, "name": "4K Action Camera", "price": 24999, "category": "Cameras",
     "image": "https://images.unsplash.com/photo-1574539322703-1c2a7d7f9b8c?auto=format&fit=crop&w=600&q=80",
     "description": "Capture adventures in stunning 4K UHD with waterproof casing."},
    {"id": 5, "name": "Gaming Mouse Pro", "price": 5999, "category": "Accessories",
     "image": "https://images.unsplash.com/photo-1606813902788-7d16d81e2b08?auto=format&fit=crop&w=600&q=80",
     "description": "Ergonomic RGB gaming mouse with 16000 DPI precision."},
    {"id": 6, "name": "Bluetooth Speaker Mini", "price": 4999, "category": "Audio",
     "image": "https://images.unsplash.com/photo-1583225252835-9e2e96a3ff4f?auto=format&fit=crop&w=600&q=80",
     "description": "Compact Bluetooth speaker with deep bass and clear sound."},
    {"id": 7, "name": "Laptop Stand Aluminum", "price": 3499, "category": "Accessories",
     "image": "https://images.unsplash.com/photo-1589183056223-094d3c76fe1d?auto=format&fit=crop&w=600&q=80",
     "description": "Ergonomic aluminum laptop stand for cooling and comfort."},
    {"id": 8, "name": "USB-C Hub 7-in-1", "price": 6999, "category": "Accessories",
     "image": "https://images.unsplash.com/photo-1612831455546-1e9b4a3a4f91?auto=format&fit=crop&w=600&q=80",
     "description": "Expand connectivity with HDMI, USB, and card reader ports."},
    {"id": 9, "name": "Wireless Charger Pad", "price": 2999, "category": "Accessories",
     "image": "https://images.unsplash.com/photo-1570818798753-6631dbdbee0d?auto=format&fit=crop&w=600&q=80",
     "description": "Fast 15W Qi wireless charging pad for all compatible devices."},
    {"id": 10, "name": "Smart Lamp RGB", "price": 7499, "category": "Home Tech",
     "image": "https://images.unsplash.com/photo-1524231757912-21f4b89f2e5c?auto=format&fit=crop&w=600&q=80",
     "description": "App-controlled RGB lamp with Alexa and Google support."},
    {"id": 11, "name": "Portable SSD 1TB", "price": 18999, "category": "Storage",
     "image": "https://images.unsplash.com/photo-1570824100810-473f2a9d8f5f?auto=format&fit=crop&w=600&q=80",
     "description": "High-speed USB-C external SSD for backups and travel."},
    {"id": 12, "name": "Noise Cancelling Earbuds", "price": 14999, "category": "Audio",
     "image": "https://images.unsplash.com/photo-1585386959984-a41552231693?auto=format&fit=crop&w=600&q=80",
     "description": "Compact ANC earbuds with charging case and 30-hour battery."},
    {"id": 13, "name": "Drone Mini 4K", "price": 32999, "category": "Cameras",
     "image": "https://images.unsplash.com/photo-1523966211575-eb4a01e7dd51?auto=format&fit=crop&w=600&q=80",
     "description": "Lightweight 4K drone with GPS and return-to-home feature."},
    {"id": 14, "name": "Fitness Band Lite", "price": 6999, "category": "Wearables",
     "image": "https://images.unsplash.com/photo-1585386959984-a41552231693?auto=format&fit=crop&w=600&q=80",
     "description": "Track steps, calories, and sleep with long battery life."},
    {"id": 15, "name": "Smart Plug WiFi", "price": 2999, "category": "Home Tech",
     "image": "https://images.unsplash.com/photo-1616628182509-cba8e8fb763b?auto=format&fit=crop&w=600&q=80",
     "description": "Control appliances remotely via app or voice assistant."},
]

# ======================================================
# SESSION STATE
# ======================================================
if "page" not in st.session_state:
    st.session_state.page = "home"
if "cart" not in st.session_state:
    st.session_state.cart = []

# ======================================================
# ORDER STORAGE SETUP
# ======================================================
ORDERS_FILE = "orders.csv"
if not os.path.exists(ORDERS_FILE):
    pd.DataFrame(columns=["OrderID", "Name", "Email", "Address", "PaymentMethod", "Items", "Total", "Date"]).to_csv(ORDERS_FILE, index=False)

# ======================================================
# PAGE NAVIGATION FUNCTION
# ======================================================
def go_to(page):
    st.session_state.page = page

# ======================================================
# SIDEBAR
# ======================================================
with st.sidebar:
    st.header("Navigation")
    if st.button("🏠 Home"):
        go_to("home")
    if st.button("💳 Checkout"):
        go_to("checkout")
    st.write("---")
    st.header("Your Cart")
    if st.session_state.cart:
        total = sum(item["price"] for item in st.session_state.cart)
        for item in st.session_state.cart:
            st.caption(f"{item['name']} — Rs {item['price']:,}")
        st.markdown(f"**Total: Rs {total:,}**")
    else:
        st.info("Your cart is empty.")

# ======================================================
# HOME PAGE
# ======================================================
if st.session_state.page == "home":
    st.markdown("### 🧩 Featured Products")
    cols = st.columns(3)
    for i, product in enumerate(PRODUCTS):
        col = cols[i % 3]
        with col:
            st.image(product["image"], use_container_width=True)
            st.subheader(product["name"])
            st.caption(product["category"])
            st.write(product["description"])
            st.markdown(f"**Price:** Rs {product['price']:,}")
            if st.button("Add to Cart 🛍️", key=f"add_{product['id']}"):
                st.session_state.cart.append(product)
                st.success(f"Added {product['name']} to cart!")

# ======================================================
# CHECKOUT PAGE
# ======================================================
elif st.session_state.page == "checkout":
    st.header("💳 Checkout")

    if not st.session_state.cart:
        st.warning("Your cart is empty! Please add some products first.")
        if st.button("⬅️ Back to Home"):
            go_to("home")
    else:
        total = sum(item["price"] for item in st.session_state.cart)
        st.subheader("🧾 Order Summary")
        for item in st.session_state.cart:
            st.markdown(f"- **{item['name']}** — Rs {item['price']:,}")
        st.markdown(f"### **Total: Rs {total:,}**")
        st.markdown("---")

        st.subheader("👤 Customer Information")
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        address = st.text_area("Shipping Address")
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
                    "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
                df = pd.read_csv(ORDERS_FILE)
                df = pd.concat([df, pd.DataFrame([order])], ignore_index=True)
                df.to_csv(ORDERS_FILE, index=False)
                st.success(f"🎉 Order Confirmed! Thank you {name}. Your order ID is {order['OrderID']}")
                st.balloons()
                st.session_state.cart = []
            else:
                st.error("⚠️ Please fill all required fields.")

# ======================================================
# FOOTER
# ======================================================
st.markdown("---")
st.caption("© 2025 ShopVerse PK | Built with ❤️ using Streamlit")
