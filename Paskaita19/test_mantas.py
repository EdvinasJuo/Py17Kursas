import unittest
import mantas

class TestKeliamieji(unittest.TestCase):
    def setUp(self):
        self.objektas = mantas.Zmogus("Jonas", 30)

    def test_tikrinti_varda_ir_amzius(self):
        self.assertEqual(self.objektas.gauti_informacija(), "Žmogaus vardas: Jonas, Amžius: 30")

    def test_vardo_tipo_patikra(self):
        with self.assertRaises(TypeError):
            self.objektas = mantas.Zmogus(1, 30)

    def test_amziaus_tipo_patikra(self):
        with self.assertRaises(TypeError):
            self.objektas = mantas.Zmogus("Jonas", "jonas")

if __name__ == "__main__":
    unittest.main()