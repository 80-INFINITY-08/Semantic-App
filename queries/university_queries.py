CQ1 = """
PREFIX uni: <http://example.org/university#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?dosenName WHERE {
  ?mk rdfs:label "Data Mining" .
  ?dosen uni:mengajarMataKuliah ?mk .
  ?dosen rdfs:label ?dosenName .
}
"""

CQ2 = """
PREFIX uni: <http://example.org/university#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?mhsName (COUNT(?mk) as ?jumlahMK) WHERE {
  ?mhs a uni:Mahasiswa .
  ?mhs rdfs:label ?mhsName .
  ?mhs uni:mengambilMataKuliah ?mk .
} GROUP BY ?mhsName ORDER BY DESC(?jumlahMK)
"""

CQ3 = """
PREFIX uni: <http://example.org/university#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT (COUNT(DISTINCT ?mhs) as ?jumlahMhs) WHERE {
  ?mk uni:beradaDiFakultas ?fak .
  ?fak rdfs:label "Teknik" .
  ?mhs uni:mengambilMataKuliah ?mk .
}
"""

CQ4 = """
PREFIX uni: <http://example.org/university#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?mkName WHERE {
  ?dosen rdfs:label "Dr. Andi" .
  ?dosen uni:mengajarMataKuliah ?mk .
  ?mk rdfs:label ?mkName .
}
"""

CQ5 = """
PREFIX uni: <http://example.org/university#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?mhsName WHERE {
  ?mhs a uni:Mahasiswa .
  ?mhs rdfs:label ?mhsName .
  ?mhs uni:mengambilMataKuliah ?mk .
} GROUP BY ?mhsName HAVING (COUNT(?mk) > 1)
"""
