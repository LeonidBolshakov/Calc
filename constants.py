from dataclasses import dataclass

from PyQt6.QtGui import QColor


@dataclass(frozen=True)
class Const:
    ALIGN_LEFT = "left"  # Выравнивание — налево
    ALIGN_RIGHT = "right"  # Выравнивание направо
    BUTTON_TEXT_COPY_LINE = "C"  # Текст кнопки "Копирование строки"
    COLUMN_WIDTH_BUTTON = 50  # Ширина колонки с кнопкой
    CSV_HEADERS = ("Выражение", "Результат")  # Заголовки столбцов CSV файла
    DECIMAL_PLACE_RANGE = (0, 9)  # Диапазон числа знаков для округления
    DEFAULT_DECIMAL_PLACES = 2  # Число знаков для округления по умолчанию
    DIALOG_ACCEPT = "&Согласен"  # Текст кнопки в диалоговом окне — Принять
    DIALOG_REJECTION = "&Отказываюсь"  # Текст кнопки в диалоговом окне — Отказаться
    DIALOG_TITLE = "Удаление"  # Заголовок диалогового окна
    DIALOG_ASK = (
        "Сейчас навсегда будет удалена\n"
        "вся ранее накопленная история вычислений.\n"
        "Вы с этим согласны?"
    )  # Вопрос в диалоговом окне
    ERROR_DIVIDE_BY_ZERO = "Ошибка. Деление на 0"  # Текст ошибки "Деление на 0"
    # текст ошибки при вводе недопустимого символа
    ERROR_INVALID_SYMBOL = "Ошибка. Недопустимый символ"
    ERROR_SYNTAX = "Ошибка синтаксиса"
    ERROR_MESSAGE_TITLE = "Ошибка"  # Заголовок окна с сообщением об ошибке
    FAILED_TO_WRITE_HISTORY_TEXT = "Не удалось записать историю вычислений в файл\n:"
    EXCEL_LIST_SEPARATOR = ";"  # Разделитель элементов списка для MS EXCEL
    # Набор допустимых формул
    FORMULA_VALIDATION_LIST = {
        "sqrt",
        "degrees",
        "radians",
        "cos",
        "sin",
        "tan",
        "acos",
        "asin",
        "atan",
        "log10",
        "abs",
        "pi",
        "e",
    }
    HELP_FILE_NAME = "Help.mht"  # Имя файла с Help
    HELP_WINDOW_SIZE = (800, 600)  # Размеры окна помощи
    HISTORY_FILE_NAME = "results.csv"  # Имя файла с историей формул и результатов
    HISTORY_READ_ERROR = (
        "Файл с историй вычислений существует, но испорчен или недоступен. \n"
        "Прежняя история вычислений не используется:"
    )  # Текст при ошибке чтения файла истории
    PLACEHOLDER_RESULT = "Здесь будет результат вычисления"
    # Словарь для замены нестандартных символов на стандартные
    REPLACEMENT_DICTIONARY = {
        ",": ".",
        " ": "",
        "'": "",
        "’": "",
        "_": "",
        ":": "/",
        "\t": "",
        "\n": "",
        "^": "**",
        "x": "*",
        "х": "*",
        "–": "-",  # Широкий дефис меняется на знак "-"
    }
    # Специальные символы шаблона регулярных выражений
    SPECIAL_REGEX_SYMBOLS = r".^$*+?{}[]\|()"
    UI_CONFIG_REL_PATH = "_internal\\Calc.ui"  # Путь к файлу UI калькулятора
    VALID_CHAR_SET = "0123456789.+-*/()"  # Набор допустимых символов
