from main import Device, Smartphone, Laptop, ServiceCenter, sc1, tel1, pc1

from flask import Flask, jsonify, url_for, request

app = Flask(__name__)


@app.route('/')
def get():
    info: dict = {
        'message': "Welcome to Service Center API",
        "list_devices": url_for('get_devises'),
        "sample_device_id:t1": url_for('get_device_id', device_id='t1'),
        "sample_device_id:l1": url_for('get_device_id', device_id='l1'),
        "sample_estimate_id:t1": url_for('tempo_stimato', device_id = "t1", factor = 1.5),
        "sample_estimate_id:l1": url_for('tempo_stimato', device_id = "l1", factor = 1.5),
    
    }
    return jsonify(info), 200

@app.route('/devices', methods=['GET'])
def  get_devises():
    return jsonify(sc1.list_all()), 200


@app.route('/devices/<int:device_id>', methods=['GET'])
def get_device_id(device_id):
    if sc1.get(device_id) == None:
        return jsonify({'errore': f'non abbiamo dispositivo con id: {device_id}'}), 404
    return jsonify(sc1.get(device_id).info()), 200


@app.route('/devices/<int:device_id>/estimate/<float:factor>', methods=['GET'])
def tempo_stimato(device_id, factor):
    if sc1.get(device_id) == None:
       return jsonify({'errore': f'non abbiamo dispositivo con id: {device_id}'}), 404
    device: Smartphone|Laptop = sc1.get(device_id)
    factor:float = float(factor)
    dict_info: dict = {
        "id": device.get_id(),
        "device_type": device.devise_type(),
        "factor": factor,
        "estimated_total_minutes": device.estimated_total_time(factor)
    }
    return jsonify(dict_info)


@app.route('/devices', methods=['POST'])
def post_device():
    data: dict = request.get_json()
    
    # Controlli
    if "device_type" not in data:
        return jsonify({"errore" : "manca il campo 'device_type' "}), 400
    if "model" not in data:
        return jsonify({"errore" : "manca il campo 'model' "}), 400
    if "customer_name" not in data:
        return jsonify({"errore" : "manca il campo 'customer_name' "}), 400
    if "purchase_year" not in data:
        return jsonify({"errore" : "manca il campo 'purchase_year' "}), 400
    if not isinstance(data["device_type"], str):
        return jsonify({"errore": "il tipo di dato deve essere 'str'"}), 400
    if not isinstance(data["model"], str):
        return jsonify({"errore": "il tipo di dato deve essere 'str'"}), 400
    if not isinstance(data["customer_name"], str):
        return jsonify({"errore": "il tipo di dato deve essere 'str'"}), 400
    if not isinstance(data["purchase_year"], int):
        return jsonify({"errore": "il tipo di dato deve essere 'int'"}), 400
    
    if data['device_type'] is None:
        return jsonify({'errore': 'devi indicare il tipo del dispositivo'}), 400
    if data['device_type'] == 'smartphone':
        if "has_protective_case" not in data:
            return jsonify({"errore" : "manca il campo 'has_protective_case' "}), 400
        if "storage_gb" not in data:
            return jsonify({"errore" : "manca il campo 'storage_gb' "}), 400
        if not isinstance(data["has_protective_case"], bool):
            return jsonify({"errore": "il tipo di dato deve essere 'bool'"}), 400
        if not isinstance(data["storage_gb"], int):
            return jsonify({"errore": "il tipo di dato deve essere 'int'"}), 400
        new_device: Smartphone = Smartphone(model=data["model"],
                                            customer_name=data["customer_name"],
                                            purchase_year=data["purchase_year"],
                                            has_protective_case=data["has_protective_case"],
                                            storage_gb=data["storage_gb"])
    if data['device_type'] == 'laptop':
        if "has_dedicated_gpu" not in data:
            return jsonify({"errore" : "manca il campo 'has_dedicated_gpu' "}), 400
        if "screen_size_inches" not in data:
            return jsonify({"errore" : "manca il campo 'screen_size_inches' "}), 400
        if not isinstance(data["has_dedicated_gpu"], bool):
            return jsonify({"errore": "il tipo di dato deve essere 'bool'"}), 400
        if not isinstance(data["screen_size_inches"], float):
            return jsonify({"errore": "il tipo di dato deve essere 'float'"}), 400
        new_device: Laptop = Laptop(model=data["model"],
                                    customer_name=data["customer_name"],
                                    purchase_year=data["purchase_year"],
                                    has_dedicated_gpu=data["has_dedicated_gpu"],
                                    screen_size_inches=data["screen_size_inches"])
        
    sc1.add(new_device)
    return jsonify(new_device.info()), 201


    
