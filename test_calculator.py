import sys
import unittest
from unittest.mock import MagicMock

from PyQt6.QtWidgets import QApplication

from constants import Const

from main import (
    CalculatorApp,
)  # Предполагается, что ваш класс находится в файле calculator_app.py


class TestCalculatorApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Настройка приложения перед запуском тестов."""
        cls.app = QApplication(sys.argv)
        cls.calc_app = CalculatorApp()

    def test_initialization(self):
        """Проверка инициализации приложения."""
        self.assertIsNotNone(self.calc_app)
        self.assertIsNotNone(self.calc_app.txtFormula)
        self.assertIsNotNone(self.calc_app.txtResult)
        self.assertIsNotNone(self.calc_app.tblResults)

    def test_clear_all(self):
        """Проверка функции очистки всех полей."""
        self.calc_app.txtFormula.setPlainText("2 + 2")
        self.calc_app.txtResult.setPlainText("4")
        self.calc_app.clear_all_fields()
        self.assertEqual(self.calc_app.txtFormula.toPlainText(), "")
        self.assertEqual(self.calc_app.txtResult.toPlainText(), "")
        self.assertEqual(self.calc_app.tblResults.rowCount(), 0)

    def test_out_result(self):
        """Проверка вывода результата в текстовое поле и таблицу."""
        self.calc_app.output_result_to_text_field_and_history("2 + 2", "4")
        self.assertEqual(self.calc_app.txtResult.toPlainText(), "4")
        self.assertEqual(self.calc_app.tblResults.rowCount(), 1)
        self.assertEqual(self.calc_app.tblResults.item(0, 1).text(), "2 + 2")
        self.assertEqual(self.calc_app.tblResults.item(0, 2).text(), "4")

    def test_copy_result_clipboard(self):
        """Проверка копирования результата в буфер обмена."""
        self.calc_app.txtResult.setPlainText("4")
        self.calc_app.copy_result_to_clipboard()
        clipboard = QApplication.clipboard()
        self.assertEqual(clipboard.text(), "4")

    def test_write_history(self):
        """Проверка записи истории в CSV файл."""
        self.calc_app.output_result_to_text_field_and_history("2 + 2", "4")
        self.calc_app.write_history_to_csv_file()
        # Проверка, что файл был создан и содержит данные
        with open(Const.HISTORY_FILE_NAME, "r", encoding="utf-8-sig") as file:
            lines = file.readlines()
            self.assertGreater(
                len(lines), 1
            )  # Убедитесь, что в файле больше одной строки (заголовок + данные)

    def test_read_from_tblResults(self):
        """Проверка чтения данных из таблицы результатов."""
        self.calc_app.output_result_to_text_field_and_history("2 + 2", "4")
        results = self.calc_app.get_history_table_data()
        self.assertEqual(results, [("2 + 2", "4")])

    @classmethod
    def tearDownClass(cls):
        """Очистка после завершения тестов."""
        cls.calc_app.close()
        cls.app.quit()


if __name__ == "__main__":
    unittest.main()
