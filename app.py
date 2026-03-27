from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return "API funcionando correctamente"

# Obtener usuarios de una API externa
@app.route('/users')
def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    return jsonify(response.json())

# Buscar con parámetro
@app.route('/search')
def search():
    query = request.args.get('q', '')
    return f"Buscando: {query}"

if __name__ == '__main__':
    app.run(debug=True)
