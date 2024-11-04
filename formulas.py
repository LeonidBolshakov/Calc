from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt

from constants import Const
from fuctions import (
    no_virus,
    calculation,
    symbol_standardization,
)


class F:
    def __init__(self, calculator_app):
        self.calculator_app = calculator_app

    def formula_processing(self) -> None:
        """Получение формулы из текстового поля и её обработка"""
        formula = (
            self.calculator_app.txtFormula.toPlainText()
        )  # Получение текста формулы
        formula_standard = symbol_standardization(formula)  # Стандартизация формулы
        # Проверка на допустимые символы
        if no_virus(formula_standard):
            self.calculator_app.output_calculation_result(
                formula, calculation(formula_standard)  # вычисление
            )  # Вывод результата
        else:
            self.calculator_app.output_calculation_result(
                formula, Const.TEXT_ERROR_SYMBOL
            )

        self.calculator_app.txtFormula.setFocus()  # Установка фокуса на поле ввода

    def handle_key_press(self, event: QtGui.QKeyEvent) -> None:
        """Обработка нажатий клавиш, включая Enter, Esc"""

        keys = (self.check_press_calc(event), self.check_press_esc(event))
        if not any(keys):
            # Если нажатая не специальная клавиша, передаем событие дальше
            QtWidgets.QTextEdit.keyPressEvent(self.calculator_app.txtFormula, event)

    def check_press_calc(self, event: QtGui.QKeyEvent) -> bool:
        """Обработка нажатия клавишей вычисления формулы (Enter)."""

        keys = (Qt.Key.Key_Return, Qt.Key.Key_Enter, Qt.Key.Key_Equal)

        # Проверяем нажата ли клавиша "Ввод" и, если нажата, производим расчёт
        if event.key() in keys:
            self.formula_processing()  # Вычисление формулы при нажатии клавиши "Ввод"
            return True
        return False

    def check_press_esc(self, event: QtGui.QKeyEvent) -> bool:
        """Обработка нажатия клавиши Esc для удаления символов из формулы."""

        if event.key() == Qt.Key.Key_Escape:
            self.calculator_app.clear_formula_result()
            return True
        return False
