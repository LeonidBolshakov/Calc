# Запуск теста
# python -m unittest test_calculator.py

import unittest
from unittest.mock import patch

from PyQt6.QtWidgets import QApplication

from main import CalculatorApp


class TestCalculatorApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])  # Создаем экземпляр QApplication
        cls.calc_app = CalculatorApp()  # Создаем экземпляр CalculatorApp

    def test_symbol_standardization(self):
        # Проверка замены нестандартных символов
        formula = "1,5 + 2_3"
        expected = "1.5+23"
        result = self.calc_app.symbol_standardization(formula)
        self.assertEqual(result, expected)

    def test_antivirus_invalid(self):
        # Проверка на недопустимые символы
        formula = "1 + 2 * (3 - 4) @"
        result = self.calc_app.antivirus(formula)
        self.assertFalse(result)

    @patch("PyQt6.QtWidgets.QApplication.clipboard")
    def test_click_button_copy(self, mock_clipboard):
        # Проверка копирования результата в буфер обмена
        self.calc_app.txtResult.setPlainText("Результат")
        self.calc_app.click_button_copy()
        mock_clipboard().setText.assert_called_with("Результат")

    def test_click_button_clear(self):
        # Проверка очистки текстового поля
        self.calc_app.txtFormula.setPlainText("Тест")
        self.calc_app.click_button_clear()
        self.assertEqual(self.calc_app.txtFormula.toPlainText(), "")

    def test_calculation_valid(self):
        # Проверка корректного вычисления
        formula = "1 + 2"
        result = self.calc_app.calculation(formula)
        self.assertEqual(result, "3")

    def test_calculation_division_by_zero(self):
        # Проверка деления на ноль
        formula = "1 / 0"
        result = self.calc_app.calculation(formula)
        self.assertEqual(result, "Ошибка. Деление на 0")

    def test_calculation_invalid_expression(self):
        # Проверка обработки некорректного выражения
        formula = "1 + "
        result = self.calc_app.calculation(formula)
        self.assertEqual(result, "Ошибка")


if __name__ == "__main__":
    unittest.main()
