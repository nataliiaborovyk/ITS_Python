from abc import ABC, abstractmethod
from flask import Flask, jsonify, request, url_for

# ==========================
# Classi di dominio
# ==========================

class Device(ABC):
    """
    Classe astratta che rappresenta un dispositivo generico
    preso in carico dal centro di assistenza.
    """

    def __init__(
        self,
        device_id: str,
        model: str,
        customer_name: str,
        purchase_year: int,
        status: str,
    ):
        self.id = device_id
        self.model = model
        self.customer_name = customer_name
        self.purchase_year = purchase_year
        self.status = status

    @abstractmethod
    def device_type(self) -> str:
        """Tipo di dispositivo (es. smartphone, laptop)."""
        pass

    @abstractmethod
    def base_diagnosis_time(self) -> int:
        """Tempo base di diagnosi in minuti."""
        pass

    @abstractmethod
    def repair_complexity(self) -> int:
        """Indice di complessità della riparazione."""
        pass

    def info(self) -> dict:
        """Restituisce un dizionario con le informazioni principali del device."""
        return {
            "id": self.id,
            "device_type": self.device_type(),
            "model": self.model,
            "customer_name": self.customer_name,
            "purchase_year": self.purchase_year,
            "status": self.status,
        }

    def estimated_total_time(self, factor: float = 1.0) -> int:
        """
        Tempo totale stimato in minuti, in base al tempo base di diagnosi,
        alla complessità di riparazione e a un fattore di carico.
        Formula totalmente inventata, ma coerente.
        """
        base = self.base_diagnosis_time()
        complexity = self.repair_complexity()
        estimate = base * factor + complexity * 30
        # Restituiamo un intero (arrotondando per eccesso)
        return int(round(estimate))


class Smartphone(Device):
    """
    Sottoclasse che rappresenta uno smartphone.
    """

    def __init__(
        self,
        device_id: str,
        model: str,
        customer_name: str,
        purchase_year: int,
        status: str,
        has_protective_case: bool,
        storage_gb: int,
    ):
        super().__init__(device_id, model, customer_name, purchase_year, status)
        self.has_protective_case = has_protective_case
        self.storage_gb = storage_gb

    def device_type(self) -> str:
        return "smartphone"

    def base_diagnosis_time(self) -> int:
        # Ad esempio, diagnosi più veloce
        return 20

    def repair_complexity(self) -> int:
        # Complessità media
        return 2

    def info(self) -> dict:
        base = super().info()
        base["has_protective_case"] = self.has_protective_case
        base["storage_gb"] = self.storage_gb
        return base


class Laptop(Device):
    """
    Sottoclasse che rappresenta un laptop.
    """

    def __init__(
        self,
        device_id: str,
        model: str,
        customer_name: str,
        purchase_year: int,
        status: str,
        has_dedicated_gpu: bool,
        screen_size_inches: float,
    ):
        super().__init__(device_id, model, customer_name, purchase_year, status)
        self.has_dedicated_gpu = has_dedicated_gpu
        self.screen_size_inches = screen_size_inches

    def device_type(self) -> str:
        return "laptop"

    def base_diagnosis_time(self) -> int:
        # Diagnosi più lunga rispetto allo smartphone
        return 40

    def repair_complexity(self) -> int:
        # Complessità un po' più alta
        return 3

    def info(self) -> dict:
        base = super().info()
        base["has_dedicated_gpu"] = self.has_dedicated_gpu
        base["screen_size_inches"] = self.screen_size_inches
        return base


