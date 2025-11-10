from rdflib import Graph, Namespace, RDF, RDFS, Literal
from rdflib.namespace import XSD

HOSP = Namespace("http://example.org/hospital#")

def build_hospital_graph():
    g = Graph()
    g.bind("hosp", HOSP)

    # Kelas
    g.add((HOSP.Pasien, RDF.type, RDFS.Class))
    g.add((HOSP.Dokter, RDF.type, RDFS.Class))
    g.add((HOSP.Perawat, RDF.type, RDFS.Class))
    g.add((HOSP.Ruangan, RDF.type, RDFS.Class))
    g.add((HOSP.Penyakit, RDF.type, RDFS.Class))
    g.add((HOSP.Obat, RDF.type, RDFS.Class))

    # Properti
    g.add((HOSP.dirawatOleh, RDF.type, RDF.Property))
    g.add((HOSP.mendiagnosa, RDF.type, RDF.Property))
    g.add((HOSP.menggunakanObat, RDF.type, RDF.Property))
    g.add((HOSP.beradaDiRuangan, RDF.type, RDF.Property))

    # Data contoh
    p1 = HOSP.Alice; g.add((p1, RDF.type, HOSP.Pasien)); g.add((p1, RDFS.label, Literal("Alice")))
    p2 = HOSP.Bob; g.add((p2, RDF.type, HOSP.Pasien)); g.add((p2, RDFS.label, Literal("Bob")))

    d1 = HOSP.Dr_Andi; g.add((d1, RDF.type, HOSP.Dokter)); g.add((d1, RDFS.label, Literal("Dr. Andi")))
    d2 = HOSP.Dr_Budi; g.add((d2, RDF.type, HOSP.Dokter)); g.add((d2, RDFS.label, Literal("Dr. Budi")))

    r1 = HOSP.Ruangan_A; g.add((r1, RDF.type, HOSP.Ruangan)); g.add((r1, RDFS.label, Literal("Ruang A")))
    r2 = HOSP.Ruangan_B; g.add((r2, RDF.type, HOSP.Ruangan)); g.add((r2, RDFS.label, Literal("Ruang B")))

    penyakit1 = HOSP.Demam; g.add((penyakit1, RDF.type, HOSP.Penyakit)); g.add((penyakit1, RDFS.label, Literal("Demam")))
    penyakit2 = HOSP.Influenza; g.add((penyakit2, RDF.type, HOSP.Penyakit)); g.add((penyakit2, RDFS.label, Literal("Influenza")))

    obat1 = HOSP.Paracetamol; g.add((obat1, RDF.type, HOSP.Obat)); g.add((obat1, RDFS.label, Literal("Paracetamol")))
    obat2 = HOSP.Antibiotik; g.add((obat2, RDF.type, HOSP.Obat)); g.add((obat2, RDFS.label, Literal("Antibiotik")))

    # Relasi
    g.add((p1, HOSP.dirawatOleh, d1))
    g.add((p2, HOSP.dirawatOleh, d2))

    g.add((d1, HOSP.mendiagnosa, penyakit1))
    g.add((d2, HOSP.mendiagnosa, penyakit2))

    g.add((p1, HOSP.menggunakanObat, obat1))
    g.add((p2, HOSP.menggunakanObat, obat2))

    g.add((p1, HOSP.beradaDiRuangan, r1))
    g.add((p2, HOSP.beradaDiRuangan, r2))

    return g
