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

    help_file_path = Const.HELP_FILE_NAME
    QDesktopServices.openUrl(QUrl.fromLocalFile(help_file_path))


def normalize_characters(formula: str) -> str:
    """Заменяет нестандартные символы стандартными"""

    # Создание таблицы перевода
    translation_table = str.maketrans(Const.REPLACEMENT_DICTIONARY)

    return formula.translate(translation_table)  # Замена символов в формуле


def calculate_and_validate_formula(formula: str) -> str:
    """Вычисление результата формулы и обработка ошибок."""

    formula = add_math_prefix_to_function_calls(formula)  # Приводим формулу к math виду

    # noinspection PyBroadException
    try:
        with redirect_stderr(NullIO()):  # Подавление вывода ошибок на консоль
            return str(eval(formula))  # Результат вычисления
    except ZeroDivisionError:
        return Const.ERROR_DIVIDE_BY_ZERO  # Сообщение о делении на 0
    except Exception:
        return Const.ERROR_SYNTAX  # Сообщение о синтаксической ошибке


def no_virus(formula: str) -> re.Match | None:
    """Проверка формулы на наличие только допустимого текста.

    Защищает программу от ввода вредоносного кода."""
    pattern = create_formula_validation_pattern() + "*"
    return re.fullmatch(pattern, formula)  # Возвращает True, если все символы допустимы


# @cache - ошибки при выполнении. Замена ручным кодом.
def create_formula_validation_pattern() -> str:
    """Формирует шаблон контроля формулы регулярными выражениями"""

    # шаблон надо формировать только 1 раз еа цикл выполнения программы
    if hasattr(create_formula_validation_pattern, "result"):
        return create_formula_validation_pattern.result
    else:
        pattern_s = "|".join(add_escape_to_special_symbols(Const.VALID_CHAR_SET))
        pattern_f = "|".join(Const.FORMULA_VALIDATION_LIST)
        create_formula_validation_pattern.result = (
            "(" + pattern_s + "|" + pattern_f + ")"
        )
        return create_formula_validation_pattern.result


def remove_unsafe_characters_from_string(pattern: str, formula: str) -> str:
    """Оставляет в строке только символы и имена формул, входящие в состав безопасных"""

    result = []
    for match in re.findall(pattern, formula):
        result.append(match)
    return "".join(result)


def add_escape_to_special_symbols(pattern: str) -> list[str]:
    """К специальным символам в образе шаблона добавляет '\'"""

    result = []
    for char in pattern:
        if char in Const.SPECIAL_REGEX_SYMBOLS:
            result.append("\\" + char)
        else:
            result.append(char)

    return result


def filter_out_unsafe_symbols(source: QMimeData) -> QMimeData:
    """Убирает из текста контейнера не безопасные символы"""

    # заменяем символы синонимы на стандартные (':' на '/').
    text_standard = normalize_characters(source.text())

    # Убираем лишние символы и корректируем контейнер для данных
    text_safe = remove_unsafe_characters_from_string(
        create_formula_validation_pattern(), text_standard
    )
    new_source = QMimeData()
    new_source.setText(text_safe)

    return new_source


def add_math_prefix_to_function_calls(formula):
    """Заменяет в формуле вызовы функций. К имени функции добавляется текст 'math.'"""

    if hasattr(add_math_prefix_to_function_calls, "pattern"):
        pattern = add_math_prefix_to_function_calls.pattern
    else:
        # Создаёт регулярное выражение для поиска всех имён функций.
        pattern = re.compile(
            "|".join(re.escape(key) for key in Const.FORMULA_VALIDATION_LIST)
        )
        add_math_prefix_to_function_calls.pattern = pattern

    # К имени функции слева добавляем 'math.'
    return pattern.sub(replacement_function, formula)


def replacement_function(match: re.Match):
    """Функция замены, которая будет использоваться в pattern.sub"""

    return "math." + match.group(0)
