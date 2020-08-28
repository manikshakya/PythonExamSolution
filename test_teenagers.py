from unittest import TestCase

from teenagers import teenagers


class TestTeenagers(TestCase):
    def test_mixed_ages_1(self):
        assert [15, 19] == teenagers([15, 27, 5, 22, 51, 52, 49, 41, 19, 65])

    def test_mixed_ages_2(self):
        assert [13, 14, 15] == teenagers([10, 11, 12, 13, 14, 15, 20])

    def test_no_teenagers(self):
        assert [] == teenagers([22, 42, 32, 7, 49, 23, 23, 10, 47, 28])
