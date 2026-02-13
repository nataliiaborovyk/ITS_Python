from clinicBooking import Booking, MedicalVisit, DiagnosticExam, ClinicHub

clinic_hub = ClinicHub()

clinic_hub.add(
    MedicalVisit(
        booking_id="BK-101",
        patient_name="Mario Rossi",
        doctor="Dr. Bianchi",
        department="Cardiologia",
        date="2026-02-10",
        time="14:30",
        status="scheduled",
        visit_reason="Controllo annuale",
        first_time=False,
    )
)

clinic_hub.add(
    DiagnosticExam(
        booking_id="BK-202",
        patient_name="Giulia Verdi",
        doctor="Dr. Neri",
        department="Radiologia",
        date="2026-02-11",
        time="09:15",
        status="scheduled",
        exam_type="RMN",
        requires_fasting=True,
    )
)

from flask import Flask, jsonify, url_for, request

app = Flask(__name__)


# Route GET
# GET /

# Restituisce un JSON con:

#     una breve descrizione del servizio, ad esempio: "Clinic Booking Hub API";
#     link testuali che indicano le altre route disponibili, generati dinamicamente con url_for(), ad esempio:
#         /bookings
#         /bookings/BK-101
#         /bookings/BK-101/wait/1.0

# Il JSON potrebbe avere una struttura tipo:

# {
#   "message": "Clinic Booking Hub API",
#   "links": {
#     "bookings_list": "/bookings",
#     "booking_sample": "/bookings/BK-101",
#     "estimate_sample": "/bookings/BK-101/wait/1.0"
#   }
# }

@app.route('/', methods=['GET'])
def get():
    dict_info: dict = {
        'info':'Clinic Booking Hub API',
        'links': {
            'booking_list': url_for('get_bookings'),
            'booking_sample': url_for('get_boocking_id', booking_id='BK-101'),
            'estimate_sample': url_for('get_tempo_attesa', booking_id='BK-101',  factor=1.0)
        }
    }
    return jsonify(dict_info)

# GET /bookings

# Restituisce un JSON con l'elenco di tutte le prenotazioni presenti nel sistema.
# Ogni elemento può essere:
#     una stringa descrittiva, ad esempio: "BK-101 - visit - Mario Rossi (status: scheduled)"
#     oppure un dizionario con i campi principali (quelli restituiti da info()).
# La scelta è libera, ma deve essere coerente in tutto il programma.

@app.route('/bookings', methods=['GET'])
def get_bookings():
    return jsonify(clinic_hub.list_all()), 200


# GET /bookings/<booking_id>
# Restituisce un JSON con i dettagli della prenotazione specificata.
# Se la prenotazione non è presente nel sistema, restituire un JSON di errore (es. {"error": "booking not found"}) con status code 404.

@app.route('/bookings/<string:booking_id>', methods=['GET'])
def get_boocking_id(booking_id: str):
    booking = clinic_hub.get(booking_id)
    if booking is None:
        return jsonify({'error':'booking not found'}), 404
    return jsonify(booking.info()), 200

# GET /bookings/<booking_id>/wait/<factor>
# Restituisce un JSON con il tempo di attesa stimato prima dell’appuntamento, utilizzando estimated_wait(factor: float).
# Esempio di output:
# {
#   "booking_id": "BK-101",
#   "booking_type": "visit",
#   "factor": 1.0,
#   "estimated_wait_minutes": 55
# }
# Se la prenotazione non esiste, si ottiene un errore 404.
# Il parametro factor può essere letto dall’URL e convertito in float (con un default di 1.0 se vuoi renderlo opzionale).

@app.route('/bookings/<booking_id>/wait/<factor>',methods=['GET'])
def get_tempo_attesa(booking_id, factor):
    booking = clinic_hub.get(booking_id)
    if booking is None:
        return jsonify({'error':'booking not found'}), 404
    try:
        val = float(factor)
    except ValueError:
        return jsonify({'error':'factor deve essere float'})
    result = {'booking_id': booking_id,
              'booking_type': booking.booking_type(),
              'factor': val,
              'estimated_wait_minutes': booking.estimated_wait(val)}
    return jsonify(result), 200


# Route POST

# POST /bookings
# Permette di aggiungere una nuova prenotazione al sistema.
# Il body della richiesta deve essere JSON, letto con request.get_json().
# Deve contenere almeno:
#     type: "visit" o "exam"
#     booking_id, patient_name, doctor, department, date, time, status
#     più i campi specifici del tipo:
#         per visit: visit_reason, first_time
#         per exam: exam_type, requires_fasting
# Esempio di JSON per un esame diagnostico:
# {
#   "type": "exam",
#   "booking_id": "BK-3e67",
#   "patient_name": "Giulia Verdi",
#   "doctor": "Dr. Neri",
#   "department": "Radiologia",
#   "date": "2026-02-10",
#   "time": "09:15",
#   "status": "scheduled",
#   "exam_type": "RMN",
#   "requires_fasting": true
# }

# La funzione della route deve:
#     validare il JSON (campi obbligatori, tipo corretto),
#     creare l’istanza corretta (MedicalVisit o DiagnosticExam),
#     aggiungerla al centro con clinic_hub.add(booking),
#     restituire un JSON di conferma (es. con info()) e status code 201,

# oppure un JSON di errore con status code 400 in caso di problemi (es. campi mancanti, tipo non riconosciuto, formati errati).

from typing import Any


