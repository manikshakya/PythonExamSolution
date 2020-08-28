from unittest import TestCase

import pytest

from bank_details import bank_details


class TestBank_details(TestCase):
    def test_valid_aib_with_spaces(self):
        assert ['931152', '12345678'] == bank_details('IE29 AIBK 9311 5212 3456 78')

    def test_valid_aib_with_different_spacing(self):
        assert ['931152', '12345678'] == bank_details('IE29 AIBK 931152 12345678')

    def test_valid_aib_with_no_spaces(self):
        assert ['521293', '11347856'] == bank_details('IE29AIBK52129311347856')

    def test_valid_bank_of_ireland_with_spaces(self):
        assert ['485738', '47193465'] == bank_details('IE29 BOFI 4857 3847 1934 65')

    def test_account_number_too_short(self):
        with pytest.raises(ValueError):
            bank_details('IE29 AIBK 9311 5212 3456')

    def test_account_number_too_long(self):
        with pytest.raises(ValueError):
            bank_details('IE29 AIBK 9311 5212 3456 7856')

    def test_bank_reference_contains_digits(self):
        with pytest.raises(ValueError):
            bank_details('IE29 AI42 9311 5212 3456 78')

    def test_country_not_ireland(self):
        with pytest.raises(ValueError):
            bank_details('UK29 AIBK 9311 5212 3456 78')

    def test_check_digits_must_be_digits(self):
        with pytest.raises(ValueError):
            bank_details('IEAB AIBK 9311 5212 3456 78')
