# Contoh CQ interaktif
CQ1_TEMPLATE = """
PREFIX eco: <http://example.org/ecommerce#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?produkName ?harga ?rating WHERE {{
  ?kategori rdfs:label "{kategori}" .
  ?produk eco:memilikiKategori ?kategori .
  ?produk rdfs:label ?produkName .
  ?produk eco:harga ?harga .
  ?produk eco:rating ?rating .
}}
ORDER BY DESC(?rating)
"""

CQ2_TEMPLATE = """
PREFIX eco: <http://example.org/ecommerce#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?penjualName WHERE {{
  ?produk rdfs:label "{produk}" .
  ?penjual eco:menjual ?produk .
  ?penjual rdfs:label ?penjualName .
}}
"""
# Template SPARQL dengan parameter {kategori}, {produk}, {pelanggan}, {rating}, {diskon}

CQ13_TEMPLATE = """
PREFIX eco: <http://example.org/ecommerce#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?produkName ?harga ?brandName WHERE {{
  ?kategori rdfs:label "{kategori}" .
  ?produk eco:memilikiKategori ?kategori ;
          rdfs:label ?produkName ;
          eco:harga ?harga ;
          eco:memilikiBrand ?brand .
  ?brand rdfs:label ?brandName .
  FILTER (?harga < {harga_max})
}}
ORDER BY ?harga
"""

CQ15 = """
PREFIX eco: <http://example.org/ecommerce#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?penjualName (COUNT(?produk) as ?jumlahProduk) WHERE {
  ?penjual a eco:Penjual ;
           rdfs:label ?penjualName ;
           eco:menjual ?produk .
}
GROUP BY ?penjualName
ORDER BY DESC(?jumlahProduk)
"""

CQ17_TEMPLATE = """
PREFIX eco: <http://example.org/ecommerce#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?pelangganName ?email WHERE {{
  ?pelanggan a eco:Pelanggan ;
             rdfs:label ?pelangganName ;
             eco:email ?email ;
             eco:alamat "{kota}" .
}}
"""

CQ20_TEMPLATE = """
PREFIX eco: <http://example.org/ecommerce#>
SELECT ?produkName ?harga ?diskon ?hargaDiskon WHERE {{
  ?produk a eco:Produk ;
          rdfs:label ?produkName ;
          eco:harga ?harga ;
          eco:memilikiPromo ?promo .
  ?promo eco:diskonPersen ?diskon .
  BIND(?harga * (1 - (?diskon / 100)) as ?hargaDiskon)
  FILTER (?diskon > {diskon_min})
}}
ORDER BY DESC(?diskon)
"""