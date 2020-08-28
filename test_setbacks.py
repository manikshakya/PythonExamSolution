from unittest import TestCase

from setbacks import setbacks


class TestSetbacks(TestCase):
    def test_random_sequence(self):
        assert [141, 164, 156, 163] == setbacks([140, 150, 165, 141, 164, 156, 187, 163])

    def test_no_setbacks(self):
        assert [] == setbacks([140, 150, 165, 170])

    def test_single_competition(self):
        assert [] == setbacks([140])

    def test_start_of_season(self):
        assert [] == setbacks([])
