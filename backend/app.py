from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/imc', methods=['POST'])
def calcul_imc():
    data = request.get_json()
    poids = data.get('poids')
    taille = data.get('taille')
    
    if not poids or not taille:
        return jsonify({'error': 'Données manquantes'}), 400

    imc = poids / (taille ** 2)
    return jsonify({'IMC': round(imc, 2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
