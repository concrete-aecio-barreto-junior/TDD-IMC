import unittest

from app import imcCalculo 

class TestIMC(unittest.TestCase):

    def test_imc(self):
        self.assertEqual(imcCalculo(60,2.10), "abaixo")
        self.assertEqual(imcCalculo(65,1.80), "ideal")
        self.assertEqual(imcCalculo(84,1.80), "sobrepeso")
        self.assertEqual(imcCalculo(90,1.70), "obesidade 1")
        self.assertEqual(imcCalculo(105,1.65), "obesidade 2")
        self.assertEqual(imcCalculo(120,1.60), "obesidade 3")

if __name__ == '__main__':
    unittest.main()
