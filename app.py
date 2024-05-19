from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def penjumlahan():
    return render_template('penjumlahan.html')

@app.route('/pengurangan')
def pengurangan():
    return render_template('pengurangan.html')

@app.route('/perkalian')
def perkalian():
    return render_template('perkalian.html')

@app.route('/pembagian')
def pembagian():
    return render_template('pembagian.html')

@app.route('/result', methods=["POST"])
def result():
    data = request.json
    angka1 = data['angka1']
    angka2 = data['angka2']
    result = angka1 + angka2
    
    return jsonify({"Hasil": result})

@app.route('/result_pengurangan', methods=["POST"])
def result_pengurangan():
    data = request.json
    angka1 = data['angka1']
    angka2 = data['angka2']
    result = angka1 - angka2
    
    return jsonify({"Hasil": result})

@app.route('/result_perkalian', methods=["POST"])
def result_perkalian():
    data = request.json
    angka1 = data['angka1']
    angka2 = data['angka2']
    result = angka1 * angka2
    
    return jsonify({"Hasil": result})

@app.route('/result_pembagian', methods=["POST"])
def result_pembagian():
    data = request.json
    angka1 = data['angka1']
    angka2 = data['angka2']
    result = angka1 // angka2
    
    return jsonify({"Hasil": result})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)