class ServiceCenter:
    """
    Contenitore principale: gestisce i dispositivi presi in carico.
    """

    def __init__(self):
        self.devices = {}  # id -> Device

    def add(self, device: Device) -> bool:
        """Aggiunge un device. Ritorna False se l'id esiste già."""
        if device.id in self.devices:
            return False
        self.devices[device.id] = device
        return True

    def get(self, device_id: str):
        return self.devices.get(device_id)

    def list_all(self):
        return list(self.devices.values())

    def update(self, device_id: str, new_device: Device) -> None:
        """
        Sostituisce (o crea) il device con id device_id.
        Qui adottiamo comportamento tipo 'upsert':
        se non esiste, lo crea.
        """
        self.devices[device_id] = new_device

    def patch_status(self, device_id: str, new_status: str) -> bool:
        """Aggiorna solo lo status del device. Ritorna False se non esiste."""
        device = self.get(device_id)
        if device is None:
            return False
        device.status = new_status
        return True

    def delete(self, device_id: str) -> bool:
        """Elimina un device. Ritorna False se non esiste."""
        if device_id in self.devices:
            del self.devices[device_id]
            return True
        return False


# ==========================
# Setup iniziale
# ==========================

service_center = ServiceCenter()

# Dispositivi di esempio
d1 = Smartphone(
    device_id="d1",
    model="iPhone 13",
    customer_name="Alice",
    purchase_year=2021,
    status="received",
    has_protective_case=True,
    storage_gb=128,
)

d2 = Laptop(
    device_id="d2",
    model="ThinkPad X1",
    customer_name="Bob",
    purchase_year=2019,
    status="diagnosing",
    has_dedicated_gpu=False,
    screen_size_inches=14.0,
)

service_center.add(d1)
service_center.add(d2)

# ==========================
# Applicazione Flask
# ==========================

app = Flask(__name__)


def create_device_from_data(data: dict, device_id: str = None) -> Device:
    """
    Crea un oggetto Device (Smartphone o Laptop) a partire da un dizionario JSON.
    Se device_id è fornito, viene usato al posto di data["id"] (per PUT).
    """
    device_type = data.get("type")
    if device_type not in ("smartphone", "laptop"):
        raise ValueError("Unknown or missing 'type' field (expected 'smartphone' or 'laptop').")

    # Campi comuni
    if device_id is None:
        device_id = data.get("id")
    model = data.get("model")
    customer_name = data.get("customer_name")
    purchase_year = data.get("purchase_year")
    status = data.get("status")

    if not all([device_id, model, customer_name, purchase_year, status]):
        raise ValueError("Missing required common fields.")

    try:
        purchase_year = int(purchase_year)
    except ValueError:
        raise ValueError("purchase_year must be an integer.")

    if device_type == "smartphone":
        has_protective_case = data.get("has_protective_case")
        storage_gb = data.get("storage_gb")
        if has_protective_case is None or storage_gb is None:
            raise ValueError("Missing smartphone fields: has_protective_case, storage_gb.")
        try:
            storage_gb = int(storage_gb)
        except ValueError:
            raise ValueError("storage_gb must be an integer.")
        return Smartphone(
            device_id=device_id,
            model=model,
            customer_name=customer_name,
            purchase_year=purchase_year,
            status=status,
            has_protective_case=bool(has_protective_case),
            storage_gb=storage_gb,
        )

    else:  # laptop
        has_dedicated_gpu = data.get("has_dedicated_gpu")
        screen_size_inches = data.get("screen_size_inches")
        if has_dedicated_gpu is None or screen_size_inches is None:
            raise ValueError("Missing laptop fields: has_dedicated_gpu, screen_size_inches.")
        try:
            screen_size_inches = float(screen_size_inches)
        except ValueError:
            raise ValueError("screen_size_inches must be a float.")
        return Laptop(
            device_id=device_id,
            model=model,
            customer_name=customer_name,
            purchase_year=purchase_year,
            status=status,
            has_dedicated_gpu=bool(has_dedicated_gpu),
            screen_size_inches=screen_size_inches,
        )


