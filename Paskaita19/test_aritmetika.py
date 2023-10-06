import unittest
import aritmetika


class TestAritmetika(unittest.TestCase):
    def test_sudetis(self):
        #ARRANGE
        actual_result = 10 + 5
        #ACT
        expected_result = 15
        #ASSERT
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(15, aritmetika.sudetis(10, 5))
        self.assertEqual(0, aritmetika.sudetis(-1, 1))
        self.assertEqual(-2, aritmetika.sudetis(-1, -1))

    def test_atimtis(self):
        # ARRANGE
        actual_result = 10 - 5
        # ACT
        expected_result = 5
        # ASSERT
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(5, aritmetika.atimtis(10, 5))
        self.assertEqual(-2, aritmetika.atimtis(-1, 1))
        self.assertEqual(0, aritmetika.atimtis(-1, -1))

    def test_daugyba(self):
        # ARRANGE
        actual_result = 10 * 5
        # ACT
        expected_result = 50
        # ASSERT
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(50, aritmetika.daugyba(10, 5))
        self.assertEqual(-1, aritmetika.daugyba(-1, 1))
        self.assertEqual(1, aritmetika.daugyba(-1, -1))

    def test_dalyba(self):
        # ARRANGE
        actual_result = 10 / 5
        # ACT
        expected_result = 2
        # ASSERT
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(2, aritmetika.dalyba(10, 5))
        self.assertEqual(-1, aritmetika.dalyba(-1, 1))
        self.assertEqual(1, aritmetika.dalyba(-1, -1))

# ASSERTRAISES NAUDOJAM KLAIDOS KODA, FUNKCIJOS PAVADINIMA IR PARASOM PARAMETRU KIEKI ATSKIRIANT KABLELIAIS
        self.assertRaises(TypeError, aritmetika.dalyba, 5, "zodis")
        self.assertRaises(ZeroDivisionError, aritmetika.dalyba, 5, 0)
# KITAS BUDAS APRASYT SU KLAIDOS ERRORU
        with self.assertRaises(TypeError):
            aritmetika.dalyba(5, "zodis")
        with self.assertRaises(ZeroDivisionError):
            aritmetika.dalyba(5, 0)