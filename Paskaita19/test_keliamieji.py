import unittest
from keliamieji import Keliamieji

class TestKeliamieji(unittest.TestCase):

    def setUp(self):
        self.obj = Keliamieji()
    def test_ar_keliamieji(self):
        # ARRANGE
        actual_result = self.obj.ar_keliamieji(2000)
        # ACT
        expected_result = "Keliamieji"
        # ASSERT
        self.assertEqual(expected_result, actual_result)
        self.assertEqual("Keliamieji", self.obj.ar_keliamieji(2020)) # KITAS VARIANTAS
        self.assertEqual("Nekeliamieji", self.obj.ar_keliamieji(2100))   # KITAS VARIANTAS

    def test_ar_keliamieji2(self):
        self.assertTrue(self.obj.ar_keliamieji(2000))    # PAVYZDYS SU TRUE ARBA FALSE
        self.assertTrue(self.obj.ar_keliamieji2(2020))
        self.assertFalse(self.obj.ar_keliamieji2(2100))

    def test_diapazonas(self):
        actual_result = self.obj.diapazonas(1980, 2000)
        expected_result = [1980, 1984, 1988, 1992, 1996]
        self.assertEqual(expected_result, actual_result)