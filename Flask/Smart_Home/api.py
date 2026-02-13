from flask import Flask, jsonify, request, url_for
from iotHub import SmartDevice, SmartBulb, SecurityCamera, IoTHub

sb: SmartBulb = SmartBulb(
    serial_number="SN-101",
    brand="Nest",
    room="Living Room",
    installation_year=2021,
    status="online",
    brightness_lumens=800,
    color_capability=True, 
)

sc: SecurityCamera = SecurityCamera(
    serial_number="SN-202",
    brand="Ring",
    room="Entrance",
    installation_year=2020,
    status="offline",
    resolution="1080p",
    night_vision=True,
)

iot_hub = IoTHub()

iot_hub.add(sb)
iot_hub.add(sc)


app = Flask(__name__)


# Route GET

# GET /
# Restituisce un JSON con:
#     una breve descrizione del servizio, ad esempio: "Smart Home Hub API";
#     link testuali che indicano le altre route attualmente disponibili, generati dinamicamente con url_for(), ad esempio:
#         /devices,
#         /devices/SN-101,
#         /devices/SN-101/diagnostics/1.0
# Il JSON potrebbe avere una struttura tipo:
# {
#     "message": "Smart Home Hub API",
#     "links": {
#         "device_list": /devices,
#         "device_sample": /devices/SN-101,
#         "estimate_sample": /devices/SN-101/diagnostic/1.0)
#     }
# }

@app.route('/')
def get():
    return jsonify({
        'info': 'Smart Home Hub',
        'links': {
            "device_list": url_for('get_devices'),
            "device_sample": url_for('get_device', serial_number='SN-101'),
            "estimate_sample": url_for('get_diagnostic', serial_number='SN-101', factor=1.0)
        }
    })

# GET /devices
# Restituisce un JSON con l'elenco di tutti i veicoli presenti nel sistema.
# Ogni elemento può essere:
#     una stringa descrittiva,
#     ad esempio "SN-101 - Bulb - Nest (status: received)",
#     oppure
#     un dizionario con i campi principali (quelli restituiti da info()).
# La scelta è libera, ma deve essere coerente in tutto il programma.

@app.route('/devices', methods=['GET'])
def get_devices():
    return jsonify(iot_hub.list_all())

# GET /devices/<serial_number>
# Restituisce un JSON con i dettagli del dispositivo specificato.
# Se il veicolo non è presente nel sistema, restituire un JSON di errore (es. {"error": "device not found"}) con status code 404.

@app.route('/devices/<serial_number>', methods=['GET'])
def get_device(serial_number):
    device = iot_hub.get(serial_number)
    if device is None:
        return jsonify({'error':'non available'}), 404
    return jsonify(device.info()), 200


# GET /devices/<serial_number>/diagnostic/<factor>
# Restituisce un JSON con il tempo stimato per una diagnostica completa del dispositivo, utilizzando il metodo diagnostics_time(factor: float).
# Esempio di output:
# {
#   "id": "SN-101",
#   "device_type": "bulb"
#   "factor": 1.0,
#   "diagnostic_seconds": 45
# }
# Se il dispositivo non esiste, si ottiene un errore 404.
# Il parametro factor può essere letto dall'URL e convertito in float (con un default di 1.0 se vuoi renderlo opzionale).

@app.route('/devices/<serial_number>/diagnostic/<factor>', methods=['GET'])
def get_diagnostic(serial_number:str, factor:str):
    device = iot_hub.get(serial_number)
    if device is None:
        return jsonify({'error':'Device do non exists'}), 404
    try:
        f = float(factor)
    except ValueError:
        return jsonify({'error':'factor must be float'}), 400
    result = {
        'id':serial_number,
        'device_type':device.device_type(),
        'factor': f,
        'diagnostic_seconds': device.diagnostics_time(f)
    }
    return jsonify(result), 200

# Route POST

# POST /devices
# Permette di aggiungere un nuovo veicolo al sistema.
# Il body della richiesta deve essere JSON, letto con request.get_json().
# Deve contenere almeno:
#     type: "bulb" o "camera",
#     serial_number, brand, room, installation_year, status,
#     più i campi specifici del tipo (es. per camera: resolution, night_vision).
# Esempio di JSON per una telecamera intelligente:
# {
#   "type": "camera",
#   "id": "SN-3e67",
#   "brand": "Philips",
#   "room": "Living Room",
#   "installation_year": 2022,
#   "status": "online",
#   "resolution": 3
#   "night_vision": true
# }
# La funzione della route deve:
#     validare il JSON (campi obbligatori, tipo corretto),
#     creare l’istanza corretta (SmartBulb o SecurityCamera),
#     aggiungerla al centro con iot_hub.add(device),
#     restituire un JSON di conferma (es. con info()) e status code 201,
#     oppure un JSON di errore con status code 400 in caso di problemi (es. campi mancanti, tipo non riconosciuto).

