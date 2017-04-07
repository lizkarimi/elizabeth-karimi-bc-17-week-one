
import unittest
from prime_num_gen import prime_num_gen

class prime_num_gen_TestCases(unittest.TestCase):
    def test_it_returns_prime_numbers(self):
        result = prime_num_listing(8)
        self.assertEqual(result,[2, 3, 5, 7], msg="It should return a list of prime numbers for range(8)")


    def test_it_returns_emptylist_for_an_input_of_1(self):
        result = prime_num_gen(1)
        self.assertEquals(result,[],"It should return an empty list for an input of 1")


    def test_it_RaisesValueError_for_a_Negative_input(self):
        with assertRaises(ValueError):
        prime_num_gen(-7)


    def test_it_returns_anemptylist_for_0_input(self):
        result = prime_num_gen(0)
        self.assertEquals(result,[],"should return an empty list for 0 input")


    def test_it_does_not_accept_strings(self):
         with self.assertRaises(ValueError) as context:
             prime_num_gen("str")
        self.assertEqual("input given is incorrect.",context.exception.message, "Doesn't allow Invalid input of type str")
