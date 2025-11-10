import streamlit as st
import pandas as pd
from ontologies.library import build_library_graph
from queries import library_queries as lq
from utils.sparql_runner import run_sparql

st.title("📚 Ontologi Library Interaktif")

graph = build_library_graph()

cq_option = st.selectbox(
    "Pilih pertanyaan:",
    [
        "CQ1: Semua buku di perpustakaan",
        "CQ2: Semua anggota perpustakaan",
        "CQ3: Buku dan penulisnya",
        "CQ4: Anggota dan buku yang dipinjam",
        "CQ5: Penulis yang ada di perpustakaan"
    ]
)

if st.button("Jalankan Query"):
    if cq_option.startswith("CQ1"):
        hasil = run_sparql(graph, lq.CQ1)
        st.subheader("Hasil CQ1: Semua Buku")
        for row in hasil:
            st.write("-", row[0])

    elif cq_option.startswith("CQ2"):
        hasil = run_sparql(graph, lq.CQ2)
        st.subheader("Hasil CQ2: Semua Anggota")
        for row in hasil:
            st.write("-", row[0])

    elif cq_option.startswith("CQ3"):
        hasil = run_sparql(graph, lq.CQ3)
        st.subheader("Hasil CQ3: Buku dan Penulis")
        rows = [{"Buku": str(r[0]), "Penulis": str(r[1])} for r in hasil]
        
    elif cq_option.startswith("CQ4"):
        hasil = run_sparql(graph, lq.CQ4)
        st.subheader("Hasil CQ4: Anggota dan Buku yang Dipinjam")
        for row in hasil:
            st.write("-", row[0], "→", row[1])

    elif cq_option.startswith("CQ5"):
        hasil = run_sparql(graph, lq.CQ5)
        st.subheader("Hasil CQ5: Penulis")
        for row in hasil:
            st.write("-", row[0])
