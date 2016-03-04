"""Tests for mailroom module."""
import pytest
RESPONSES = ['r', 'q', 't']
DONORS = {'Ben': [0, 1], 'Daniel': [12, 34, 56, 7, 89]}
donor_name = 'Ben'
donation_amount = 5


@pytest.mark.parametrize('responses', RESPONSES)
def test_validate_user_input(responses):
    """Assert user input is one of the valid choices."""
    from mailroom import validate_user_input
    assert validate_user_input(responses)


def test_add_donation():
    """Assert input string returns list as value."""
    from mailroom import add_donation
    add_donation(donor_name, donation_amount, DONORS)
    assert donation_amount == DONORS[donor_name][-1]


def test_donation_totals():
    """Assert donations are added correctly."""
    from mailroom import donation_totals
    assert donation_totals(DONORS, donor_name) == sum(DONORS[donor_name])


def test_donation_qty():
    """Assert donations are added correctly."""
    from mailroom import donation_qty
    assert donation_qty(DONORS, donor_name) == len(DONORS[donor_name])


def test_donation_avg():
    """Assert donations are added correctly."""
    from mailroom import donation_avg
    value = DONORS[donor_name]
    avg = sum(value) // len(value)
    assert donation_avg(DONORS, donor_name) == avg

