from constant import Const
from contextlib import redirect_stderr
import io

from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt


class NullIO(io.StringIO):
    """Класс для подавления вывода ошибок в консоль."""

    def write(self, *args, **kwargs):
        pass


class F:
    def __init__(self, calculator_app):
        self.calculator_app = calculator_app

    def formula_processing(self) -> None:
        """Получение формулы из текстового поля и её обработка"""

        formula = (
            self.calculator_app.txtFormula.toPlainText()
        )  # Получение текста формулы
        formula_standard = self.symbol_standardization(
            formula
        )  # Стандартизация формулы

        if self.antivirus(formula_standard):  # Проверка на допустимые символы
            self.calculator_app.out_result(
                formula, self.calculation(formula_standard)  # вычисление
            )  # Вывод результата
        else:
            self.calculator_app.out_result(formula, Const.TEXT_ERROR_SYMBOL)

        self.calculator_app.txtFormula.setFocus()  # Установка фокуса на поле ввода

    @staticmethod
    def symbol_standardization(formula: str) -> str:
        """Заменяем нестандартные символы стандартными"""

        # Создание таблицы перевода
        translation_table = str.maketrans(Const.REPLACE_SYMBOLS)

        return formula.translate(translation_table)  # Замена символов в формуле

    # noinspection PyBroadException
    @staticmethod
    def calculation(formula: str) -> str:
        """Вычисление результата формулы и обработка ошибок."""
        try:
            with redirect_stderr(NullIO()):  # Подавление вывода ошибок на консоль
                return str(eval(formula))  # Результат вычисления
        except ZeroDivisionError:
            return Const.TEXT_DEVISE_0  # Сообщение о делении на 0
        except Exception:
            return Const.TEXT_SYNTAX_ERROR  # Сообщение о синтаксической ошибке

    @staticmethod
    def antivirus(formula: str) -> bool:
        """Проверка формулы на наличие только допустимых символов.
        Защищает программу от ввода вредоносного кода."""

        return all(
            char in Const.SAFE_SYMBOLS for char in formula
        )  # Возвращает True, если все символы допустимы

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
