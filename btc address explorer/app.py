import streamlit as st
from providers.blockstream import (
    get_address_info,
    get_address_txs,
    get_address_utxo
)

st.set_page_config(page_title="BTC Explorer", layout="wide")
st.title("BTC Address Explorer")

address = st.text_input(
    "Bitcoin address",
    placeholder="bc1q..."
)

if address:
    try:
        info = get_address_info(address)
        utxo = get_address_utxo(address)
        txs = get_address_txs(address)

        st.subheader("Address summary")
        st.json(info)

        st.subheader("UTXO")
        st.json(utxo)

        st.subheader("Transactions")
        st.json(txs)

    except Exception as e:
        st.error(f"Error fetching data: {e}")
