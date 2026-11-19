"""Starter tests retained for the Highway Toll Lab 6 submission."""

from highway_toll import toll_charge, toll_for


def test_ambulance_is_exempt():
    assert toll_charge("ambulance", 2, False, False) == 0


def test_two_axle_base_toll():
    assert toll_for(2, False, False) == 100
