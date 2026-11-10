import json

class Inventory:
    def __init__(self):
        self.devices = []

    def add_device(self, device_id, name, serial_number):
        # ВАЖНО: Эта проверка будет использоваться в "отрицательном эксперименте"
        for dev in self.devices:
            if dev['serial_number'] == serial_number:
                raise ValueError("Serial number must be unique")
        
        self.devices.append({
            "id": device_id,
            "name": name,
            "serial_number": serial_number
        })

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.devices, f, ensure_ascii=False, indent=2)
