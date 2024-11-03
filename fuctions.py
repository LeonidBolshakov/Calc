from contextlib import redirect_stderr
import io
import re
import math

from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl
from PyQt6 import QtGui
from PyQt6.QtCore import QMimeData

from constants import Const


class NullIO(io.StringIO):
    """Класс для подавления вывода ошибок в консоль."""

    def write(self, *args, **kwargs):
        pass


def bold_font(font: QtGui.QFont) -> QtGui.QFont:
    """Возвращает шрифт с установленным жирным начертанием."""

    font.setBold(True)
    return font


def open_help():
    """Вызов Help файла"""

    help_file_path = Const.FILE_HELP
    QDesktopServices.openUrl(QUrl.fromLocalFile(help_file_path))


def symbol_standardization(formula: str) -> str:
    """Заменяет нестандартные символы стандартными"""

    # Создание таблицы перевода
    translation_table = str.maketrans(Const.REPLACE_SYMBOLS)

    return formula.translate(translation_table)  # Замена символов в формуле


def calculation(formula: str) -> str:
    """Вычисление результата формулы и обработка ошибок."""

    formula = math_formula(formula)  # Приводим формулу к math виду

    # noinspection PyBroadException
    try:
        with redirect_stderr(NullIO()):  # Подавление вывода ошибок на консоль
            return str(eval(formula))  # Результат вычисления
    except ZeroDivisionError:
        return Const.TEXT_DEVISE_0  # Сообщение о делении на 0
    except Exception:
        return Const.TEXT_SYNTAX_ERROR  # Сообщение о синтаксической ошибке


def no_virus(formula: str) -> re.Match | None:
    """Проверка формулы на наличие только допустимого текста.

    Защищает программу от ввода вредоносного кода."""
    pattern = get_pattern() + "*"
    return re.fullmatch(pattern, formula)  # Возвращает True, если все символы допустимы


# @cache
def get_pattern() -> str:
    """Формирует шаблон контроля формулы регулярными выражениями"""

    # шаблон надо формировать только 1 раз еа цикл выполнения программы
    if hasattr(get_pattern, "result"):
        return get_pattern.result
    else:
        pattern_s = "|".join(do_pattern_escape(Const.SAFE_SYMBOLS))
        pattern_f = "|".join(Const.SAFE_FORMULAS)
        get_pattern.result = "(" + pattern_s + "|" + pattern_f + ")"
        return get_pattern.result


def remove_extra_characters(pattern: str, formula: str) -> str:
    """Оставляет в строке только символы и имена формул, входящие в состав безопасных"""

    result = []
    for match in re.findall(pattern, formula):
        result.append(match)
    return "".join(result)


def do_pattern_escape(pattern: str) -> list[str]:
    result = []
    for char in pattern:
        if char in Const.SPECIAL_TEMPLATE_CHARACTERS:
            result.append("\\" + char)
        else:
            result.append(char)

    return result


def only_safe_symbols(source: QMimeData) -> QMimeData:
    """Убирает из текста контейнера не безопасные символы"""

    # заменяем символы синонимы на стандартные (':' на '/').
    text_standard = symbol_standardization(source.text())

    # Убираем лишние символы и корректируем контейнер для данных
    text_safe = remove_extra_characters(get_pattern(), text_standard)
    new_source = QMimeData()
    new_source.setText(text_safe)

    return new_source


def math_formula(formula):
    """Заменяет вызовы функций. К имени функции добавляется текст 'math.'"""

    if hasattr(math_formula, "pattern"):
        pattern = math_formula.pattern
    else:
        # Создаёт регулярное выражение для поиска всех имён функций.
        pattern = re.compile("|".join(re.escape(key) for key in Const.SAFE_FORMULAS))
        math_formula.pattern = pattern

    # Выполняет замену -> К имени функции слева добавляем 'math.'
    return pattern.sub(replacement, formula)


def replacement(match: re.Match):
    """Функция замены, которая будет использоваться в pattern.sub"""

    return "math." + match.group(0)