@app.route('/devices/<int:device_id>', methods=['PUT'])
def put_device(device_id):
    data: dict = request.get_json()
    device = sc1.get(device_id)
    if device is None:
        return jsonify({'errore': f'non abbiamo dispositivo con id: {device_id}'}), 404
    # Controlli
    if "device_type" not in data:
        return jsonify({"errore" : "manca il campo 'device_type' "}), 400
    if "model" not in data:
        return jsonify({"errore" : "manca il campo 'model' "}), 400
    if "customer_name" not in data:
        return jsonify({"errore" : "manca il campo 'customer_name' "}), 400
    if "purchase_year" not in data:
        return jsonify({"errore" : "manca il campo 'purchase_year' "}), 400
    if not isinstance(data["device_type"], str):
        return jsonify({"errore": "il tipo di dato deve essere 'str'"}), 400
    if not isinstance(data["model"], str):
        return jsonify({"errore": "il tipo di dato deve essere 'str'"}), 400
    if not isinstance(data["customer_name"], str):
        return jsonify({"errore": "il tipo di dato deve essere 'str'"}), 400
    if not isinstance(data["purchase_year"], int):
        return jsonify({"errore": "il tipo di dato deve essere 'int'"}), 400
    
    if data['device_type'] is None:
        return jsonify({'errore': 'devi indicare il tipo del dispositivo'}), 400
    device.model = data["model"]
    device.customer_name = data["customer_name"]
    device.purchase_year = data["purchase_year"]
    device.status = data["status"]
    
    if data['device_type'] == 'smartphone':
        if "has_protective_case" not in data:
            return jsonify({"errore" : "manca il campo 'has_protective_case' "}), 400
        if "storage_gb" not in data:
            return jsonify({"errore" : "manca il campo 'storage_gb' "}), 400
        if not isinstance(data["has_protective_case"], bool):
            return jsonify({"errore": "il tipo di dato deve essere 'bool'"}), 400
        if not isinstance(data["storage_gb"], int):
            return jsonify({"errore": "il tipo di dato deve essere 'int'"}), 400
        device.has_protective_case = data["has_protective_case"]
        device.storage_gb = data["storage_gb"]
    if data['device_type'] == 'laptop':
        if "has_dedicated_gpu" not in data:
            return jsonify({"errore" : "manca il campo 'has_dedicated_gpu' "}), 400
        if "screen_size_inches" not in data:
            return jsonify({"errore" : "manca il campo 'screen_size_inches' "}), 400
        if not isinstance(data["has_dedicated_gpu"], bool):
            return jsonify({"errore": "il tipo di dato deve essere 'bool'"}), 400
        if not isinstance(data["screen_size_inches"], float):
            return jsonify({"errore": "il tipo di dato deve essere 'float'"}), 400
        device.has_dedicated_gpu = data["has_dedicated_gpu"]
        device.screen_size_inches = data["screen_size_inches"]
    sc1.update(device_id, device)
    return jsonify(device.info()), 201



@app.route('/devices/<int:device_id>/status', methods=['PATCH'])
def patch_status(device_id):
    data:dict = request.get_json()
    if sc1.get(device_id) is None:
        return jsonify({'errore': f'non abbiamo dispositivo con id: {device_id}'}), 404
    if "status" not in data:
        return jsonify({"errore" : "manca il campo 'status' "}), 400
    if not isinstance(data["status"], str):
        return jsonify({"errore": "il tipo di dato deve essere 'str'"}), 400
    sc1.patch_status(device_id, data["status"])
    device: Smartphone|Laptop = sc1.get(device_id)
    return jsonify(device.info()), 201



@app.route('/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    data:dict = request.get_json()
    if sc1.get(device_id) is None:
        return jsonify({'errore': f'non abbiamo dispositivo con id: {device_id}'}), 404
    device: Smartphone|Laptop = sc1.get(device_id)
    sc1.delete(device_id)
    return jsonify({"deleted": True, "id": device_id})

    
    
    
if __name__ == '__main__':
    app.run(debug=True)