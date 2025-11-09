import streamlit as st
import pandas as pd
from ontologies.ecommerce import build_ecommerce_graph
from queries import ecommerce_queries as eq
from utils.sparql_runner import run_sparql

st.title("🛒 Ontologi E-Commerce Interaktif")

graph = build_ecommerce_graph()

cq_option = st.selectbox(
    "Pilih pertanyaan:",
    [
        "Produk dalam kategori dengan harga maksimum",
        "Penjual dengan jumlah produk terbanyak",
        "Pelanggan dari kota tertentu",
        "Produk dengan promo diskon minimum"
    ]
)

user_input = st.text_input("Masukkan kata kunci (kategori/kota/diskon):")
extra_input = st.text_input("Masukkan angka tambahan (misalnya harga max atau diskon min):")

if st.button("Jalankan Query"):
    if cq_option == "Produk dalam kategori dengan harga maksimum":
        try:
            harga_max = int(extra_input)
        except:
            st.error("Masukkan angka harga maksimum")
            harga_max = None
        if harga_max:
            query = eq.CQ13_TEMPLATE.format(kategori=user_input, harga_max=harga_max)
            hasil = run_sparql(graph, query)
            rows = [{"Produk": str(r[0]), "Harga": int(r[1]), "Brand": str(r[2])} for r in hasil]
            st.dataframe(pd.DataFrame(rows))

    elif cq_option == "Penjual dengan jumlah produk terbanyak":
        hasil = run_sparql(graph, eq.CQ15)
        rows = [{"Penjual": str(r[0]), "Jumlah Produk": int(r[1])} for r in hasil]
        st.dataframe(pd.DataFrame(rows))

    elif cq_option == "Pelanggan dari kota tertentu":
        query = eq.CQ17_TEMPLATE.format(kota=user_input)
        hasil = run_sparql(graph, query)
        rows = [{"Pelanggan": str(r[0]), "Email": str(r[1])} for r in hasil]
        st.dataframe(pd.DataFrame(rows))

    elif cq_option == "Produk dengan promo diskon minimum":
        try:
            diskon_min = int(extra_input)
        except:
            st.error("Masukkan angka diskon minimum")
            diskon_min = None
        if diskon_min:
            query = eq.CQ20_TEMPLATE.format(diskon_min=diskon_min)
            hasil = run_sparql(graph, query)
            rows = [{"Produk": str(r[0]), "Harga Asli": int(r[1]), "Diskon": int(r[2]), "Harga Diskon": float(r[3])} for r in hasil]
            st.dataframe(pd.DataFrame(rows))
