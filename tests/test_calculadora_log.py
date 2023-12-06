import unittest
import tkinter as tk
import math
from unittest.mock import patch

from app.calculadora import Calculadora

class TestCalculadoraLog(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.calc = Calculadora(self.root)

    @patch('app.calculadora.math.log10')
    def test_calculate_log_valid_expression(self, mock_log10):
        expression = '10'
        self.calc._entrada.delete(0, tk.END)
        self.calc._entrada.insert(0, expression)
        mock_log10.return_value = 1.0

        self.calc._calculate_log() 
        mock_log10.assert_called_once_with(eval(expression))

        result_displayed = self.calc._entrada.get()
        self.assertEqual(result_displayed, '1.0')


    

if __name__ == '__main__':
    unittest.main()