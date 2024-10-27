from dataclasses import dataclass


@dataclass(frozen=True)
class Const:
    FILE_NAME = "results.csv"  # Имя файла с историй формул и результатов
    CALC_UI = "calc.ui"  # Имя файла UI для калькулятора
    # Словарь для замены нестандартных символов на стандартные
    REPLACE_SYMBOLS = {
        "," : ".",
        " " : "",
        "'" : "",
        "_" : "",
        ":" : "/",
        "\t": "",
        "^" : "**",
    }
    # Набор допустимых символов для формул
    SAFE_SYMBOLS = "0123456789.+-*/()%"
    TEXT_BUTTON_COPY = "C"
    DIRECTION_RIGHT = "right"
    DIRECTION_LEFT = "left"
    TEXT_DEVISE_0 = "Ошибка. Деление на 0"
    TEXT_SYNTAX_ERROR = "Ошибка синтаксиса"
    HEAD_CSV_FILE = ("Выражение", "Результат")
    TEXT_ERROR_WRITE = "Не удалось записать историю вычислений в файл\n:"
    TEXT_ERROR_READ = (
        "Файл с историй вычислений существует, но испорчен или недоступен. \n"
        "Прежняя история вычислений не используется:"
    )
    TEXT_TITLE_ERROR = "Ошибка"
    WIDTH_COLUMN_BUTTON = 50
    WIDTH_COLUMN_FORMULA = 275
    WIDTH_COLUMN_RESULT = 275
    TEXT_ERROR_SYMBOL = "Ошибка. Недопустимый символ"
    DELIMITER = ";"
    DIALOG_AGREE = "&Согласен"
    DIALOG_REJECTION = "&Отказываюсь"
    DIALOG_TITLE = "Предупреждение"
    DIALOG_ASK = (
        "Сейчас будет удалена вся ранее накопленная история вычислений.\n"
        "Вы с этим согласны?"
    )
