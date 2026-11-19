"""Branch-focused Highway Toll tests."""

import pytest

from highway_toll import pass_advice, toll_charge, toll_for


@pytest.mark.parametrize(
    ("axles", "peak", "fastag", "expected"),
    [
        (2, False, False, 100),
        (2, False, True, 90),
        (2, True, False, 125),
        (2, True, True, 112.5),
        (3, False, False, 150),
        (3, True, True, 178.12),
        (4, False, True, 237.5),
        (5, False, False, 400),
    ],
)
def test_all_toll_rate_branches(axles, peak, fastag, expected):
    assert toll_for(axles, peak, fastag) == expected


@pytest.mark.parametrize("axles", [0, 1, -1])
def test_invalid_axle_branch(axles):
    with pytest.raises(ValueError):
        toll_for(axles, False, False)


@pytest.mark.parametrize("vehicle", ["ambulance", "fire_engine"])
def test_exempt_vehicle_branches(vehicle):
    assert toll_charge(vehicle, 5, True, False) == 0


def test_regular_vehicle_branch():
    assert toll_charge("truck", 4, False, False) == 250


@pytest.mark.parametrize(
    ("trips", "pass_price", "expected"),
    [
        ([(False, False)], 100, "either"),
        ([(True, False)], 100, "buy_pass"),
        ([(False, False)], 150, "pay_per_trip"),
        ([], 0, "either"),
    ],
)
def test_pass_advice_all_decisions(trips, pass_price, expected):
    assert pass_advice(trips, 2, pass_price) == expected
