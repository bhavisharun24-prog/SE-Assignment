# Name: Bhavish A | SRN: PES2UG24AM040
# Test cases written to get 90%+ branch coverage of atm_withdrawal.py.
# Every if-statement is tested for both its True and False outcome.
import pytest
from atm_withdrawal import withdraw, pin_check, note_breakup


# ---- withdraw ----
def test_own_bank_no_fee():                       # own_bank True -> skip fee block
    assert withdraw(5000, 1000, "savings", True) == 4000

def test_unknown_account():                       # account_type not in DAILY_LIMIT
    with pytest.raises(ValueError):
        withdraw(5000, 1000, "salary", True)

def test_zero_amount():                           # amount <= 0
    with pytest.raises(ValueError):
        withdraw(5000, 0, "savings", True)

def test_negative_amount():
    with pytest.raises(ValueError):
        withdraw(5000, -500, "savings", True)

def test_amount_not_multiple_of_100():           # amount % 100 != 0
    with pytest.raises(ValueError):
        withdraw(5000, 150, "savings", True)

def test_savings_limit_exceeded():                # amount > daily limit
    assert withdraw(100000, 25100, "savings", True) == "limit exceeded"

def test_savings_exactly_at_limit():              # boundary: amount == limit is allowed
    assert withdraw(100000, 25000, "savings", True) == 75000

def test_current_account_higher_limit():          # same amount is fine on current
    assert withdraw(100000, 30000, "current", True) == 70000

def test_current_limit_exceeded():
    assert withdraw(100000, 50100, "current", True) == "limit exceeded"

def test_other_bank_small_amount_fee():           # not own_bank, amount <= 10000 -> fee 20
    assert withdraw(5000, 1000, "savings", False) == 3980

def test_other_bank_exactly_10000():              # boundary: 10000 is not > 10000
    assert withdraw(20000, 10000, "savings", False) == 9980

def test_other_bank_large_amount_fee():           # not own_bank, amount > 10000 -> fee 30
    assert withdraw(50000, 20000, "current", False) == 29970

def test_insufficient_funds():                    # amount + fee > balance
    assert withdraw(500, 1000, "savings", True) == "insufficient funds"

def test_insufficient_only_because_of_fee():      # amount fits, but fee pushes it over
    assert withdraw(1000, 1000, "savings", False) == "insufficient funds"

def test_exact_balance():                         # amount + fee == balance is allowed
    assert withdraw(1020, 1000, "savings", False) == 0


# ---- pin_check ----
def test_correct_pin_first_try():
    assert pin_check(1234, 1234, 0) == "ok"

def test_correct_pin_last_try():                  # correct on the 3rd attempt (attempts == 2)
    assert pin_check(1234, 1234, 2) == "ok"

def test_already_blocked():                       # attempts >= 3, even with right pin
    assert pin_check(1234, 1234, 3) == "card blocked"

def test_more_than_three_attempts():
    assert pin_check(1111, 1234, 5) == "card blocked"

def test_wrong_pin_third_attempt():               # wrong and attempts == 2
    assert pin_check(1111, 1234, 2) == "card blocked"

def test_wrong_pin_retry():                       # wrong and attempts < 2
    assert pin_check(1111, 1234, 1) == "retry"


# ---- note_breakup ----
def test_note_breakup_invalid():
    with pytest.raises(ValueError):
        note_breakup(250)

def test_note_breakup_with_200s():                # remaining >= 200
    assert note_breakup(1800) == (3, 1, 1)

def test_note_breakup_remaining_exactly_200():
    assert note_breakup(700) == (1, 1, 0)

def test_note_breakup_without_200s():             # remaining < 200
    assert note_breakup(1100) == (2, 0, 1)

def test_note_breakup_only_500s():
    assert note_breakup(1500) == (3, 0, 0)
