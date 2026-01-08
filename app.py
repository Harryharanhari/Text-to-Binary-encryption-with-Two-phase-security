import streamlit as st
import os
from crypto_utils import *

st.set_page_config(page_title="Text → Binary Encryption", layout="centered")

st.title("🔐 Text to Binary Encryption System")
st.markdown("**Two-Phase Security: Salting + MD5 (Educational Purpose)**")

tab1, tab2 = st.tabs(["🔒 Encrypt", "🔓 Decrypt"])

# ------------------ ENCRYPT ------------------
with tab1:
    st.subheader("Encrypt Text")

    text = st.text_area("Enter Text")
    password = st.text_input("Enter Password", type="password")

    if st.button("Encrypt"):
        if text and password:
            salt = os.urandom(16)
            key = generate_key(password, salt)

            binary = text_to_binary(text)
            encrypted = xor_process(binary, key)

            st.success("Encryption Successful ✅")
            st.text_area("Encrypted Binary", encrypted, height=150)
            st.text_input("Salt (Save this)", salt.hex())
        else:
            st.warning("Please enter both text and password")

# ------------------ DECRYPT ------------------
with tab2:
    st.subheader("Decrypt Text")

    encrypted_binary = st.text_area("Encrypted Binary")
    password = st.text_input("Password", type="password")
    salt_hex = st.text_input("Salt (Hex)")

    if st.button("Decrypt"):
        try:
            salt = bytes.fromhex(salt_hex)
            key = generate_key(password, salt)

            decrypted_binary = xor_process(encrypted_binary, key)
            original_text = binary_to_text(decrypted_binary)

            st.success("Decryption Successful ✅")
            st.text_area("Decrypted Text", original_text)
        except:
            st.error("❌ Invalid password or corrupted data")
