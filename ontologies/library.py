from rdflib import Graph, Namespace, RDF, RDFS, Literal
from rdflib.namespace import XSD

LIB = Namespace("http://example.org/library#")

def build_library_graph():
    g = Graph()
    g.bind("lib", LIB)

    # Kelas
    g.add((LIB.Buku, RDF.type, RDFS.Class))
    g.add((LIB.Anggota, RDF.type, RDFS.Class))
    g.add((LIB.Peminjaman, RDF.type, RDFS.Class))
    g.add((LIB.Penulis, RDF.type, RDFS.Class))

    # Data contoh
    buku1 = LIB.HarryPotter; g.add((buku1, RDF.type, LIB.Buku)); g.add((buku1, RDFS.label, Literal("Harry Potter")))
    buku2 = LIB.LaskarPelangi; g.add((buku2, RDF.type, LIB.Buku)); g.add((buku2, RDFS.label, Literal("Laskar Pelangi")))
    buku3 = LIB.Alchemist; g.add((buku3, RDF.type, LIB.Buku)); g.add((buku3, RDFS.label, Literal("The Alchemist")))

    anggota1 = LIB.Alice; g.add((anggota1, RDF.type, LIB.Anggota)); g.add((anggota1, RDFS.label, Literal("Alice")))
    anggota2 = LIB.Bob; g.add((anggota2, RDF.type, LIB.Anggota)); g.add((anggota2, RDFS.label, Literal("Bob")))

    penulis1 = LIB.Rowling; g.add((penulis1, RDF.type, LIB.Penulis)); g.add((penulis1, RDFS.label, Literal("J.K. Rowling")))
    penulis2 = LIB.Hirata; g.add((penulis2, RDF.type, LIB.Penulis)); g.add((penulis2, RDFS.label, Literal("Andrea Hirata")))
    penulis3 = LIB.Coehlo; g.add((penulis3, RDF.type, LIB.Penulis)); g.add((penulis3, RDFS.label, Literal("Paulo Coehlo")))

    # Relasi
    g.add((buku1, LIB.ditulisOleh, penulis1))
    g.add((buku2, LIB.ditulisOleh, penulis2))
    g.add((buku3, LIB.ditulisOleh, penulis3))

    g.add((anggota1, LIB.memilikiPeminjaman, buku1))
    g.add((anggota1, LIB.memilikiPeminjaman, buku2))
    g.add((anggota2, LIB.memilikiPeminjaman, buku3))

    return g
