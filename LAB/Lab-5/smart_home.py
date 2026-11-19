"""Smart home device controller demonstration."""

import json
from typing import Any


HUB_HOST = "127.0.0.1"
HUB_PORT = 8080
POWER_USAGE = {"light": 10, "fan": 60, "thermostat": 1500, "tv": 120}
devices: dict[str, dict[str, Any]] = {}


def add_device(
    device_name: str,
    kind: str,
    room: str = "Living Room",
    settings: dict[str, Any] | None = None,
) -> None:
    """Add a device to the smart-home registry."""
    devices[device_name] = {
        "kind": kind,
        "room": room,
        "on": False,
        "settings": {} if settings is None else settings,
    }


def toggle_device(device_name: str) -> bool:
    """Toggle a device and return its new state."""
    if device_name not in devices:
        print("Device not found:", device_name)
        return False
    devices[device_name]["on"] = not devices[device_name]["on"]
    return bool(devices[device_name]["on"])


def set_temperature(device_name: str, value: int) -> bool:
    """Set a thermostat temperature within the supported range."""
    if device_name not in devices:
        print("Device not found:", device_name)
        return False
    device = devices[device_name]
    if device["kind"] != "thermostat":
        print(device_name, "is not a thermostat")
        return False
    device["settings"]["temperature"] = min(max(value, 16), 30)
    return True


def devices_in_room(room: str) -> list[str]:
    """Return names of devices located in a room."""
    return [name for name, info in devices.items() if info["room"] == room]


def power_usage() -> int:
    """Calculate current power use in watts."""
    active = [info for info in devices.values() if info["on"]]
    return sum(POWER_USAGE.get(info["kind"], 0) for info in active)


def save_state(file_name: str = "home_state.json") -> None:
    """Persist the current device state as JSON."""
    with open(file_name, "w", encoding="utf-8") as state_file:
        json.dump(devices, state_file, indent=2)


def hub_address() -> str:
    """Return the local hub address used for app setup."""
    return f"{HUB_HOST}:{HUB_PORT}"


def main() -> None:
    """Run the smart-home demonstration."""
    add_device("Ceiling Light", "light")
    add_device("Bedroom Fan", "fan", "Bedroom")
    add_device("Thermostat", "thermostat", "Bedroom")
    add_device("Smart TV", "tv")

    toggle_device("Ceiling Light")
    toggle_device("Thermostat")
    toggle_device("Garage Door")
    set_temperature("Thermostat", 35)
    set_temperature("Ceiling Light", 20)

    print("Bedroom devices:", devices_in_room("Bedroom"))
    print("Current power use (W):", power_usage())
    print("Hub address:", hub_address())
    print("Light settings:", devices["Ceiling Light"]["settings"])
    devices_on = [name for name, info in devices.items() if info["on"]]
    print("Devices on:", devices_on)
    save_state()


if __name__ == "__main__":
    main()
