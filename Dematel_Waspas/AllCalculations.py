from SunScreen import get_sunscreen_list

def normalisasi_matriksKeputusan():
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
        
    print (kriteria_matriks)

    
    #Memisahkan status kriteria cost dan benefit
    # Memisahkan kolom pertama sebagai cost kriteria
    cost_criteria = [row[0] for row in kriteria_matriks]

    # Memisahkan kolom kedua sampai terakhir sebagai benefit kriteria
    benefit_criteria = [row[1:] for row in kriteria_matriks]

    # Output
    print("Cost Kriteria:")
    for nilai_cost in cost_criteria:
        print(nilai_cost)

    print("\nBenefit Kriteria:")
    for nilai_benefit in benefit_criteria:
        print(nilai_benefit)

    #normalisasi cost criteria
    # Normalisasi cost criteria
    min_value_cost = min(cost_criteria)
    normalized_cost_criteria = [min_value_cost / x if x != 0 else 0 for x in cost_criteria]

    # Output hasil normalisasi cost criteria
    print("Hasil Normalisasi Cost Criteria:")
    for normalized_value in normalized_cost_criteria:
        print(normalized_value)

    # print ("Cost Kriteria")
    # for row in cost_criteria:
    #     print(row)
    
        # Normalisasi benefit criteria
    max_values_benefit = [max(col) for col in zip(*benefit_criteria)]
    normalized_benefit_criteria = [[x / max_value for x, max_value in zip(row, max_values_benefit)] for row in benefit_criteria]

    # Output hasil normalisasi benefit criteria
    print("Hasil Normalisasi Benefit Criteria:")
    for row in normalized_benefit_criteria:
        print(row) 
    
    # print ("Benefit Kriteria")
    # for row in benefit_criteria:
    #     print(row)
     
        # Menggabungkan cost kriteria dan benefit kriteria
    combined_criteria = [[cost] + benefit for cost, benefit in zip(normalized_cost_criteria, normalized_benefit_criteria)]
    

    # Output hasil penggabungan
    print("Combined Criteria:")
    for row in combined_criteria:
        print(row)

    return combined_criteria

MatrixNormalisasi = normalisasi_matriksKeputusan()
print("Table Normalisasi Matriks Keputusan")
for row in MatrixNormalisasi:
        print(row)

print()

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
for i in range(len(MatrixNormalisasi)):
    Q_i = sum([data_bobot[kriteria] * MatrixNormalisasi[i][j] for j, kriteria in enumerate(data_bobot)])
    nilai_Q.append((i + 1, Q_i))


sunscreen_name = ["Azarine", "Skin Aqua", "Biore", "Wardah", "Emina", "The Originote", "Annesa", "Nivea", "Banana boat", "Facetology"]

for row in nilai_Q: 
    print(row)

# Sorting hasil perangkingan berdasarkan nilai Q
named_alternatif = list(zip(nilai_Q, sunscreen_name))

# Sorting hasil perangkingan berdasarkan nilai Q
named_alternatif.sort(key=lambda x: x[1], reverse=True)

named_only = []
for i in range(len(named_alternatif)):
    named_only.append(named_alternatif[i][1])

print(named_only)

print("Hasil Perangkingan:")
for rank, nilai in nilai_Q:
    print(f"Alternatif {rank}: Nilai Q = {nilai}")