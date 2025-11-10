# CQ1: Siapa dokter yang merawat pasien tertentu?
CQ1_TEMPLATE = """
PREFIX hosp: <http://example.org/hospital#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?dokterName WHERE {{
  ?pasien rdfs:label "{pasien}" .
  ?pasien hosp:dirawatOleh ?dokter .
  ?dokter rdfs:label ?dokterName .
}}
"""

# CQ2: Pasien yang berada di ruangan tertentu
CQ2_TEMPLATE = """
PREFIX hosp: <http://example.org/hospital#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?pasienName WHERE {{
  ?ruangan rdfs:label "{ruangan}" .
  ?pasien hosp:beradaDiRuangan ?ruangan .
  ?pasien rdfs:label ?pasienName .
}}
"""

# CQ3: Penyakit yang didiagnosa oleh dokter tertentu
CQ3_TEMPLATE = """
PREFIX hosp: <http://example.org/hospital#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?penyakitName WHERE {{
  ?dokter rdfs:label "{dokter}" .
  ?dokter hosp:mendiagnosa ?penyakit .
  ?penyakit rdfs:label ?penyakitName .
}}
"""

# CQ4: Obat yang digunakan pasien tertentu
CQ4_TEMPLATE = """
PREFIX hosp: <http://example.org/hospital#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?obatName ?pasienName WHERE {
  ?pasien a hosp:Pasien ;
            rdfs:label ?pasienName ;
            hosp:menggunakanObat ?obat .
  ?obat rdfs:label ?obatName .
}
"""

# CQ5: Pasien dan dokter yang merawatnya
CQ5 = """
PREFIX hosp: <http://example.org/hospital#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?pasienName ?dokterName WHERE {
  ?pasien a hosp:Pasien ;
          rdfs:label ?pasienName ;
          hosp:dirawatOleh ?dokter .
  ?dokter rdfs:label ?dokterName .
}
"""
