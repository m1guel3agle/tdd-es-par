import unittest

from math_utils import es_par, es_impar, es_positivo, es_negativo


class TestEsPar(unittest.TestCase):

    def test_4_es_par(self):
        self.assertTrue(es_par(4))

    def test_5_no_es_par(self):
        self.assertFalse(es_par(5))


class TestEsImpar(unittest.TestCase):

    def test_3_es_impar(self):
        self.assertTrue(es_impar(3))

    def test_4_no_es_impar(self):
        self.assertFalse(es_impar(4))


class TestEsPositivo(unittest.TestCase):

    def test_5_es_positivo(self):
        self.assertTrue(es_positivo(5))

    def test_menos_5_no_es_positivo(self):
        self.assertFalse(es_positivo(-5))


class TestEsNegativo(unittest.TestCase):

    def test_menos_3_es_negativo(self):
        self.assertTrue(es_negativo(-3))

    def test_3_no_es_negativo(self):
        self.assertFalse(es_negativo(3))


if __name__ == "__main__":
    unittest.main()