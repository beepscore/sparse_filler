import unittest
from sparse_filler import fill_sparse


class TestSparseFiller(unittest.TestCase):

    def test_line_list(self):
        self.assertEqual(fill_sparse.line_list('2 5:1 8:1'), ['2', '5:1', '8:1'])

    def test_int_element_zero(self):
        self.assertEqual(fill_sparse.int_element_zero(['2', '5:1', '8:1']), 2)
        self.assertEqual(fill_sparse.int_element_zero('0 2:1 5:1 7:1'), 0)

    def test_ints_from_string_with_colon(self):
        self.assertEqual(fill_sparse.ints_from_string_with_colon('5:1'), [5, 1])

    def test_ints_from_string_with_colon_no_colon(self):
        self.assertEqual(fill_sparse.ints_from_string_with_colon('51'), None)

    def test_ints_from_string_with_colon_too_many_ints(self):
        self.assertEqual(fill_sparse.ints_from_string_with_colon('5:1:3'), None)

    def test_int_before_colon(self):
        self.assertEqual(fill_sparse.int_before_colon('5:1'), 5)

    def test_int_before_colon_no_colon(self):
        self.assertEqual(fill_sparse.int_before_colon('5'), None)

    def test_int_after_colon(self):
        self.assertEqual(fill_sparse.int_after_colon('5:1'), 1)

    def test_int_after_colon_no_colon(self):
        self.assertEqual(fill_sparse.int_after_colon('5'), None)

    def test_filled(self):
        self.assertEqual(fill_sparse.filled('2 5:1 8:1'), [2, 0, 0, 0, 0, 1, 0, 0, 1])
        self.assertEqual(fill_sparse.filled('0 2:1 5:1 7:1'), [0, 0, 1, 0, 0, 1, 0, 1])

    def test_filled_consecutive_ones(self):
        self.assertEqual(fill_sparse.filled('1 2:1 3:1 7:1 10:1'), [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1])

    def test_filled_int_before_colon_not_sorted_ascending(self):
        self.assertEqual(fill_sparse.filled('1 5:1 3:1'), None)

    def test_list_of_lists(self):
        input_filename = "../data/test_input1.txt"
        expected = [[1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1], [2, 0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 0, 1], [2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1]]
        self.assertEqual(fill_sparse.list_of_lists(input_filename), expected)
