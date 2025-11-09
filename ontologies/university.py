from rdflib import Graph, Namespace, RDF, RDFS, Literal
from rdflib.namespace import XSD

UNI = Namespace("http://example.org/university#")

def build_university_graph():
    g = Graph()
    g.bind("uni", UNI)

    # Kelas
    g.add((UNI.Mahasiswa, RDF.type, RDFS.Class))
    g.add((UNI.Dosen, RDF.type, RDFS.Class))
    g.add((UNI.MataKuliah, RDF.type, RDFS.Class))
    g.add((UNI.Fakultas, RDF.type, RDFS.Class))

    # Properti
    g.add((UNI.mengambilMataKuliah, RDF.type, RDF.Property))
    g.add((UNI.mengajarMataKuliah, RDF.type, RDF.Property))
    g.add((UNI.beradaDiFakultas, RDF.type, RDF.Property))

    # Data contoh
    m1 = UNI.Alice; g.add((m1, RDF.type, UNI.Mahasiswa)); g.add((m1, RDFS.label, Literal("Alice")))
    m2 = UNI.Bob; g.add((m2, RDF.type, UNI.Mahasiswa)); g.add((m2, RDFS.label, Literal("Bob")))

    d1 = UNI.Dr_Andi; g.add((d1, RDF.type, UNI.Dosen)); g.add((d1, RDFS.label, Literal("Dr. Andi")))
    d2 = UNI.Dr_Budi; g.add((d2, RDF.type, UNI.Dosen)); g.add((d2, RDFS.label, Literal("Dr. Budi")))

    mk1 = UNI.DataMining; g.add((mk1, RDF.type, UNI.MataKuliah)); g.add((mk1, RDFS.label, Literal("Data Mining")))
    mk2 = UNI.Algoritma; g.add((mk2, RDF.type, UNI.MataKuliah)); g.add((mk2, RDFS.label, Literal("Algoritma")))

    f1 = UNI.Teknik; g.add((f1, RDF.type, UNI.Fakultas)); g.add((f1, RDFS.label, Literal("Teknik")))

    # Relasi
    g.add((m1, UNI.mengambilMataKuliah, mk1))
    g.add((m1, UNI.mengambilMataKuliah, mk2))
    g.add((m2, UNI.mengambilMataKuliah, mk1))

    g.add((d1, UNI.mengajarMataKuliah, mk1))
    g.add((d2, UNI.mengajarMataKuliah, mk2))

    g.add((mk1, UNI.beradaDiFakultas, f1))
    g.add((mk2, UNI.beradaDiFakultas, f1))

    return g
