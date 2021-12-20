import unittest


def sum(x, y):
    result = x + y
    return result


class SampleTest(unittest.TestCase):

    @unittest.skip
    def test_sum_neg_float(self):
        self.assertEqual(sum(-4.5, -6.2), -10.7)

    @unittest.expectedFailure
    def test_sum_pos_int(self):
        self.assertEqual(sum(4, 6), 0)

    def test_sum_neg_int(self):
        self.assertEqual(sum(-4, -6), -10)

    def test_sum_pos_float(self):
        self.assertEqual(sum(4.5, 6.2), 10.7)

    def test_sum_neg_float(self):
        self.assertEqual(sum(-4.5, -6.2), -10.7)


if __name__ == '__main__':
    unittest.main()