@app.route("/", methods=["GET"])
def index():
    """
    Route principale: restituisce un messaggio di benvenuto e alcuni link
    alle principale route dell'API.
    """
    sample_id = "d1"
    return jsonify(
        {
            "message": "Welcome to Service Center API",
            "links": {
                "list_devices": url_for("list_devices"),
                "sample_device": url_for("get_device", device_id=sample_id),
                "sample_estimate": url_for("get_estimate", device_id=sample_id, factor=1.5),
                "create_device": url_for("create_device"),
                "update_device_put": url_for("update_device", device_id=sample_id),
                "patch_status": url_for("patch_device_status", device_id=sample_id),
                "delete_device": url_for("delete_device", device_id=sample_id),
            },
        }
    )


@app.route("/devices", methods=["GET"])
def list_devices():
    """
    Restituisce la lista di tutti i dispositivi sotto forma di lista di dizionari.
    """
    devices_info = [device.info() for device in service_center.list_all()]
    return jsonify(devices_info)


@app.route("/devices/<device_id>", methods=["GET"])
def get_device(device_id):
    """
    Restituisce i dettagli del dispositivo specificato.
    """
    device = service_center.get(device_id)
    if device is None:
        return jsonify({"error": "Device not found"}), 404
    return jsonify(device.info())


@app.route("/devices/<device_id>/estimate/<factor>", methods=["GET"])
def get_estimate(device_id, factor):
    """
    Restituisce il tempo stimato totale per la lavorazione del dispositivo.
    """
    device = service_center.get(device_id)
    if device is None:
        return jsonify({"error": "Device not found"}), 404

    try:
        factor_float = float(factor)
    except ValueError:
        return jsonify({"error": "Factor must be a float."}), 400

    estimate = device.estimated_total_time(factor_float)
    return jsonify(
        {
            "id": device.id,
            "device_type": device.device_type(),
            "factor": factor_float,
            "estimated_total_minutes": estimate,
        }
    )


@app.route("/devices", methods=["POST"])
def create_device():
    """
    Crea un nuovo dispositivo (POST /devices).
    Richiede un body JSON con:
    - type: "smartphone" o "laptop"
    - id, model, customer_name, purchase_year, status
    - più i campi specifici del tipo.
    """
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Missing or invalid JSON body."}), 400

    try:
        device = create_device_from_data(data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    if service_center.get(device.id) is not None:
        return jsonify({"error": "Device with this id already exists."}), 400

    service_center.add(device)
    return jsonify(device.info()), 201


@app.route("/devices/<device_id>", methods=["PUT"])
def update_device(device_id):
    """
    Sostituisce (o crea) completamente un dispositivo con id device_id.
    Richiede un JSON simile a POST, con campo "type".
    Qui adottiamo un comportamento 'upsert':
    - se il device esiste, viene sovrascritto;
    - se non esiste, viene creato.
    """
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Missing or invalid JSON body."}), 400

    try:
        device = create_device_from_data(data, device_id=device_id)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    service_center.update(device_id, device)
    return jsonify(device.info()), 200


@app.route("/devices/<device_id>/status", methods=["PATCH"])
def patch_device_status(device_id):
    """
    Aggiorna solo lo stato (status) del dispositivo (PATCH).
    Body JSON atteso: { "status": "nuovo_status" }
    """
    device = service_center.get(device_id)
    if device is None:
        return jsonify({"error": "Device not found"}), 404

    data = request.get_json()
    if data is None:
        return jsonify({"error": "Missing or invalid JSON body."}), 400

    new_status = data.get("status")
    if not new_status:
        return jsonify({"error": "Missing 'status' field."}), 400

    service_center.patch_status(device_id, new_status)
    return jsonify(device.info()), 200


@app.route("/devices/<device_id>", methods=["DELETE"])
def delete_device(device_id):
    """
    Elimina il dispositivo con id device_id.
    """
    deleted = service_center.delete(device_id)
    if not deleted:
        return jsonify({"error": "Device not found"}), 404

    return jsonify({"deleted": True, "id": device_id}), 200


if __name__ == "__main__":
    # Avvia il server in debug sulla porta 5000
    app.run(debug=True, host="127.0.0.1", port=5000)
