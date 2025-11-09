import streamlit as st
from ontologies.university import build_university_graph
from queries import university_queries as uq
from utils.sparql_runner import run_sparql
import pandas as pd

st.title("🏫 Ontologi Universitas & Akademik")

graph = build_university_graph()

# Dropdown untuk memilih CQ
cq_option = st.selectbox(
    "Pilih pertanyaan (CQ):",
    [
        "CQ1: Siapa dosen yang mengajar Data Mining?",
        "CQ2: Mahasiswa mana yang mengambil mata kuliah terbanyak?",
        "CQ3: Berapa jumlah mahasiswa di Fakultas Teknik?",
        "CQ4: Mata kuliah apa saja yang diajarkan oleh Dr. Andi?",
        "CQ5: Mahasiswa dengan lebih dari 1 mata kuliah"
    ]
)

# Tombol eksekusi
if st.button("Jalankan Query"):
    if cq_option.startswith("CQ1"):
        hasil = run_sparql(graph, uq.CQ1)
        st.subheader("Hasil CQ1")
        for row in hasil:
            st.write("-", row[0])

    elif cq_option.startswith("CQ2"):
        hasil = run_sparql(graph, uq.CQ2)
        rows = [{"Mahasiswa": str(row[0]), "Jumlah MK": int(row[1])} for row in hasil]
        df = pd.DataFrame(rows)
        
        st.subheader("Hasil CQ2")
        st.dataframe(df, use_container_width=True)

    elif cq_option.startswith("CQ3"):
        hasil = run_sparql(graph, uq.CQ3)
        st.subheader("Hasil CQ3")
        for row in hasil:
            st.write("Jumlah Mahasiswa di Fakultas Teknik:", row[0])

    elif cq_option.startswith("CQ4"):
        hasil = run_sparql(graph, uq.CQ4)
        st.subheader("Hasil CQ4")
        for row in hasil:
            st.write("-", row[0])

    elif cq_option.startswith("CQ5"):
        hasil = run_sparql(graph, uq.CQ5)
        st.subheader("Hasil CQ5")
        for row in hasil:
            st.write("-", row[0])
