from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QApplication

from constants import Const
from functions import (
    no_virus,
    calculate_and_validate_formula,
    normalize_characters,
)


class F:
    def __init__(self, calculator_app):
        self.calculator_app = calculator_app

    def formula_processing(self) -> None:
        """Получение формулы из текстового поля и её обработка"""
        formula = (
            self.calculator_app.txtFormula.toPlainText()
        )  # Получение текста формулы
        formula_standard = normalize_characters(formula)  # Стандартизация формулы
        # Проверка на допустимые символы
        if no_virus(formula_standard):
            self.calculator_app.output_result_to_text_field_and_history(
                formula, calculate_and_validate_formula(formula_standard)
            )  # Вывод результата
        else:
            self.calculator_app.output_result_to_text_field_and_history(
                formula, Const.ERROR_INVALID_SYMBOL
            )  # Вывод сообщения об ошибке

        self.calculator_app.txtFormula.setFocus()  # Установка фокуса на поле ввода

    def handle_key_press(self, event: QtGui.QKeyEvent) -> None:
        """Обработка нажатий клавиш, включая Enter, Esc"""

        keys = (
            self.handle_calculation_key_press(event),
            self.clear_on_escape_key(event),
        )
        if not any(keys):
            # Если нажатая не специальная клавиша, передаем событие дальше
            QtWidgets.QTextEdit.keyPressEvent(self.calculator_app.txtFormula, event)

    def handle_calculation_key_press(self, event: QtGui.QKeyEvent) -> bool:
        """Обработка нажатия клавишей вычисления формулы (Enter)."""

        keys = (Qt.Key.Key_Return, Qt.Key.Key_Enter, Qt.Key.Key_Equal)

        # Проверяем нажата ли клавиша "Ввод" и, если нажата, производим расчёт
        if event.key() in keys:
            self.formula_processing()  # Вычисление формулы при нажатии клавиши "Ввод"
            return True
        return False

    def clear_on_escape_key(self, event: QtGui.QKeyEvent) -> bool:
        """Обработка нажатия клавиши Esc для удаления символов из формулы."""

        if event.key() == Qt.Key.Key_Escape:
            self.calculator_app.clear_formula_and_result()
            return True
        return False

    def round_result(self):
        """Округление результатов вычислений"""

        result = self.calculator_app.txtResult.toPlainText()
        round_digit = int(self.calculator_app.lineRoundDigit.text())
        try:
            result_float = round(float(result), round_digit)
            result_str = f"{result_float:.{round_digit}f}"
            self.calculator_app.txtResult.setPlainText(result_str)
        except Exception:
            QApplication.beep()

    def set_decimal_places_input(self):
        """Настройка поля ввода числа десятичных знаков для округления"""

        # Установка правильности ввода числа знаков для округления
        validator = QIntValidator(*Const.DECIMAL_PLACE_RANGE)
        self.calculator_app.lineRoundDigit.setValidator(validator)

        # Установка по умолчанию числа знаков для округления
        self.calculator_app.lineRoundDigit.setText(str(Const.DEFAULT_DECIMAL_PLACES))
