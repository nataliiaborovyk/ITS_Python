from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from flask import Flask, jsonify, request, url_for


# -----------------------------
# Domain model
# -----------------------------

ALLOWED_STATUSES = {"online", "offline", "updating", "error"}


class SmartDevice(ABC):
    """
    Abstract base class for a generic IoT device.
    """

    def __init__(
        self,
        serial_number: str,
        brand: str,
        room: str,
        installation_year: int,
        status: str,
    ) -> None:
        self.serial_number = serial_number
        self.brand = brand
        self.room = room
        self.installation_year = installation_year
        self.status = status

    @abstractmethod
    def device_type(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def energy_consumption(self) -> float | int:
        raise NotImplementedError

    @abstractmethod
    def connection_quality(self) -> int:
        raise NotImplementedError

    def info(self) -> dict[str, float | int | str | bool]:
        return {
            "serial_number": self.serial_number,
            "brand": self.brand,
            "room": self.room,
            "installation_year": self.installation_year,
            "status": self.status,
            "device_type": self.device_type(),
        }

    def diagnostics_time(self, factor: float = 1.0) -> int:
        """
        Estimated seconds for a full diagnostics run.

        Formula:
          energy_consumption() * factor + connection_quality() * 10
        """
        seconds = float(self.energy_consumption()) * float(factor) + self.connection_quality() * 10
        return int(round(seconds))


class SmartBulb(SmartDevice):
    def __init__(
        self,
        serial_number: str,
        brand: str,
        room: str,
        installation_year: int,
        status: str,
        brightness_lumens: int,
        color_capability: bool,
    ) -> None:
        super().__init__(serial_number, brand, room, installation_year, status)
        self.brightness_lumens = brightness_lumens
        self.color_capability = color_capability

    def device_type(self) -> str:
        return "bulb"

    def energy_consumption(self) -> float | int:
        # typical low consumption
        return 9

    def connection_quality(self) -> int:
        # typical low/medium requirement
        return 3

    def info(self) -> dict[str, float | int | str | bool]:
        data = super().info()
        data.update(
            {
                "brightness_lumens": self.brightness_lumens,
                "color_capability": self.color_capability,
            }
        )
        return data


class SecurityCamera(SmartDevice):
    def __init__(
        self,
        serial_number: str,
        brand: str,
        room: str,
        installation_year: int,
        status: str,
        resolution: str,
        night_vision: bool,
    ) -> None:
        super().__init__(serial_number, brand, room, installation_year, status)
        self.resolution = resolution
        self.night_vision = night_vision

    def device_type(self) -> str:
        return "camera"

    def energy_consumption(self) -> float | int:
        # typical higher consumption for cameras
        return 50

    def connection_quality(self) -> int:
        # high requirement for video streaming
        return 9

    def info(self) -> dict[str, float | int | str | bool]:
        data = super().info()
        data.update({"resolution": self.resolution, "night_vision": self.night_vision})
        return data


class IoTHub:
    def __init__(self) -> None:
        self.devices: dict[str, SmartDevice] = {}

    def add(self, device: SmartDevice) -> bool:
        if device.serial_number in self.devices:
            return False
        self.devices[device.serial_number] = device
        return True

    def get(self, serial_number: str) -> SmartDevice | None:
        return self.devices.get(serial_number)

    def update(self, serial_number: str, new_device: SmartDevice) -> None:
        self.devices[serial_number] = new_device

    def patch_status(self, serial_number: str, new_status: str) -> None:
        d = self.devices.get(serial_number)
        if d is None:
            return
        d.status = new_status

    def delete(self, serial_number: str) -> bool:
        if serial_number not in self.devices:
            return False
        del self.devices[serial_number]
        return True

    def list_all(self) -> list[dict[str, float | int | str | bool]]:
        return [d.info() for d in self.devices.values()]


# -----------------------------
# Helpers (validation/parsing)
# -----------------------------

def _get_first_present(d: dict[str, Any], *keys: str) -> Any:
    for k in keys:
        if k in d:
            return d[k]
    return None


def _validate_common_fields(payload: dict[str, Any]) -> str | None:
    required = ["serial_number", "brand", "room", "installation_year", "status"]
    missing = [k for k in required if k not in payload]
    if missing:
        return f"Missing required fields: {', '.join(missing)}"

    if not isinstance(payload["serial_number"], str) or not payload["serial_number"].strip():
        return "serial_number must be a non-empty string"
    if not isinstance(payload["brand"], str) or not payload["brand"].strip():
        return "brand must be a non-empty string"
    if not isinstance(payload["room"], str) or not payload["room"].strip():
        return "room must be a non-empty string"

    try:
        payload["installation_year"] = int(payload["installation_year"])
    except Exception:
        return "installation_year must be an integer"

    if not isinstance(payload["status"], str) or payload["status"] not in ALLOWED_STATUSES:
        return f"status must be one of: {sorted(ALLOWED_STATUSES)}"

    return None


def device_from_json(data: dict[str, Any]) -> SmartDevice:
    """
    Create a SmartDevice instance (SmartBulb or SecurityCamera) from JSON dict.
    Accepts a few alias keys to be tolerant with minor differences (id -> serial_number).
    """
    dtype = _get_first_present(data, "type", "device_type")
    if not isinstance(dtype, str):
        raise ValueError("Missing or invalid 'type' (must be 'bulb' or 'camera')")

    # Normalize common keys (accept id -> serial_number)
    if "serial_number" not in data and "id" in data:
        data["serial_number"] = data["id"]

    err = _validate_common_fields(data)
    if err:
        raise ValueError(err)

    serial_number = str(data["serial_number"]).strip()
    brand = str(data["brand"]).strip()
    room = str(data["room"]).strip()
    installation_year = int(data["installation_year"])
    status = str(data["status"])

    if dtype == "bulb":
        if "brightness_lumens" not in data or "color_capability" not in data:
            raise ValueError("SmartBulb requires fields: brightness_lumens, color_capability")
        try:
            brightness_lumens = int(data["brightness_lumens"])
        except Exception:
            raise ValueError("brightness_lumens must be an integer")
        if not isinstance(data["color_capability"], bool):
            raise ValueError("color_capability must be a boolean")
        return SmartBulb(
            serial_number=serial_number,
            brand=brand,
            room=room,
            installation_year=installation_year,
            status=status,
            brightness_lumens=brightness_lumens,
            color_capability=bool(data["color_capability"]),
        )

    if dtype == "camera":
        if "resolution" not in data or "night_vision" not in data:
            raise ValueError("SecurityCamera requires fields: resolution, night_vision")
        if not isinstance(data["resolution"], str) or not data["resolution"].strip():
            raise ValueError("resolution must be a non-empty string")
        if not isinstance(data["night_vision"], bool):
            raise ValueError("night_vision must be a boolean")
        return SecurityCamera(
            serial_number=serial_number,
            brand=brand,
            room=room,
            installation_year=installation_year,
            status=status,
            resolution=str(data["resolution"]).strip(),
            night_vision=bool(data["night_vision"]),
        )

    raise ValueError("Unknown type. Use 'bulb' or 'camera'.")


# -----------------------------
# Flask app
# -----------------------------

app = Flask(__name__)
iot_hub = IoTHub()

# Sample data (at least one bulb and one camera)
iot_hub.add(
    SmartBulb(
        serial_number="SN-101",
        brand="Nest",
        room="Living Room",
        installation_year=2021,
        status="online",
        brightness_lumens=800,
        color_capability=True,
    )
)
iot_hub.add(
    SecurityCamera(
        serial_number="SN-202",
        brand="Ring",
        room="Entrance",
        installation_year=2020,
        status="offline",
        resolution="1080p",
        night_vision=True,
    )
)


@app.get("/")
def root():
    return jsonify(
        {
            "message": "Smart Home Hub API",
            "links": {
                "devices_list": url_for("list_devices", _external=False),
                "device_sample": url_for("get_device", serial_number="SN-101", _external=False),
                "estimate_sample": url_for("get_diagnostic_time", serial_number="SN-101", factor=1.0, _external=False),
            },
        }
    )


@app.get("/devices")
def list_devices():
    # Coherent choice: return list of dicts (info())
    return jsonify(iot_hub.list_all())


@app.get("/devices/<serial_number>")
def get_device(serial_number: str):
    d = iot_hub.get(serial_number)
    if d is None:
        return jsonify({"error": "device not found"}), 404
    return jsonify(d.info())


@app.get("/devices/<serial_number>/diagnostic/<factor>")
def get_diagnostic_time(serial_number: str, factor: str):
    d = iot_hub.get(serial_number)
    if d is None:
        return jsonify({"error": "device not found"}), 404

    try:
        f = float(factor)
    except Exception:
        return jsonify({"error": "Invalid factor"}), 400

    return jsonify(
        {
            "serial_number": d.serial_number,
            "device_type": d.device_type(),
            "factor": f,
            "diagnostic_seconds": d.diagnostics_time(f),
        }
    )


@app.post("/devices")
def create_device():
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be JSON object"}), 400

    try:
        d = device_from_json(data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    ok = iot_hub.add(d)
    if not ok:
        return jsonify({"error": "Device already exists"}), 400

    return jsonify(d.info()), 201


@app.put("/devices/<serial_number>")
def put_device(serial_number: str):
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be JSON object"}), 400

    # Enforce the path serial_number
    data = dict(data)
    data["serial_number"] = serial_number

    try:
        d = device_from_json(data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    # Choose behavior: create if missing (UPSERT)
    iot_hub.update(serial_number, d)
    return jsonify(d.info())


@app.patch("/devices/<serial_number>/status")
def patch_device_status(serial_number: str):
    d = iot_hub.get(serial_number)
    if d is None:
        return jsonify({"error": "device not found"}), 404

    data = request.get_json()
    if not isinstance(data, dict) or "status" not in data:
        return jsonify({"error": "Body must be JSON with 'status' field"}), 400

    new_status = data["status"]
    if not isinstance(new_status, str) or new_status not in ALLOWED_STATUSES:
        return jsonify({"error": f"status must be one of: {sorted(ALLOWED_STATUSES)}"}), 400

    iot_hub.patch_status(serial_number, new_status)
    return jsonify(iot_hub.get(serial_number).info())


@app.delete("/devices/<serial_number>")
def delete_device(serial_number: str):
    ok = iot_hub.delete(serial_number)
    if not ok:
        return jsonify({"error": "device not found"}), 404
    return jsonify({"deleted": True, "serial_number": serial_number})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
