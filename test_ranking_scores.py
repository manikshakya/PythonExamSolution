from unittest import TestCase

# import pytest

from ranking_scores import ranking_scores


class TestRanking_scores(TestCase):
    def test_eight_scores(self):
        assert [63, 64, 68, 69, 69] == ranking_scores([68, 72, 73, 69, 69, 64, 63, 75])

    def test_five_scores(self):
        assert [64, 64, 69, 74, 75] == ranking_scores([74, 69, 75, 64, 64])

    def test_three_scores(self):
        assert [63, 66, 70] == ranking_scores([66, 63, 70])

    def test_two_scores(self):
        with pytest.raises(ValueError):
            ranking_scores([72, 74])

    def test_no_scores(self):
        with pytest.raises(ValueError):
            ranking_scores([])
