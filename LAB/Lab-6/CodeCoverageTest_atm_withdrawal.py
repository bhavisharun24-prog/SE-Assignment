# Name: Bhavish A | SRN: PES2UG24AM040
# Test cases written to get 90%+ line (code) coverage of atm_withdrawal.py
import pytest
from atm_withdrawal import withdraw, pin_check, note_breakup


# ---- withdraw ----
def test_simple_withdrawal():
    assert withdraw(5000, 1000, "savings", True) == 4000

def test_unknown_account():
    with pytest.raises(ValueError):
        withdraw(5000, 1000, "salary", True)

def test_invalid_amount():
    with pytest.raises(ValueError):
        withdraw(5000, 150, "savings", True)

def test_limit_exceeded():
    assert withdraw(100000, 30000, "savings", True) == "limit exceeded"

def test_other_bank_large_amount_fee():
    # other bank, amount above 10000 -> fee 20 + 10
    assert withdraw(50000, 20000, "current", False) == 50000 - 20000 - 30

def test_insufficient_funds():
    assert withdraw(500, 1000, "savings", True) == "insufficient funds"


# ---- pin_check ----
def test_correct_pin():
    assert pin_check(1234, 1234, 0) == "ok"

def test_already_blocked():
    assert pin_check(1234, 1234, 3) == "card blocked"

def test_wrong_pin_third_attempt():
    assert pin_check(1111, 1234, 2) == "card blocked"

def test_wrong_pin_retry():
    assert pin_check(1111, 1234, 0) == "retry"


# ---- note_breakup ----
def test_note_breakup_invalid():
    with pytest.raises(ValueError):
        note_breakup(250)

def test_note_breakup_with_200s():
    assert note_breakup(1800) == (3, 1, 1)

def test_note_breakup_without_200s():
    assert note_breakup(1100) == (2, 0, 1)
