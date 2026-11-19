"""Regression tests for the smart-home controller."""

import unittest

import smart_home


class SmartHomeTests(unittest.TestCase):
    """Verify state changes and the original mutable-default regression."""

    def setUp(self):
        smart_home.devices.clear()

    def test_add_device_settings_are_independent(self):
        smart_home.add_device("Thermostat", "thermostat", "Bedroom")
        smart_home.add_device("Ceiling Light", "light")

        self.assertTrue(
            smart_home.set_temperature("Thermostat", 35)
        )
        self.assertEqual(
            smart_home.devices["Ceiling Light"]["settings"],
            {},
        )

    def test_temperature_is_clamped(self):
        smart_home.add_device("Thermostat", "thermostat", "Bedroom")

        self.assertTrue(smart_home.set_temperature("Thermostat", 35))
        self.assertEqual(
            smart_home.devices["Thermostat"]["settings"]["temperature"],
            30,
        )

    def test_unknown_devices_are_safe(self):
        self.assertFalse(smart_home.toggle_device("Missing"))
        self.assertFalse(smart_home.set_temperature("Missing", 20))

    def test_power_usage_only_counts_active_devices(self):
        smart_home.add_device("Ceiling Light", "light")
        smart_home.add_device("Thermostat", "thermostat")

        smart_home.toggle_device("Ceiling Light")

        self.assertEqual(smart_home.power_usage(), 10)


if __name__ == "__main__":
    unittest.main()
