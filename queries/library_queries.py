# CQ1: Semua buku di perpustakaan
CQ1 = """
PREFIX lib: <http://example.org/library#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?bukuName WHERE {
  ?buku a lib:Buku ;
        rdfs:label ?bukuName .
}
"""

# CQ2: Semua anggota perpustakaan
CQ2 = """
PREFIX lib: <http://example.org/library#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?anggotaName WHERE {
  ?anggota a lib:Anggota ;
           rdfs:label ?anggotaName .
}
"""

# CQ3: Buku dan penulisnya
CQ3 = """
PREFIX lib: <http://example.org/library#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?bukuName ?penulisName WHERE {
  ?buku a lib:Buku ;
        rdfs:label ?bukuName ;
        lib:ditulisOleh ?penulis .
  ?penulis rdfs:label ?penulisName .
}
"""

# CQ4: Anggota dan buku yang dipinjam
CQ4 = """
PREFIX lib: <http://example.org/library#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?anggotaName ?bukuName WHERE {
  ?anggota a lib:Anggota ;
           rdfs:label ?anggotaName ;
           lib:memilikiPeminjaman ?buku .
  ?buku rdfs:label ?bukuName .
}
"""

# CQ5: Penulis yang ada di perpustakaan
CQ5 = """
PREFIX lib: <http://example.org/library#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?penulisName WHERE {
  ?penulis a lib:Penulis ;
           rdfs:label ?penulisName .
}
"""
