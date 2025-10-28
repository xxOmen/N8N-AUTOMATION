import streamlit as st
from datetime import datetime

# ======================================================
# SITE CONFIG
# ======================================================
st.set_page_config(page_title="ShopVerse — Mock E-Commerce", layout="wide")
st.title("🛍️ ShopVerse — Streamlit Demo Store")

# ======================================================
# MOCK DATABASE
# ======================================================
PRODUCTS = [
    {
        "id": 1,
        "name": "Wireless Headphones",
        "price": 59.99,
        "category": "Audio",
        "image": "https://images.unsplash.com/photo-1511367461989-f85a21fda167?auto=format&fit=crop&w=600&q=60",
        "description": "High-quality wireless headphones with noise cancellation and 20-hour battery life."
    },
    {
        "id": 2,
        "name": "Smartwatch Pro",
        "price": 129.99,
        "category": "Wearables",
        "image": "https://images.unsplash.com/photo-1523475496153-3d6cc450b0fa?auto=format&fit=crop&w=600&q=60",
        "description": "Track fitness, sleep, and notifications with the Smartwatch Pro. Waterproof and lightweight."
    },
    {
        "id": 3,
        "name": "Mechanical Keyboard",
        "price": 89.99,
        "category": "Accessories",
        "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=600&q=60",
        "description": "RGB mechanical keyboard with tactile switches for gaming and productivity."
    },
    {
        "id": 4,
        "name": "4K Action Camera",
        "price": 149.99,
        "category": "Cameras",
        "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=600&q=60",
        "description": "Capture adventures in stunning 4K with waterproof case and wide-angle lens."
    }
]

# ======================================================
# SESSION STATE INITIALIZATION
# ======================================================
if "cart" not in st.session_state:
    st.session_state.cart = []

# ======================================================
# SIDEBAR: SHOPPING CART
# ======================================================
with st.sidebar:
    st.header("🛒 Your Cart")
    total = 0
    if st.session_state.cart:
        for item in st.session_state.cart:
            st.write(f"**{item['name']}** — ${item['price']:.2f}")
            total += item["price"]
        st.write("---")
        st.subheader(f"Total: ${total:.2f}")
        if st.button("Checkout"):
            st.success("✅ Checkout complete! Thank you for your purchase.")
            st.session_state.cart = []
    else:
        st.info("Your cart is empty.")

# ======================================================
# PRODUCT LISTING
# ======================================================
st.markdown("### 🧩 Featured Products")

cols = st.columns(2)
for i, product in enumerate(PRODUCTS):
    col = cols[i % 2]
    with col:
        st.image(product["image"], use_column_width=True)
        st.subheader(product["name"])
        st.caption(product["category"])
        st.write(product["description"])
        st.markdown(f"**Price:** ${product['price']:.2f}")
        if st.button(f"Add to Cart 🛍️", key=f"add_{product['id']}"):
            st.session_state.cart.append(product)
            st.success(f"Added {product['name']} to your cart!")

# ======================================================
# MOCK RAG DATABASE PREVIEW
# ======================================================
st.markdown("---")
st.subheader("📦 Product Database (for RAG / search systems)")
st.dataframe(PRODUCTS)

# ======================================================
# FOOTER
# ======================================================
st.markdown("---")
st.caption("© 2025 ShopVerse | Built with ❤️ using Streamlit")
