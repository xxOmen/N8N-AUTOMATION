import streamlit as st
from datetime import datetime

# ======================================================
# SITE CONFIG
# ======================================================
st.set_page_config(page_title="ShopVerse PK — Mock E-Commerce", layout="wide")
st.title("🛒 ShopVerse PK — Streamlit E-Commerce Demo")

# ======================================================
# MOCK PRODUCT DATABASE (PKR)
# ======================================================
PRODUCTS = [
    {"id": 1, "name": "Wireless Headphones", "price": 12999, "category": "Audio",
     "image": "https://images.unsplash.com/photo-1511367461989-f85a21fda167?auto=format&fit=crop&w=600&q=60",
     "description": "Noise-cancelling wireless headphones with 24-hour battery life."},
    {"id": 2, "name": "Smartwatch Pro", "price": 18999, "category": "Wearables",
     "image": "https://images.unsplash.com/photo-1523475496153-3d6cc450b0fa?auto=format&fit=crop&w=600&q=60",
     "description": "Track fitness, notifications, and heart rate. Waterproof design."},
    {"id": 3, "name": "Mechanical Keyboard RGB", "price": 10999, "category": "Accessories",
     "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=600&q=60",
     "description": "RGB mechanical keyboard with tactile blue switches."},
    {"id": 4, "name": "4K Action Camera", "price": 24999, "category": "Cameras",
     "image": "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?auto=format&fit=crop&w=600&q=60",
     "description": "Capture adventures in stunning 4K UHD with waterproof casing."},
    {"id": 5, "name": "Gaming Mouse Pro", "price": 5999, "category": "Accessories",
     "image": "https://images.unsplash.com/photo-1606813902788-7d16d81e2b08?auto=format&fit=crop&w=600&q=60",
     "description": "Ergonomic RGB gaming mouse with 16000 DPI precision."},
    {"id": 6, "name": "Bluetooth Speaker Mini", "price": 4999, "category": "Audio",
     "image": "https://images.unsplash.com/photo-1585386959984-a41552231693?auto=format&fit=crop&w=600&q=60",
     "description": "Compact, powerful Bluetooth speaker with deep bass."},
    {"id": 7, "name": "Laptop Stand Aluminum", "price": 3499, "category": "Accessories",
     "image": "https://images.unsplash.com/photo-1616627985025-3cbe41a5dc41?auto=format&fit=crop&w=600&q=60",
     "description": "Ergonomic laptop stand for better posture and cooling."},
    {"id": 8, "name": "USB-C Hub 7-in-1", "price": 6999, "category": "Accessories",
     "image": "https://images.unsplash.com/photo-1612831455546-1e9b4a3a4f91?auto=format&fit=crop&w=600&q=60",
     "description": "Expand connectivity with HDMI, USB, and card reader ports."},
    {"id": 9, "name": "Wireless Charger Pad", "price": 2999, "category": "Accessories",
     "image": "https://images.unsplash.com/photo-1585386959984-a41552231693?auto=format&fit=crop&w=600&q=60",
     "description": "Fast 15W Qi wireless charging pad for all devices."},
    {"id": 10, "name": "Smart Lamp RGB", "price": 7499, "category": "Home Tech",
     "image": "https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=600&q=60",
     "description": "App-controlled RGB lamp with voice assistant support."},
    {"id": 11, "name": "Portable SSD 1TB", "price": 18999, "category": "Storage",
     "image": "https://images.unsplash.com/photo-1555617983-7f9b8a4c9187?auto=format&fit=crop&w=600&q=60",
     "description": "High-speed USB-C external SSD for backups and travel."},
    {"id": 12, "name": "Noise Cancelling Earbuds", "price": 14999, "category": "Audio",
     "image": "https://images.unsplash.com/photo-1570818836591-0b67b4f67d64?auto=format&fit=crop&w=600&q=60",
     "description": "Compact ANC earbuds with case and 30-hour battery."},
    {"id": 13, "name": "Drone Mini 4K", "price": 32999, "category": "Cameras",
     "image": "https://images.unsplash.com/photo-1523966211575-eb4a01e7dd51?auto=format&fit=crop&w=600&q=60",
     "description": "Lightweight 4K drone with GPS and return-to-home."},
    {"id": 14, "name": "Fitness Band Lite", "price": 6999, "category": "Wearables",
     "image": "https://images.unsplash.com/photo-1554284126-aa88f22d8b74?auto=format&fit=crop&w=600&q=60",
     "description": "Track steps, calories, and sleep with long battery life."},
    {"id": 15, "name": "Smart Home Plug", "price": 2999, "category": "Home Tech",
     "image": "https://images.unsplash.com/photo-1523395242510-2930fdd9c6c0?auto=format&fit=crop&w=600&q=60",
     "description": "Control appliances remotely via app or voice assistant."},
    {"id": 16, "name": "Gaming Chair", "price": 28999, "category": "Furniture",
     "image": "https://images.unsplash.com/photo-1616628182509-cba8e8fb763b?auto=format&fit=crop&w=600&q=60",
     "description": "Ergonomic gaming chair with lumbar and neck support."},
    {"id": 17, "name": "Mechanical Pencil Set", "price": 1999, "category": "Stationery",
     "image": "https://images.unsplash.com/photo-1573496782646-ff4b2a6b6d79?auto=format&fit=crop&w=600&q=60",
     "description": "Durable precision pencils for sketching and drafting."},
    {"id": 18, "name": "Monitor 27-inch 2K", "price": 49999, "category": "Displays",
     "image": "https://images.unsplash.com/photo-1616628182509-cba8e8fb763b?auto=format&fit=crop&w=600&q=60",
     "description": "27-inch 2K IPS monitor with 144Hz refresh rate."}
]

# ======================================================
# INITIALIZE SESSION STATE
# ======================================================
if "page" not in st.session_state:
    st.session_state.page = "home"
if "cart" not in st.session_state:
    st.session_state.cart = []

# ======================================================
# PAGE NAVIGATION
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
    if st.button("🛒 Cart / Checkout"):
        go_to("checkout")
    st.write("---")
    st.header("Your Cart")
    if st.session_state.cart:
        total = sum(item["price"] for item in st.session_state.cart)
        for item in st.session_state.cart:
            st.caption(f"{item['name']} — Rs {item['price']:,}")
        st.markdown(f"**Total: Rs {total:,}**")
    else:
        st.info("Cart is empty.")

# ======================================================
# HOME PAGE (PRODUCT LIST)
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
                st.success(f"🎉 Order Confirmed! Thank you {name}.")
                st.balloons()
                st.session_state.cart = []
            else:
                st.error("⚠️ Please fill all required fields.")

# ======================================================
# FOOTER
# ======================================================
st.markdown("---")
st.caption("© 2025 ShopVerse PK | Demo by GPT-5 | Built with ❤️ using Streamlit")
