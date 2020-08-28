from unittest import TestCase

from divisors import divisors


class TestDivisors(TestCase):
    def test_divisors_of_18(self):
        assert [2, 3, 6, 9] == divisors(18)

    def test_divisors_of_27(self):
        assert [3, 9] == divisors(27)

    def test_divisors_of_31(self):
        assert [] == divisors(31)
