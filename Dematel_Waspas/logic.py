from SunScreen import get_sunscreen_list

class SunscreenDematelWaspas:
    range_harga = ["< 100k", "101k - 200k", "201k - 300k", "> 300k"]
    range_spf = [ "30", "35", "40", "50", "50+"]
    range_kondisi_kulit = ["kering", "kombinasi", "berminyak", "semua tipe kulit"]
    range_isi = ["30", "40", "50", "60", "90"]
    range_finishing = ["glow", "semi-glow", "matte-glow", "matte"]
    range_formula = ["mild-milk", "lotion-watery-cream", "cream-watery", "gel", "water-base"]
    range_pa = ["pa", "pa-plus", "pa-plus-plus", "pa-plus-plus-plus", "pa-plus-plus-plus-plus"]
    range_tekstur = ["kental", "cream-watery", "creamy", "cair"]
    range_packaging = ["tube", "botol", "tube-spay"]
    range_wangi = ["berbau", "tidak-berbau"]

    @staticmethod
    def hitung_bobot_harga(self, harga):
        if harga == self.range_harga[0]:
            return 4 
        elif harga == self.range_harga[1]:
            return 3
        elif harga == self.range_harga[2]:
            return 2
        elif harga == self.range_harga[3]:
            return 1
        else:
            return 0
        
    @staticmethod
    def hitung_bobot_spf(self, spf):
        if spf == self.range_spf[0]:
            return 1
        elif spf == self.range_spf[1]:
            return 2
        elif spf == self.range_spf[2]:
            return 3
        elif spf == self.range_spf[3]:
            return 4
        elif spf == self.range_spf[4]:
            return 5
        else:
            return 0
        
    @staticmethod
    def hitung_bobot_kondisi_kulit(self, kondisi_kulit):
        if kondisi_kulit == self.range_kondisi_kulit[0]:
            return 1
        elif kondisi_kulit == self.range_kondisi_kulit[1]:
            return 2
        elif kondisi_kulit == self.range_kondisi_kulit[2]:
            return 3
        elif kondisi_kulit == self.range_kondisi_kulit[3]:
            return 4
        else:
            return 0
        
    
    @staticmethod
    def hitung_bobot_isi(self, isi):
        if isi == self.range_isi[0]:
            return 1
        elif isi == self.range_isi[1]:
            return 2
        elif isi == self.range_isi[2]:
            return 3
        elif isi == self.range_isi[3]:
            return 4
        elif isi == self.range_isi[4]:
            return 5
        else:
            return 0

    @staticmethod
    def hitung_bobot_finishing(self, finishing):
        if finishing == self.range_finishing[0]:
            return 1
        elif finishing == self.range_finishing[1]:
            return 2
        elif finishing == self.range_finishing[2]:
            return 3
        elif finishing == self.range_finishing[3]:
            return 4
        else:
            return 0

    @staticmethod
    def hitung_bobot_formula(self, formula):
        if formula == self.range_formula[0]:
            return 1
        elif formula == self.range_formula[1]:
            return 2
        elif formula == self.range_formula[2]:
            return 3
        elif formula == self.range_formula[3]:
            return 4
        elif formula == self.range_formula[4]:
            return 5
        else:
            return 0

    @staticmethod
    def hitung_bobot_pa(self, pa):
        if pa == self.range_pa[0]:
            return 1
        elif pa == self.range_pa[1]:
            return 2
        elif pa == self.range_pa[2]:
            return 3
        elif pa == self.range_pa[3]:
            return 4
        elif pa == self.range_pa[4]:
            return 5
        else:
            return 0

    @staticmethod
    def hitung_bobot_tekstur(self, tekstur):
        if tekstur == self.range_tekstur[0]:
            return 1
        elif tekstur == self.range_tekstur[1]:
            return 2
        elif tekstur == self.range_tekstur[2]:
            return 3
        elif tekstur == self.range_tekstur[3]:
            return 4
        else:
            return 0
        
    @staticmethod
    def hitung_bobot_packaging(self, packaging):
        if packaging == self.range_packaging[0]:
            return 1
        elif packaging == self.range_packaging[1]:
            return 2
        elif packaging == self.range_packaging[2]:
            return 3
        else:
            return 0
        
    @staticmethod
    def hitung_bobot_wangi(self, wangi):
        if wangi == self.range_wangi[0]:
            return 1
        elif wangi == self.range_wangi[1]:
            return 2
        else:
            return 0   
        
    @staticmethod
    def matrix_kriteria(self):
        kriteria_matriks = []
        
        for SunScreen in self.alternatif_sunscreen:
            kriteria_SunScreen =[
                SunScreen.harga,
                SunScreen.spf,
                SunScreen.kondisi_kulit,
                SunScreen.isi,
                SunScreen.finishing,
                SunScreen.formula,
                SunScreen.pa,
                SunScreen.tekstur,
                SunScreen.packaging,
                SunScreen.wangi
            ]
            kriteria_matriks.append(kriteria_SunScreen)

        return kriteria_SunScreen
    
    @staticmethod
    def hitung_sistem_keputusan(harga, spf, kondisi_kulit, isi, finishing, formula, pa, tekstur, packaging, wangi):
        preferensi_harga = SunscreenDematelWaspas.hitung_bobot_harga(SunscreenDematelWaspas, harga)
        preferensi_spf = SunscreenDematelWaspas.hitung_bobot_spf(SunscreenDematelWaspas, spf)
        preferensi_kondisi_kulit = SunscreenDematelWaspas.hitung_bobot_kondisi_kulit(SunscreenDematelWaspas, kondisi_kulit)
        preferensi_kondisi_kulit = SunscreenDematelWaspas.hitung_bobot_kondisi_kulit(SunscreenDematelWaspas, kondisi_kulit)
        preferensi_isi = SunscreenDematelWaspas.hitung_bobot_isi(SunscreenDematelWaspas, isi)
        preferensi_finishing = SunscreenDematelWaspas.hitung_bobot_finishing(SunscreenDematelWaspas, finishing)
        preferensi_formula = SunscreenDematelWaspas.hitung_bobot_formula(SunscreenDematelWaspas, formula)
        preferensi_pa = SunscreenDematelWaspas.hitung_bobot_pa(SunscreenDematelWaspas, pa)
        preferensi_tekstur = SunscreenDematelWaspas.hitung_bobot_tekstur(SunscreenDematelWaspas, tekstur)
        preferensi_packaging = SunscreenDematelWaspas.hitung_bobot_packaging(SunscreenDematelWaspas, packaging)
        preferensi_wangi = SunscreenDematelWaspas.hitung_bobot_wangi(SunscreenDematelWaspas, wangi)

        normalisasi_table = SunscreenDematelWaspas.normalisasi_matriksKeputusan(preferensi_harga, preferensi_spf, preferensi_kondisi_kulit, preferensi_isi, preferensi_finishing, preferensi_formula, preferensi_pa,preferensi_tekstur, preferensi_packaging, preferensi_wangi)

        hasil_perangkingan = SunscreenDematelWaspas.hitung_perangkingan(normalisasi_table)

        return hasil_perangkingan
    
    @staticmethod
    def normalisasi_matriksKeputusan(preferensi_harga, preferensi_spf, preferensi_kondisi_kulit, preferensi_isi, preferensi_finishing, preferensi_formula, preferensi_pa,preferensi_tekstur, preferensi_packaging, preferensi_wangi):
        kriteria_matriks = []
        alternatif_sunscreen = get_sunscreen_list()
        for SunScreen in alternatif_sunscreen:
            kriteria_SunScreen =[
                SunScreen.harga,
                SunScreen.spf,
                SunScreen.kondisi_kulit,
                SunScreen.isi,
                SunScreen.finishing,
                SunScreen.formula,
                SunScreen.pa,
                SunScreen.tekstur,
                SunScreen.packaging,
                SunScreen.wangi
            ]
            kriteria_matriks.append(kriteria_SunScreen)

        #Memisahkan status kriteria cost dan benefit
        # Memisahkan kolom pertama sebagai cost kriteria
        cost_criteria = [row[0] for row in kriteria_matriks]

        # Memisahkan kolom kedua sampai terakhir sebagai benefit kriteria
        benefit_criteria = [row[1:] for row in kriteria_matriks]

        # Normalisasi cost criteria
        min_value_cost = min(cost_criteria)
        normalized_cost_criteria = [min_value_cost / x if x != 0 else 0 for x in cost_criteria]

        # Normalisasi benefit criteria
        max_values_benefit = [max(col) for col in zip(*benefit_criteria)]
        normalized_benefit_criteria = [[x / max_value for x, max_value in zip(row, max_values_benefit)] for row in benefit_criteria]

        # Menggabungkan cost kriteria dan benefit kriteria
        combined_criteria = [[cost] + benefit for cost, benefit in zip(normalized_cost_criteria, normalized_benefit_criteria)]
        return combined_criteria
    
    @staticmethod
    def hitung_perangkingan(data_normalisasi):
        # Data bobot kriteria
        data_bobot = {
            'Harga': 0.10,
            'SPF': 0.10,
            'Kondisi_Kulit': 0.15,
            'Isi': 0.08,
            'Finishing': 0.12,
            'Formula': 0.10,
            'PA': 0.10,
            'Tekstur': 0.08,
            'Packaging': 0.10,
            'Wangi': 0.07
        }

        # Hitung nilai Q untuk setiap alternatif
        nilai_Q = []
        for i in range(len(data_normalisasi)):
            Q_i = sum([data_bobot[kriteria] * data_normalisasi[i][j] for j, kriteria in enumerate(data_bobot)])
            nilai_Q.append((i + 1, Q_i))

        sunscreen_name = ["Azarine", "Skin Aqua", "Biore", "Wardah", "Emina", "The Originote", "Annesa", "Nivea", "Banana boat", "Facetology"]

        named_alternatif = list(zip(nilai_Q, sunscreen_name))

        # Sorting hasil perangkingan berdasarkan nilai Q
        named_alternatif.sort(key=lambda x: x[1], reverse=True)

        named_only = []
        for i in range(len(named_alternatif)):
            named_only.append(named_alternatif[i][1])

        return named_only
