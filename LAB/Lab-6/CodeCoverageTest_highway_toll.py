"""Code-coverage test suite for the Highway Toll application."""

import pytest

from highway_toll import pass_advice, toll_charge, toll_for


def test_ambulance_is_exempt():
    assert toll_charge("ambulance", 2, False, False) == 0


def test_fire_engine_is_exempt():
    assert toll_charge("fire_engine", 4, True, True) == 0


@pytest.mark.parametrize(
    ("axles", "peak", "fastag", "expected"),
    [
        (2, False, False, 100),
        (3, False, False, 150),
        (4, True, False, 312.5),
        (5, False, False, 400),
        (2, True, True, 112.5),
        (5, True, True, 475.0),
    ],
)
def test_toll_for_rates(axles, peak, fastag, expected):
    assert toll_for(axles, peak, fastag) == expected


@pytest.mark.parametrize("axles", [0, 1, -2, 2.5, True, "2"])
def test_invalid_axle_counts(axles):
    with pytest.raises(ValueError, match="invalid axle count"):
        toll_for(axles, False, False)


def test_regular_vehicle_charges_toll():
    assert toll_charge("car", 2, False, False) == 100


@pytest.mark.parametrize(
    ("trips", "pass_price", "expected"),
    [
        ([(False, False), (True, True)], 212.5, "either"),
        ([(True, False)], 100, "buy_pass"),
        ([(False, False)], 150, "pay_per_trip"),
    ],
)
def test_pass_advice_decisions(trips, pass_price, expected):
    assert pass_advice(trips, 2, pass_price) == expected
