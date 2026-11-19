import pytest
from atm_withdrawal import withdraw, pin_check, note_breakup

#Example test cases:
def test_simple_withdrawal():
    assert withdraw(5000, 1000, "savings", True) == 4000

def test_correct_pin():
    assert pin_check(1234, 1234, 0) == "ok"


def test_savings_withdrawal_with_fee():
    assert withdraw(20000, 10000, "savings", False) == 9980


def test_current_withdrawal_limit():
    assert withdraw(60000, 60000, "current", True) == "limit exceeded"


def test_unknown_account():
    with pytest.raises(ValueError):
        withdraw(1000, 100, "checking", True)


def test_invalid_amount():
    with pytest.raises(ValueError):
        withdraw(1000, -100, "savings", True)


def test_insufficient_funds():
    assert withdraw(500, 1000, "savings", True) == "insufficient funds"


def test_pin_blocked_on_attempt_limit():
    assert pin_check(1234, 4321, 3) == "card blocked"


def test_pin_blocked_after_second_retry():
    assert pin_check(1234, 4321, 2) == "card blocked"


def test_pin_retry():
    assert pin_check(1234, 4321, 1) == "retry"


def test_note_breakup():
    assert note_breakup(1700) == (3, 1, 0)


def test_invalid_note_breakup():
    with pytest.raises(ValueError):
        note_breakup(150)
