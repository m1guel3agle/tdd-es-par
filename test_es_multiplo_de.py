import unittest

from math_utils import es_multiplo_de


class TestEsMultiploDe(unittest.TestCase):

    def test_multiplo_positivo(self):
        self.assertTrue(es_multiplo_de(10, 5))

    def test_multiplo_con_negativos(self):
        self.assertTrue(es_multiplo_de(-10, 5))

    def test_multiplo_de_cero(self):
        self.assertFalse(es_multiplo_de(10, 0))


if __name__ == "__main__":
    unittest.main()