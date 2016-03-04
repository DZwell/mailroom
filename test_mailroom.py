"""Tests for mailroom module."""
import pytest
RESPONSES = ['r', 'q', 't']
DONORS = {'Ben': [0, 1], 'Daniel': [123456789]}
donor_name = 'Ben'
donation_amount = 5


# def test_start():
#     """Assert something printed to the screen."""
#     from mailroom import start
#     assert


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
