"""Defensive Highway Toll input parsing functions."""

import re


PLATE_PATTERN = re.compile(
    r"^(?P<state>[A-Za-z]{2})-(?P<district>\d{2})-"
    r"(?P<series>[A-Za-z]{1,3})-(?P<number>\d{4})$"
)


def parse_plate(plate):
    """Parse an Indian-style plate into normalized components."""
    if not isinstance(plate, str):
        raise ValueError("plate must be text")
    match = PLATE_PATTERN.fullmatch(plate.strip().upper())
    if match is None:
        raise ValueError("invalid plate format")
    return (
        match.group("state"),
        int(match.group("district")),
        match.group("series"),
        int(match.group("number")),
    )


def trip_cost(text):
    """Parse a `count x rate` expression and return the integer cost."""
    if not isinstance(text, str):
        raise ValueError("trip cost must be text")
    parts = text.lower().split("x")
    if len(parts) != 2:
        raise ValueError("trip cost must contain exactly one 'x'")
    count_text = parts[0].strip()
    rate_text = parts[1].strip()
    if not count_text or not rate_text:
        raise ValueError("trip count and rate are required")
    try:
        count = int(count_text)
        rate = int(rate_text)
    except ValueError as exc:
        raise ValueError("trip count and rate must be integers") from exc
    if count < 0 or rate < 0:
        raise ValueError("trip count and rate must not be negative")
    return count * rate


def axle_class(axles):
    """Return the vehicle class for a valid axle count."""
    if isinstance(axles, bool):
        raise ValueError("axle count must be an integer")
    try:
        count = int(axles)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError("axle count must be an integer") from exc
    if isinstance(axles, float) and not axles.is_integer():
        raise ValueError("axle count must be an integer")
    if count < 2:
        raise ValueError("axle count must be at least 2")
    if count == 2:
        return "car"
    if count <= 4:
        return "truck"
    return "heavy"


def main():
    """Run the interactive Highway Toll demonstration."""
    print("==== Running parse_plate ====")
    plate = input("Enter a plate (e.g. KA-05-AB-1234): ")
    try:
        print("State, District, Series and Number:", parse_plate(plate))
    except ValueError as exc:
        print("Invalid plate:", exc)

    print("\n==== Running trip_cost ====")
    text = input("Enter trips x rate (e.g. 3x150): ")
    try:
        print("Trip Cost:", trip_cost(text))
    except ValueError as exc:
        print("Invalid trip cost:", exc)

    print("\n==== Running axle_class ====")
    axles = input("Enter an axle count (e.g. 3): ")
    try:
        print("Vehicle Class:", axle_class(axles))
    except ValueError as exc:
        print("Invalid axle count:", exc)


if __name__ == "__main__":
    main()
