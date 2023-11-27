class SunScreen:
    def __init__(self, nama, harga, spf,kondisi_kulit, isi, finishing, formula, pa, tekstur, packaging, wangi ): 
        self.name = nama
        self.harga = harga
        self.spf = spf
        self.kondisi_kulit = kondisi_kulit
        self.isi = isi
        self.finishing = finishing
        self.formula = formula
        self.pa = pa
        self.tekstur = tekstur
        self.packaging = packaging
        self.wangi = wangi

# Daftar Alternatif SunScreen
alternatif_sunscreen = [
    SunScreen("Azarine", 4, 4, 4, 3, 4, 4, 4, 1, 1, 2),
    SunScreen("Skin Aqua", 4, 5, 4, 2, 1, 5, 2, 1, 2, 2),
    SunScreen("Biore", 4, 4, 3, 1, 4, 5, 3, 1, 1, 2),
    SunScreen("Wardah", 4, 2, 4, 2, 4, 5, 3, 1, 1, 2),
    SunScreen("Emina", 4, 1, 4, 4, 3, 4, 3, 1, 1, 2),
    SunScreen("The Originote", 4, 4, 4, 3, 1, 5, 4, 2, 3, 1),
    SunScreen("Annesa", 1, 4, 1, 5, 4, 1, 4, 3, 1, 2),
    SunScreen("Nivea", 4, 5, 2, 1, 1, 3, 3, 3, 1, 1),
    SunScreen("Banana Boat", 4, 5, 4, 3, 2, 2, 1, 4, 1, 2),
    SunScreen("Facetology", 4, 3, 4, 2, 1, 3, 3, 3, 2, 2)
]

def get_sunscreen_list():
    return alternatif_sunscreen



