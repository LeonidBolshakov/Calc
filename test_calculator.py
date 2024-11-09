import unittest
from unittest.mock import patch

from PyQt6.QtWidgets import QApplication, QTextEdit
from PyQt6 import QtGui
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtTest import QTest
from PyQt6.QtGui import QKeyEvent

from main import CalculatorApp
from constants import Const
import functions


# noinspection PyUnusedLocal
class TestCalculatorApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])  # Создаем экземпляр QApplication
        cls.calculator = CalculatorApp()  # Создаём экземпляр калькулятора

    @patch("main.ask_for_continuation", return_value=True)  # Подмена функции
    def test_clear_all_fields(self, mock_ask):
        """Тестирование очистки всех полей"""
        self.calculator.txtFormula.setPlainText("2 + 2")
        self.calculator.f.formula_processing()
        self.calculator.clear_all_fields()  # Здесь вызывается ask_for_continuation
        self.assertEqual(self.calculator.txtFormula.toPlainText(), "")
        self.assertEqual(self.calculator.txtResult.toPlainText(), "")
        self.assertEqual(self.calculator.tblResults.rowCount(), 0)

    def test_copy_result_to_clipboard(self):
        """Тестирование копирования результата в буфер обмена"""
        self.calculator.txtResult.setPlainText("4")
        self.calculator.copy_result_to_clipboard()
        clipboard = QApplication.clipboard()
        self.assertEqual(clipboard.text(), "4")

    def test_formula_processing_valid(self):
        """Тестирование обработки корректной формулы"""
        self.calculator.txtFormula.setPlainText("2 + 2")
        self.calculator.f.formula_processing()
        self.assertEqual(self.calculator.txtResult.toPlainText(), "4")

        self.calculator.txtFormula.setPlainText("sin(1)**2 + cos(1)^2")
        self.calculator.f.formula_processing()
        self.assertEqual(self.calculator.txtResult.toPlainText(), "1.0")

    def test_formula_processing_invalid(self):
        """Тестирование обработки некорректной формулы"""
        self.calculator.txtFormula.setPlainText("2 + ш")
        self.calculator.f.formula_processing()
        self.assertEqual(
            self.calculator.txtResult.toPlainText(), Const.ERROR_INVALID_SYMBOL
        )

        self.calculator.txtFormula.setPlainText("2 + *")
        self.calculator.f.formula_processing()
        self.assertEqual(self.calculator.txtResult.toPlainText(), Const.ERROR_SYNTAX)

        self.calculator.txtFormula.setPlainText("2/0")
        self.calculator.f.formula_processing()
        self.assertEqual(
            self.calculator.txtResult.toPlainText(), Const.ERROR_DIVIDE_BY_ZERO
        )

    def test_round_result(self):
        """Тестирование округления результата"""
        self.calculator.txtResult.setPlainText("3.14159")
        self.calculator.lineRoundDigit.setText("2")
        self.calculator.f.round_result()
        self.assertEqual(self.calculator.txtResult.toPlainText(), "3.14")

    def test_insert_new_row_in_results(self):
        """Тестирование добавления новой строки в таблицу результатов"""
        self.calculator.clear_table_results()
        self.calculator.insert_new_row_in_results("2 + 2", "4")
        self.assertEqual(self.calculator.tblResults.rowCount(), 1)
        self.assertEqual(self.calculator.tblResults.item(0, 1).text(), "2 + 2")
        self.assertEqual(self.calculator.tblResults.item(0, 2).text(), "4")

    def test_bold_font(self):
        """Тестирование установки жирного начертания шрифта"""
        font = QtGui.QFont()
        functions.bold_font(font)
        self.assertEqual(font.bold(), True)


if __name__ == "__main__":
    unittest.main()
