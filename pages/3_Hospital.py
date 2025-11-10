import streamlit as st
import pandas as pd
from ontologies.hospital import build_hospital_graph
from queries import hospital_queries as hq
from utils.sparql_runner import run_sparql

st.title("🏥 Ontologi Hospital Interaktif")

graph = build_hospital_graph()

cq_option = st.selectbox(
    "Pilih pertanyaan:",
    [
        "CQ1: Dokter yang merawat pasien tertentu",
        "CQ2: Pasien di ruangan tertentu",
        "CQ3: Penyakit yang didiagnosa oleh dokter tertentu",
        "CQ4: Obat yang digunakan pasien tertentu",
        "CQ5: Pasien dan dokter yang merawatnya"
    ]
)

user_input = st.text_input("Masukkan kata kunci (nama pasien/dokter/ruangan):")

if st.button("Jalankan Query"):
    if cq_option.startswith("CQ1"):
        query = hq.CQ1_TEMPLATE.format(pasien=user_input)
        hasil = run_sparql(graph, query)
        st.subheader("Hasil CQ1: Dokter yang merawat pasien")
        for row in hasil:
            st.write("-", row[0])   # tampil per baris dengan dot

    elif cq_option.startswith("CQ2"):
        query = hq.CQ2_TEMPLATE.format(ruangan=user_input)
        hasil = run_sparql(graph, query)
        st.subheader("Hasil CQ2: Pasien di ruangan")
        for row in hasil:
            st.write("-", row[0])

    elif cq_option.startswith("CQ3"):
        query = hq.CQ3_TEMPLATE.format(dokter=user_input)
        hasil = run_sparql(graph, query)
        st.subheader("Hasil CQ3: Penyakit yang didiagnosa dokter")
        for row in hasil:
            st.write("-", row[0])

    elif cq_option.startswith("CQ4"):
        hasil = run_sparql(graph, hq.CQ4_TEMPLATE)
        st.subheader("Hasil CQ4: Obat yang digunakan pasien")
        rows = [{"Obat": str(r[0]), "Pasien": str(r[1])} for r in hasil]
        st.dataframe(pd.DataFrame(rows))

    elif cq_option.startswith("CQ5"):
        hasil = run_sparql(graph, hq.CQ5)
        st.subheader("Hasil CQ5: Pasien dan dokter yang merawatnya")
        rows = [{"Pasien": str(r[0]), "Dokter": str(r[1])} for r in hasil]
        st.dataframe(pd.DataFrame(rows))
