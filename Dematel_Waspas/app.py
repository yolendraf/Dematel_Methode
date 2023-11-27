from flask import Flask, render_template, request, jsonify
from logic import SunscreenDematelWaspas
import json


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_sunscreen_data')
def get_sunscreen_data():
    with open('Dematel_Waspas\DataSet\sunscreen_list.json', 'r') as file:
        sunscreen_list = json.load(file)
    return jsonify(sunscreen_list)

@app.route('/hitung_keputusan', methods=['POST'])
def process_dropdown():
    criteria1 = request.form['criteria1']
    criteria2 = request.form['criteria2']
    criteria3 = request.form['criteria3']
    criteria4 = request.form['criteria4']
    criteria5 = request.form['criteria5']
    criteria6 = request.form['criteria6']
    criteria7 = request.form['criteria7']
    criteria8 = request.form['criteria8']
    criteria9 = request.form['criteria9']
    criteria10 = request.form['criteria10']

    print("Nilai Criteria 1:", criteria1)
    print("Nilai Criteria 2:", criteria2)
    print("Nilai Criteria 3:", criteria3)
    print("Nilai Criteria 4:", criteria4)
    print("Nilai Criteria 5:", criteria5)
    print("Nilai Criteria 6:", criteria6)
    print("Nilai Criteria 7:", criteria7)
    print("Nilai Criteria 8:", criteria8)
    print("Nilai Criteria 9:", criteria9)
    print("Nilai Criteria 10:", criteria10)

    if request.method == 'POST':
        preferensi_harga = request.form['criteria1']
        preferensi_spf = request.form['criteria2']
        preferensi_kondisi_kulit = request.form['criteria3']
        preferensi_isi = request.form['criteria4']
        preferensi_finishing = request.form['criteria5']
        preferensi_pa = request.form['criteria6']
        preferensi_tekstur = request.form['criteria7']
        preferensi_packaging = request.form['criteria8']
        preferensi_wangi = request.form['criteria9']
        preferensi_formula = request.form['criteria10']


        hasil_keputusan = SunscreenDematelWaspas.hitung_sistem_keputusan(
            harga=preferensi_harga,
            spf=preferensi_spf,
            kondisi_kulit = preferensi_kondisi_kulit,
            isi = preferensi_isi,
            finishing = preferensi_finishing,
            pa = preferensi_pa,
            tekstur = preferensi_tekstur,
            packaging = preferensi_packaging,
            wangi = preferensi_wangi,
            formula = preferensi_formula
        )

        print(hasil_keputusan)

        return jsonify({'hasil_keputusan': hasil_keputusan})
    
if __name__ == '__main__':
    app.run(debug=True)

