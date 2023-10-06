import unittest

import Task1
from Task1 import sum_of_numbers_list, find_highest_number, prime_numbers

class TestTask1(unittest.TestCase):
    def test_sum_of_positive_numbers_list(self):
        numbers_list = [1, 2, 3, 12, 43]
        self.assertEqual(sum_of_numbers_list(numbers_list), 61)

    def test_sum_of_negative_numbers_in_list(self):
        numbers_list = [-1, -2, -3, -12, -43]
        self.assertEqual(sum_of_numbers_list(numbers_list), -61)

    def test_sum_of_empty_list(self):
        numbers_list = []
        self.assertEqual(sum_of_numbers_list(numbers_list), 0)

    def test_sum_of_string_list(self):
        numbers_list = ['Labas', 'Ka']
        self.assertRaises(TypeError, Task1.sum_of_numbers_list, numbers_list)

    def test_find_highest_number_with_positive_numbers(self):
        result = find_highest_number(1, 5, 3, 4, 8, 9)
        self.assertEqual(result, 9)

    def test_find_highest_number_with_negative_numbers(self):
        result = find_highest_number(-1, -5, -3, -4)
        self.assertEqual(result, -1)

    def test_find_highest_number_with_mixed_numbers(self):
        result = find_highest_number(-1, 20, -80, 10, -3)
        self.assertEqual(result, 20)

    def test_find_highest_number_with_single_number(self):
        result = find_highest_number(8)
        self.assertEqual(result, 8)

    def test_find_highest_number_with_words_in_argument(self):
        self.assertRaises(TypeError, Task1.find_highest_number, 5, "Labas")

    def test_prime_numbers(self):
        self.assertEqual("Pirminis", prime_numbers(2))
        self.assertEqual("Pirminis", prime_numbers(7))
        self.assertEqual("Nera pirminis", prime_numbers(6))
        self.assertEqual("Nera pirminis", prime_numbers(-10))
        self.assertRaises(TypeError, Task1.prime_numbers, 2, "Labas")
