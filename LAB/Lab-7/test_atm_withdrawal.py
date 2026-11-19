# Name: Bhavish A | SRN: PES2UG24AM040
# Fuzz tests for atm_withdrawal.py using Hypothesis.
# Each function is fed random text (and None) and must never crash.
# For valid-looking inputs we also check that the answer is correct.
from hypothesis import given, strategies as st
from atm_withdrawal import notes_needed, mask_card, average_withdrawal


@given(st.text() | st.none())
def test_notes_needed_no_crash(s):
    try:
        result = notes_needed(s)
    except Exception as e:
        assert False, f"notes_needed crashed with: {e!r}"
    assert result is None or (isinstance(result, int) and result >= 0)


@given(st.integers(min_value=0, max_value=10**9))
def test_notes_needed_correct(n):
    assert notes_needed(f"{n:,}") == n // 100


@given(st.text() | st.none())
def test_mask_card_no_crash(s):
    try:
        result = mask_card(s)
    except Exception as e:
        assert False, f"mask_card crashed with: {e!r}"
    assert result is None or result.startswith("XXXX XXXX XXXX ")


@given(st.from_regex(r"[0-9]{4} [0-9]{4} [0-9]{4} [0-9]{4}", fullmatch=True))
def test_mask_card_correct(card):
    assert mask_card(card) == "XXXX XXXX XXXX " + card[-4:]


@given(st.text() | st.none())
def test_average_withdrawal_no_crash(s):
    try:
        result = average_withdrawal(s)
    except Exception as e:
        assert False, f"average_withdrawal crashed with: {e!r}"
    assert result is None or isinstance(result, int)


@given(st.lists(st.integers(min_value=0, max_value=10**6), min_size=1))
def test_average_withdrawal_correct(amounts):
    csv = ",".join(str(a) for a in amounts)
    assert average_withdrawal(csv) == sum(amounts) // len(amounts)
