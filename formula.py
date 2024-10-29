import constant as c
from contextlib import redirect_stderr
import io

from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt


class NullIO(io.StringIO):
    """Класс для подавления вывода ошибок в консоль."""

    def write(self, *args, **kwargs):
        pass


class F:
    def __init__(self, calculator):
        self.calculator = calculator

    def calculate_formula(self) -> None:
        """Получение формулы из текстового поля и вычисление результата"""

        formula = self.calculator.txtFormula.toPlainText()  # Получение текста формулы
        self.formula_processing(formula)  # Обработка формулы
        self.calculator.txtFormula.setFocus()  # Установка фокуса обратно на поле ввода

    def formula_processing(self, formula: str) -> None:
        """Обработка формулы: стандартизация, проверка и вычисление."""

        formula_st = self.symbol_standardization(formula)  # Стандартизация формулы
        if self.antivirus(formula_st):  # Проверка на допустимые символы
            self.calculator.out_result(
                formula, self.calculation(formula_st)
            )  # Вывод результата
        else:
            self.calculator.out_result(formula, c.Const.TEXT_ERROR_SYMBOL)

    @staticmethod
    def symbol_standardization(formula: str) -> str:
        """Заменяем нестандартные символы стандартными"""

        # Создание таблицы перевода
        translation_table = str.maketrans(c.Const.REPLACE_SYMBOLS)

        return formula.translate(translation_table)  # Применение замены к формуле

    # noinspection PyBroadException
    @staticmethod
    def calculation(formula: str) -> str:
        """Вычисление результата формулы с обработкой ошибок."""
        try:
            with redirect_stderr(NullIO()):  # Подавление вывода ошибок на консоль
                return str(eval(formula))  # Вычисление по формуле
        except ZeroDivisionError:
            return c.Const.TEXT_DEVISE_0  # Обработка деления на ноль
        except Exception:
            return c.Const.TEXT_SYNTAX_ERROR  # Обработка всех других ошибок

    @staticmethod
    def antivirus(formula: str) -> bool:
        """Проверка формулы на наличие только допустимых символов.
        Защищает программу от ввода вредоносного кода."""

        return all(
            char in c.Const.SAFE_SYMBOLS for char in formula
        )  # Возвращает True, если все символы допустимы

    def handle_key_press(self, event: QtGui.QKeyEvent) -> None:
        """Обработка нажатий клавиш, включая Enter, Esc"""

        keys = (self.check_calculation(event), self.check_esc(event))
        if all(keys):
            # Если нажатая не специальная клавиша, передаем событие дальше
            QtWidgets.QTextEdit.keyPressEvent(self.calculator.txtFormula, event)

    def check_calculation(self, event: QtGui.QKeyEvent) -> bool:
        """Обработка нажатия клавиши Enter (вычисления формулы)."""

        keys = (Qt.Key.Key_Return, Qt.Key.Key_Enter, Qt.Key.Key_Equal)

        # Проверяем нажата ли клавиша "Ввод" и, если нажата, производим расчёт
        if event.key() in keys:
            self.calculate_formula()  # Вычисление формулы при нажатии Enter
            return False
        return True

    def check_esc(self, event: QtGui.QKeyEvent) -> bool:
        """Обработка нажатия клавиши Esc для удаления символов из формулы."""

        if event.key() == Qt.Key.Key_Escape:
            self.calculator.clear_formula_result()
            return False
        return True