@app.route('/bookings', methods=['POST'])
def post_booking():
    data:dict = request.get_json()
    if not isinstance(data, dict):
        return jsonify({'error':'Invalid json body'})
    campi: list[str] = ['type', 'booking_id', 'patient_name', 'doctor', 'department', 'date', 'time', 'status']
    for el in campi:
        if el not in data:
            return jsonify({'error':f'Missing: {el}'}), 400
    body_type: str = str(data['type']).strip().lower()
    if body_type not in ['visit', 'exam']:
        return jsonify({'error':'Type anexists'}), 400
    if body_type == 'visit':
        for el in [ 'visit_reason', 'first_time']:
            if el not in data:
                return jsonify({'error':f'Missing: {el}'}), 400
        booking: MedicalVisit = MedicalVisit(
            booking_id=str(data['booking_id']),
            patient_name=str(data['patient_name']),
            doctor=str(data['doctor']),
            department=str(data['department']),
            date=str(data['date']),
            time=str(data['time']),
            status=str(data['status']),
            visit_reason=str(data['visit_reason']),
            first_time=bool(data['first_time'])
        )
    elif body_type == 'exam':
        for el in ['exam_type', 'requires_fasting']:
            if el not in data:
                return jsonify({'error':f'Missing: {el}'}), 400
        booking: DiagnosticExam = DiagnosticExam(
            booking_id=str(data['booking_id']),
            patient_name=str(data['patient_name']),
            doctor=str(data['doctor']),
            department=str(data['department']),
            date=str(data['date']),
            time=str(data['time']),
            status=str(data['status']),
            exam_type=str(data['exam_type']),
            requires_fasting=bool(data['requires_fasting'])
        )
    if not clinic_hub.add(booking):
        return jsonify({'error':'booking_id alredy exists'}), 400
    return jsonify(booking.info()), 201
            



# Route PUT
# PUT /bookings/<booking_id>
# Sostituisce completamente le informazioni di una prenotazione esistente con quelle fornite nel body JSON (stesso formato del POST /bookings).
# Comportamento tipico:
#     Se la prenotazione esiste → viene rimpiazzata (aggiornata completamente).
#     Se non esiste → puoi scegliere se:
#         creare una nuova prenotazione con quel booking_id, oppure
#         restituire un errore 404.

@app.route('/bookings/<booking_id>', methods=['PUT'])
def put_booking(booking_id):
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({'error': 'invalid json body'}), 400
    campi:list[str] = ['type', 'booking_id', 'patient_name', 'doctor', 'department', 'date', 'time', 'status']
    for el in campi:
        if el not in data:
            return jsonify({'error':f'Missing: {el}'}), 400
    body_type: str = str(data['type']).strip().lower()
    if body_type not in ['visit', 'exam']:
        return jsonify({'error':'Type is non valid'}), 400
    if body_type == 'visit':
        for el in ['visit_reason', 'first_time']:
            if el not in data:
                return jsonify({'error': f'Missing: {el}'}), 400
        booking: MedicalVisit = MedicalVisit(
            booking_id=booking_id,
            patient_name=str(data['patient_name']),
            doctor=str(data['doctor']),
            department=str(data['department']),
            date=str(data['date']),
            time=str(data['time']),
            status=str(data['status']),
            visit_reason=str(data['visit_reason']),
            first_time=bool(data['first_time'])
        )
    elif body_type == 'exam':
        for el in ['exam_type', 'requires_fasting']:
            if el not in data:
                return jsonify({'error': f'Missing: {el}'}), 400
        booking: DiagnosticExam = DiagnosticExam(
            booking_id=booking_id,
            patient_name=str(data['patient_name']),
            doctor=str(data['doctor']),
            department=str(data['department']),
            date=str(data['date']),
            time=str(data['time']),
            status=str(data['status']),
            exam_type=str(data['exam_type']),
            requires_fasting=bool(data['requires_fasting'])
        )
    booking_old = clinic_hub.get(booking_id)
    clinic_hub.update(booking_id, booking)
    if booking_old is None:
        return jsonify(booking.info()), 201
    return jsonify(booking.info()), 200


# Route PATCH
# PATCH /bookings/<booking_id>/status
# Aggiorna solo lo stato (status) della prenotazione specificata.
# Body JSON di esempio:
# {
#   "status": "checked_in"
# }
# La funzione deve:
#     verificare che la prenotazione esista,
#     leggere il nuovo stato dal JSON,
#     chiamare clinic_hub.patch_status(booking_id, new_status),
#     restituire la prenotazione aggiornata (via info()) o un messaggio di conferma.
# In caso di prenotazione inesistente → errore 404.

@app.route('/bookings/<booking_id>/status',  methods=['PATCH'])
def patch_booking_id(booking_id: str):
    booking = clinic_hub.get(booking_id)
    if booking is None:
        return jsonify({'error':'Booking non esiste'}), 404
    data: dict = request.get_json()
    if not isinstance(data, dict):
        return jsonify({'error':'invalid json type'}), 400
    if 'status' not in data:
        return jsonify({'error':'Missing status'}), 400
    new_status: str = str(data['status'])
    clinic_hub.patch_status(booking_id, new_status)
    return jsonify(clinic_hub.get(booking_id).info()), 200



# Route DELETE
# DELETE /bookings/<booking_id>
# Rimuove una prenotazione dal sistema.
# Comportamento:
#     Se la prenotazione esiste → viene eliminata e si restituisce un JSON di conferma (es. {"deleted": true, "booking_id": "BK-34567"}).
#     Se non esiste → restituire un JSON di errore con status code 404.

@app.route('/bookings/<booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    result: bool = clinic_hub.delete(booking_id)
    if not result:
        return jsonify({'error': 'booking not exists'}), 404
    return jsonify({'deleted': True, 'booking_id': booking_id}), 200






if __name__=='__main__':
    app.run(debug=True)

