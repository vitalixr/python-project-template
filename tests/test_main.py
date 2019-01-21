from big_bang import sum


class TestSum(object):
    def test_sum(self):
        assert sum.sum(1, 2) == 3
