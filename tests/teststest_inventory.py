import unittest
import os
from inventory import Inventory

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory()

    def test_add_device_success(self):
        self.inv.add_device(1, "Laptop", "SN123")
        self.assertEqual(len(self.inv.devices), 1)

    def test_add_multiple_devices(self):
        self.inv.add_device(1, "PC", "SN1")
        self.inv.add_device(2, "Printer", "SN2")
        self.assertEqual(len(self.inv.devices), 2)

    def test_device_fields(self):
        self.inv.add_device(1, "Router", "SN999")
        self.assertEqual(self.inv.devices[0]['name'], "Router")

    def test_serial_number_is_unique(self):
        # ЭТОТ ТЕСТ МЫ СЛОМАЕМ В ЗАДАНИИ 2
        self.inv.add_device(1, "Laptop", "SN123")
        with self.assertRaises(ValueError):
            self.inv.add_device(2, "Laptop 2", "SN123")

    def test_different_serials_allowed(self):
        self.inv.add_device(1, "Laptop", "SN123")
        self.inv.add_device(2, "Laptop", "SN456")
        self.assertEqual(len(self.inv.devices), 2)

    def test_save_to_file(self):
        self.inv.add_device(1, "PC", "SN777")
        self.inv.save_to_file("test_temp.json")
        self.assertTrue(os.path.exists("test_temp.json"))
        os.remove("test_temp.json")

    def test_empty_inventory(self):
        self.assertEqual(len(self.inv.devices), 0)

    def test_id_is_saved(self):
        self.inv.add_device(42, "Device", "SN42")
        self.assertEqual(self.inv.devices[0]['id'], 42)

    def test_serial_saved(self):
        self.inv.add_device(1, "Device", "SN-XYZ")
        self.assertEqual(self.inv.devices[0]['serial_number'], "SN-XYZ")

    def test_multiple_saves(self):
        self.inv.add_device(1, "A", "SN1")
        self.inv.add_device(2, "B", "SN2")
        self.inv.save_to_file("test_temp.json")
        self.assertTrue(os.path.exists("test_temp.json"))
        os.remove("test_temp.json")

if __name__ == '__main__':
    unittest.main()