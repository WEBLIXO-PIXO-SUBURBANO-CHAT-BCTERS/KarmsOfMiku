# hatsuneKarms.py (exemplo Flask)
from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

comentarios_db = {}  # Em produção, use um banco de dados real

@app.route('/api/comentarios', methods=['POST'])
def adicionar_comentario():
    data = request.get_json()
    
    novo_comentario = {
        'id': datetime.datetime.now().timestamp(),
        'carta_id': data['carta_id'],
        'usuario': data.get('usuario', 'Anônimo'),
        'texto': data['texto'],
        'data': datetime.datetime.now().isoformat()
    }
    
    # Adicionar ao "banco de dados"
    if data['carta_id'] not in comentarios_db:
        comentarios_db[data['carta_id']] = []
    
    comentarios_db[data['carta_id']].append(novo_comentario)
    
    return jsonify(novo_comentario), 201

@app.route('/api/comentarios/<carta_id>', methods=['GET'])
def obter_comentarios(carta_id):
    comentarios = comentarios_db.get(carta_id, [])
    return jsonify(comentarios)

if __name__ == '__main__':
    app.run(debug=True)
