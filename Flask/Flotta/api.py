from flask import Flask, jsonify, url_for, request
from main import Veichle, Car, Van, c1, v1, fm1

app = Flask(__name__)


parametri:list[str] = ['id_targa', 'veichle_type', 'model', 'driver_name', 'registration_year', 'status']
param_car:list[str] = ['doors', 'is_cabrio']
param_van:list[str] = ['max_load_kg', 'require_special_license']

def create_veichle_from_data(data:dict, plate_id) -> Veichle:
    if 'veichle_type' not in data:
        raise ValueError()



@app.route('/')
def get_info():
    result : dict = {
        "message": "Welcome to Rent Center API",
        "links": {
            "vehicles_list": /vehicles,
            "vehicle_sample": /vehicles/HA014AS,
            "estimate_sample": /devices/HA014AS/prep-time/2.0
        }
        }

@app.route('/veichles',  method=['GET'])
def get_veichles():
    return jsonify(fm1.list_all())

@app.route('/veichles/<string:plate_id', method=['GET'])
def get_single_veichle(plate_id:str):
    if plate_id not in fm1:
        return jsonify({'error': f'Non esiste veicolo con la targa {plate_id}'})
    return jsonify(fm1.get(plate_id).info())

@app.route('/veicles', method=['POST'])
def post_veichle():
    data: dict = request.get_json()
    for p in parametri:
        if p not in data:
            return jsonify({'errore': f'manca il campo di \'{p}\' nel body'})
    if data['veichle_type']  == 'car':
        for p in param_car:
            if p not in data:
                return jsonify({'errore': f'manca il campo di \'{p}\' nel body'})
    if data['veichle_type']  == 'van':
        for p in param_van:
            if p not in data:
                return jsonify({'errore': f'manca il campo di \'{p}\' nel body'})
    veichle : Car

    


