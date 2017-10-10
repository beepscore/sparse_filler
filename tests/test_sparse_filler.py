import unittest
from sparse_filler import fill_sparse


class TestSparseFiller(unittest.TestCase):

    def test_line_list(self):
        self.assertEqual(fill_sparse.line_list('2 5:1 8:1'), ['2', '5:1', '8:1'])

    def test_int_element_zero(self):
        self.assertEqual(fill_sparse.int_element_zero(['2', '5:1', '8:1']), 2)

    def test_int_before_colon(self):
        self.assertEqual(fill_sparse.int_before_colon('5:1'), 5)

    def test_filled(self):
        self.assertEqual(fill_sparse.filled('2 5:1 8:1'), [2, 0, 0, 0, 0, 1, 0, 0, 1])
