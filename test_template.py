import unittest
import template as sut


class BusinessLogicTest(unittest.TestCase):

    def test_pattern1(self):
        input_data = [2, 10000]
        sut.business_logic(input_data)
