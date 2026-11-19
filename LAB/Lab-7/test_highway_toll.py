"""Property-based tests for Highway Toll input validation."""

import math

import pytest
from hypothesis import given, strategies as st

from highway_toll import axle_class, main, parse_plate, trip_cost


@given(st.text(max_size=100))
def test_parse_plate_fuzz_never_leaks_parser_errors(value):
    try:
        state, district, series, number = parse_plate(value)
    except ValueError:
        return
    assert len(state) == 2
    assert 0 <= district <= 99
    assert series
    assert 0 <= number <= 9999


@given(st.text(max_size=100))
def test_trip_cost_fuzz_never_leaks_parser_errors(value):
    try:
        result = trip_cost(value)
    except ValueError:
        return
    assert isinstance(result, int)
    assert result >= 0


@given(st.one_of(st.text(max_size=20), st.none(), st.integers(), st.floats()))
def test_axle_class_fuzz_never_leaks_parser_errors(value):
    try:
        result = axle_class(value)
    except (ValueError, OverflowError):
        return
    assert result in {"car", "truck", "heavy"}


@given(
    state=st.from_regex(r"[A-Z]{2}", fullmatch=True),
    district=st.integers(min_value=0, max_value=99),
    series=st.from_regex(r"[A-Z]{1,3}", fullmatch=True),
    number=st.integers(min_value=0, max_value=9999),
)
def test_parse_plate_valid_inputs(state, district, series, number):
    plate = f"{state}-{district:02d}-{series}-{number:04d}"
    assert parse_plate(plate) == (state, district, series, number)


@given(
    count=st.integers(min_value=0, max_value=10000),
    rate=st.integers(min_value=0, max_value=10000),
)
def test_trip_cost_valid_inputs(count, rate):
    assert trip_cost(f"{count}x{rate}") == count * rate


@given(st.integers(min_value=2, max_value=30))
def test_axle_class_valid_inputs(axles):
    result = axle_class(axles)
    expected = "car" if axles == 2 else "truck" if axles <= 4 else "heavy"
    assert result == expected


@pytest.mark.parametrize(
    "plate",
    [None, "", "KA", "KA-05-1234", "KA-ABC-AB-1234",
     "KA-05-AB-12", "12-05-AB-1234", "KA-05-AB-12345"],
)
def test_parse_plate_rejects_invalid_values(plate):
    with pytest.raises(ValueError):
        parse_plate(plate)


@pytest.mark.parametrize(
    "value",
    [None, "", "3", "3xx150", "ax150", "3x", "x150", "-1x150", "3x-150"],
)
def test_trip_cost_rejects_invalid_values(value):
    with pytest.raises(ValueError):
        trip_cost(value)


@pytest.mark.parametrize(
    "value",
    [None, True, 0, 1, -2, 2.5, "", "abc", "inf", math.inf, math.nan],
)
def test_axle_class_rejects_invalid_values(value):
    with pytest.raises((ValueError, OverflowError)):
        axle_class(value)


def test_main_runs_with_valid_input(monkeypatch, capsys):
    answers = iter(["KA-05-AB-1234", "3x150", "3"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(answers))
    main()
    output = capsys.readouterr().out
    assert "('KA', 5, 'AB', 1234)" in output
    assert "Trip Cost: 450" in output
    assert "Vehicle Class: truck" in output
