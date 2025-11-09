from rdflib import Graph, Namespace, RDF, RDFS, Literal
from rdflib.namespace import XSD, FOAF

ECO = Namespace("http://example.org/ecommerce#")

def build_ecommerce_graph():
    g = Graph()
    g.bind("eco", ECO)
    g.bind("foaf", FOAF)

    # Tambahkan kelas, properti, data sesuai file ontologi yang kamu punya
        # Kelas utama
    classes = [
        ECO.User, ECO.Pelanggan, ECO.Penjual, ECO.Admin,
        ECO.Product, ECO.Produk, ECO.Kategori, ECO.Brand,
        ECO.Transaction, ECO.Pesanan, ECO.Pembayaran, ECO.Pengiriman,
        ECO.Review, ECO.Rating, ECO.Ulasan, ECO.Keranjang, ECO.Promo
    ]

    for cls in classes:
        g.add((cls, RDF.type, RDFS.Class))

    # Properti relasional
    object_properties = [
        ECO.membeli, ECO.menjual, ECO.memilikiKategori, ECO.termasukDalam,
        ECO.memberikanReview, ECO.memilikiBrand, ECO.memilikiPesanan,
        ECO.berisiProduk, ECO.memilikiStatus, ECO.dibeliDari, ECO.untukProduk,
        ECO.memilikiItemKeranjang, ECO.memilikiPromo, ECO.terapkanPromo
    ]

    for prop in object_properties:
        g.add((prop, RDF.type, RDF.Property))
        g.add((prop, RDFS.domain, ECO.User))  # Domain umum, bisa disesuaikan
        g.add((prop, RDFS.range, ECO.User))   # Range umum, bisa disesuaikan

    # Properti data
    data_properties = [
        ECO.nama, ECO.email, ECO.harga, ECO.stok, ECO.rating,
        ECO.tanggalPesanan, ECO.total, ECO.kuantitas, ECO.deskripsi,
        ECO.tanggalMulai, ECO.tanggalAkhir, ECO.diskonPersen, ECO.alamat,
        ECO.telepon, ECO.berat, ECO.sku, ECO.statusPembayaran
    ]

    for prop in data_properties:
        g.add((prop, RDF.type, RDF.Property))
        # (disingkat di sini, tapi kamu bisa copy isi dari file g = Graph().txt)

        # Contoh sederhana:
        #g.add((ECO.Produk, RDF.type, RDFS.Class))
        #g.add((ECO.Kategori, RDF.type, RDFS.Class))
        #g.add((ECO.Brand, RDF.type, RDFS.Class))
 
    # Tambahkan data produk, kategori, brand, pelanggan, penjual, promo, dll.
    # ---------- Tambah contoh data lebih banyak ----------

    # Kategori
    kategori_data = {
        "Elektronik": "Perangkat elektronik dan gadget",
        "Pakaian": "Fashion pakaian pria dan wanita",
        "Olahraga": "Perlengkapan olahraga",
        "Rumah_Tangga": "Perabotan rumah tangga",
        "Kecantikan": "Kosmetik dan perawatan tubuh"
    }

    for name, desc in kategori_data.items():
        uri = getattr(ECO, name)
        g.add((uri, RDF.type, ECO.Kategori))
        g.add((uri, RDFS.label, Literal(name)))
        g.add((uri, ECO.deskripsi, Literal(desc)))

    # Brand
    brands_data = {
        "Samsung": "Teknologi dan elektronik",
        "Nike": "Olahraga dan athleisure",
        "Uniqlo": "Fashion casual",
        "IKEA": "Furnitur rumah tangga",
        "Sephora": "Kecantikan dan kosmetik",
        "Apple": "Teknologi premium"
    }

    for name, desc in brands_data.items():
        uri = getattr(ECO, name)
        g.add((uri, RDF.type, ECO.Brand))
        g.add((uri, RDFS.label, Literal(name)))
        g.add((uri, ECO.deskripsi, Literal(desc)))

    # Produk dengan variasi lebih banyak
    produk_data = [
        ("Smartphone_X", "Smartphone X", 5000000, 50, 4.7, "Elektronik", "Samsung"),
        ("Laptop_Gaming", "Laptop Gaming", 15000000, 25, 4.5, "Elektronik", "Samsung"),
        ("Sepatu_Lari", "Sepatu Lari Nike Air", 800000, 100, 4.8, "Olahraga", "Nike"),
        ("Kaos_Polos", "Kaos Polos Cotton", 150000, 200, 4.2, "Pakaian", "Uniqlo"),
        ("Meja_Kerja", "Meja Kerja Minimalis", 1200000, 30, 4.6, "Rumah_Tangga", "IKEA"),
        ("Lipstick_Matte", "Lipstick Matte 24h", 250000, 80, 4.4, "Kecantikan", "Sephora"),
        ("iPhone_15", "iPhone 15 Pro", 18000000, 15, 4.9, "Elektronik", "Apple"),
        ("Jaket_Olahraga", "Jaket Olahraga Windproof", 450000, 60, 4.3, "Olahraga", "Nike")
    ]

    for pid, name, harga, stok, rating, kategori, brand in produk_data:
        uri = getattr(ECO, pid)
        g.add((uri, RDF.type, ECO.Produk))
        g.add((uri, RDFS.label, Literal(name)))
        g.add((uri, ECO.harga, Literal(harga, datatype=XSD.integer)))
        g.add((uri, ECO.stok, Literal(stok, datatype=XSD.integer)))
        g.add((uri, ECO.rating, Literal(rating, datatype=XSD.float)))
        g.add((uri, ECO.memilikiKategori, getattr(ECO, kategori)))
        g.add((uri, ECO.memilikiBrand, getattr(ECO, brand)))
        g.add((uri, ECO.sku, Literal(f"SKU-{pid}")))

    # Penjual
    penjual_data = [
        ("Toko_Elektronik_Berkah", "berkah@example.com", ["Smartphone_X", "Laptop_Gaming"]),
        ("Sports_World", "sports@example.com", ["Sepatu_Lari", "Jaket_Olahraga"]),
        ("Fashion_Store", "fashion@example.com", ["Kaos_Polos"]),
        ("Home_Decor", "home@example.com", ["Meja_Kerja"]),
        ("Beauty_Hub", "beauty@example.com", ["Lipstick_Matte"]),
        ("Tech_Premium", "tech@example.com", ["iPhone_15"])
    ]

    for name, email, produk_list in penjual_data:
        uri = getattr(ECO, name.replace(" ", "_"))
        g.add((uri, RDF.type, ECO.Penjual))
        g.add((uri, RDFS.label, Literal(name)))
        g.add((uri, ECO.email, Literal(email)))
        for produk in produk_list:
            g.add((uri, ECO.menjual, getattr(ECO, produk)))

    # Pelanggan
    pelanggan_data = [
        ("Alice", "alice@example.com", "Jakarta"),
        ("Bob", "bob@example.com", "Bandung"),
        ("Charlie", "charlie@example.com", "Surabaya"),
        ("Diana", "diana@example.com", "Medan"),
        ("Eve", "eve@example.com", "Bali")
    ]

    for name, email, alamat in pelanggan_data:
        uri = getattr(ECO, name)
        g.add((uri, RDF.type, ECO.Pelanggan))
        g.add((uri, RDFS.label, Literal(name)))
        g.add((uri, ECO.email, Literal(email)))
        g.add((uri, ECO.alamat, Literal(alamat)))

    # Promo
    promo_data = [
        ("Promo_October", "Promo Oktober", 10, "2025-10-01", "2025-10-31"),
        ("Promo_Welcome", "Promo Welcome", 15, "2025-10-01", "2025-12-31"),
        ("Promo_Elektronik", "Promo Elektronik", 5, "2025-10-15", "2025-11-15")
    ]

    for pid, name, diskon, mulai, akhir in promo_data:
        uri = getattr(ECO, pid)
        g.add((uri, RDF.type, ECO.Promo))
        g.add((uri, RDFS.label, Literal(name)))
        g.add((uri, ECO.diskonPersen, Literal(diskon, datatype=XSD.integer)))
        g.add((uri, ECO.tanggalMulai, Literal(mulai, datatype=XSD.date)))
        g.add((uri, ECO.tanggalAkhir, Literal(akhir, datatype=XSD.date)))


    return g
