import unittest
from sparse_filler import fill_sparse


class TestSparseFiller(unittest.TestCase):

    def test_line_list(self):
        # call method under test
        self.assertEqual(fill_sparse.line_list('2 5:1 8:1'), ['2', '5:1', '8:1'])

    def test_int_element_zero(self):
        # call method under test
        self.assertEqual(fill_sparse.int_element_zero(['2', '5:1', '8:1']), 2)