def _control_create_device(data:dict) -> tuple[SmartDevice|None,str|None]:
    campi: list[str] = ['type','serial_number', 'brand', 'room','installation_year', 'status']
    for el in campi:
        if el not in data:
            return None, f'Missing: {el}'
    d_type: str = str(data['type']).strip().lower()
    if d_type not in ['bulb', 'camera']:
        return None, 'invalid type'
    if d_type == 'bulb':
        for el in ['brightness_lumens', 'color_capability']:
            if el not in data:
                return None, f'Missing: {el}'
        device: SmartBulb = SmartBulb(
            serial_number=str(data['serial_number']),
            brand=str(data['brand']),
            room=str(data['room']),
            installation_year=int(data['installation_year']),
            status=str(data['status']),
            brightness_lumens=int(data['brightness_lumens']),
            color_capability=bool(data['color_capability'])
        )
    elif d_type == 'camera':
        for el in ['resolution', 'night_vision']:
            if el not in data:
                return None, f'Missing: {el}'
        device: SecurityCamera = SecurityCamera(
            serial_number=str(data['serial_number']),
            brand=str(data['brand']),
            room=str(data['room']),
            installation_year=int(data['installation_year']),
            status=str(data['status']),
            resolution=str(data['resolution']),
            night_vision=bool(data['night_vision'])
        )
    return device, None

@app.route('/devices', methods=['POST'])
def post_device():
    data: dict = request.get_json()
    if not isinstance(data, dict):
        return jsonify({'error':'Invalid json type'}), 400
    device, error = _control_create_device(data)
    if error is not None:
        return jsonify({'error': error}), 400
    result = iot_hub.add(device)
    if not result:
        return jsonify({'error':'device already exists'}), 400
    return jsonify(device.info()), 201

# Route PUT

# PUT /devices/<serial_number>
# Sostituisce completamente le informazioni di un dispositivo esistente con quelle fornite nel body JSON (stesso formato del POST /devices).
# Comportamento tipico:
#     Se il veicolo esiste → viene rimpiazzato (aggiornato completamente).
#     Se non esiste → puoi scegliere se:
#         creare un nuovo veicolo con quell’plate id, oppure
#         restituire un errore 404.

@app.route('/devices/<serial_number>', methods=['PUT'])
def put_device(serial_number: str):
    device_old = iot_hub.get(serial_number)
    if device_old is None:
        return jsonify({'error':'device not exists'}), 404
    data: dict = request.get_json()
    if not isinstance(data, dict):
        return jsonify({'error':'invalid json type'}), 400
    data_new = dict(data)
    data_new['serial_number'] = serial_number
    device, errore = _control_create_device(data_new)
    if errore is not None:
        return jsonify({'error':errore}), 400
    iot_hub.update(serial_number, device)
    return jsonify(device.info()), 200

    

# Route PATCH

# PATCH /devices/<serial_number>/status
# Aggiorna solo lo stato (status) del dispositivo specificato.
# Body JSON di esempio:
# {
#   "status": "mantainance"
# }
# La funzione deve:
#     verificare che il dispositivo esista,
#     leggere il nuovo stato dal JSON,
#     chiamare iot_hub.patch_status(serial_number, new_status),
#     restituire il dispositivo aggiornato (via info()) o un messaggio di conferma.
# In caso di dispositivo inesistente → errore 404.



@app.route('/devices/<serial_number>/status', methods=['PATCH'])
def patch_status_device(serial_number):
    device = iot_hub.get(serial_number)
    if device is None:
        return jsonify({'error': 'device not exists'}), 404
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({'error':'invalid json type'}), 400
    if 'status' not in data:
        return jsonify({'error': 'Missing status'}),400
    status = str(data['status'])
    ALLOWED_STATUSES = {"online", "offline", "updating", "error"}
    if status not in ALLOWED_STATUSES:
        return jsonify({'error': 'invalid status'}), 400
    iot_hub.patch_status(serial_number,status)
    return jsonify(iot_hub.get(serial_number). info()) , 200
    

# Route DELETE

# DELETE /devices/<serial_number>
# Rimuove un dispositivo dal sistema.
# Comportamento:
#     Se il dispositivo esiste → viene eliminato e si restituisce un JSON di conferma (es. {"deleted": true, "serial_number": "SN-34567"}).
#     Se non esiste → restituire un JSON di errore con status code 404.

@app.route('/devices/<serial_number>', methods=['DELETE'])
def delete_device(serial_number):
    result = iot_hub.delete(serial_number)
    if not result:
        return jsonify({'error': 'device not exists'}), 404
    return jsonify({'deleted': True, 'serial_number': serial_number}), 200

if __name__=='__main__':
    app.run(debug=True)