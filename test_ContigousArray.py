from unittest import TestCase

from ContigousArray import find_max_len_brute, find_max_len


class Test(TestCase):
    def test_find_max_len_brute(self):
        for i in range(4096):
            b = bin(i)[2:]
            b_arr = [int(c) for c in b]
            print(b_arr)
            self.assertEqual(find_max_len_brute(b_arr), find_max_len(b_arr))
