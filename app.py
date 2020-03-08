from flask import Flask, jsonify, request
import json

app = Flask(__name__);

desenvolvedores = [
    {'nome':'Alvason',
     'habilidades':['Python','Flask']
     },
    {'nome':'Alvaro',
     'habilidades':['Python','HTML5']
     }

]

@app.route('/dev/<int:id>/', methods=['GET','PUT'])
def desenvolvedor(id):
    if request.method == 'GET':
        desenvolvedor = desenvolvedores[id]
        return jsonify(desenvolvedor)
    elif request.method == 'PUT':
         dados = json.loads(request.data)
         desenvolvedores[id] = dados
         return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)