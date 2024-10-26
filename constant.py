from dataclasses import dataclass


@dataclass(frozen=True)
class Const:
    FILE_NAME = "results.csv"  # Имя файла с историй формул и результатов
    CALC_UI = "calc.ui"  # Имя файла UI для калькулятора
    # Словарь для замены нестандартных символов на стандартные
    REPLACE_SYMBOLS = {
        ",": ".",
        " ": "",
        "'": "",
        "_": "",
        ":": "/",
        "\t": "",
        "^": "**",
    }
    # Набор допустимых символов для формул
    SAFE_SYMBOLS = "0123456789.+-*/()%"
    TEXT_BUTTON_COPY = "C"
    DIRECTION_RIGHT = "right"
    DIRECTION_LEFT = "left"
    TEXT_DEVISE_0 = "Ошибка. Деление на 0"
    TEXT_SYNTAX_ERROR = "Ошибка синтаксиса"
    HEAD_CSV_FILE = ("Выражение", "Результат")
    TEXT_ERROR_WRITE = "Не удалось записать историю вычислений в файл:"
    TEXT_ERROR_READ = "Не удалось обработать файл с историей результатов:"
    TEXT_TITLE_ERROR = "Ошибка"
    WIDTH_COLUMN_BUTTON = 50
    WIDTH_COLUMN_FORMULA = 275
    WIDTH_COLUMN_RESULT = 275
    TEXT_ERROR_SYMBOL = "Ошибка. Недопустимый символ"
