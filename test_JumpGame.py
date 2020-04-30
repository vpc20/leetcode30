from unittest import TestCase

from JumpGame import can_jump, can_jump_dyna, can_jump_dyna1
from RandomData import random_int_array


class Test(TestCase):
    def test_can_jump(self):
        for _ in range(10000):
            arr = random_int_array(10, 10)
            if arr:
                # print(arr)
                # print(can_jump(arr))
                self.assertEqual(can_jump(arr), can_jump_dyna(arr))
                self.assertEqual(can_jump(arr), can_jump_dyna1(arr))
