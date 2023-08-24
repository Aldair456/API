from flask import Flask,request,jsonify
import json
app= Flask(__name__)
with open('date.json', 'r') as json_file:
    data = json.load(json_file)
animes=data
@app.route('/anime',methods=['GET'])
def anime():
    return animes
@app.route('/anime/<int:id>',methods=['GET'])
def busqueda(id):
    return  animes[id]

@app.route('/anime',methods=['POST'])
def Create():
    new_date=request.json
    animes.append(new_date)
    return animes

@app.route('/anime/<int:id>', methods=['PUT'])
def Cambio_total(id):
    data = request.json
    if id < 0 or id >= len(animes):
        return jsonify({"message": "Anime no encontrado"}), 404
    else:
        animes[id]=data
        return animes

@app.route('/anime/<int:id>', methods=['DELETE'])

def Eliminar(id):
    if id < 0 or id >= len(animes):
        return jsonify({"message": "Anime no encontrado"}),
    else:
        animes.pop(id)
        return animes
@app.route('/anime/<int:id>', methods=['PATCH'])

def CambioParcial(id):
    data = request.json
    if id < 0 or id >= len(animes):
        return jsonify({"message": "Anime no encontrado"}), 404
    else:
        anime = animes[id]
        for key, value in data.items():
            if key in anime:
                anime[key] = value
        return animes
    


# Cargar el archivo JSON
