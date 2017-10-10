import unittest
from sparse_filler import line_list


class TestSparseFiller(unittest.TestCase):

    def test_line_list(self):
        # call method under test
        self.assertEqual(line_list('2 5:1 8:1'), ['2', '5:1', '8:1'])

