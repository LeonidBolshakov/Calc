from dataclasses import dataclass


@dataclass(frozen=True)
class Const:
    CALC_UI = "calc.ui"  # Имя файла UI для калькулятора
    DELIMITER = ";"
    DIALOG_AGREE = "&Согласен"
    DIALOG_REJECTION = "&Отказываюсь"
    DIALOG_TITLE = "Удаление"
    DIALOG_ASK = (
        "Сейчас навсегда будет удалена\n"
        "вся ранее накопленная история вычислений.\n"
        "Вы с этим согласны?"
    )
    DIRECTION_LEFT = "left"
    DIRECTION_RIGHT = "right"
    FILE_HELP = "help.mht"
    FILE_HISTORY = "results.csv"  # Имя файла с историей формул и результатов
    HEAD_CSV_FILE = ("Выражение", "Результат")
    # Словарь для замены нестандартных символов на стандартные
    REPLACE_SYMBOLS = {
        ",": ".",
        " ": "",
        "'": "",
        "_": "",
        ":": "/",
        "\t": "",
        "^": "**",
        "x": "*",
        "х": "*",
    }
    # Набор допустимых символов для формул
    SAFE_SYMBOLS = "0123456789.+-*/()%"
    SIZE_WINDOW_HELP = (800, 600)
    TEXT_BUTTON_COPY = "C"
    TEXT_DEVISE_0 = "Ошибка. Деление на 0"
    TEXT_ERROR_READ = (
        "Файл с историй вычислений существует, но испорчен или недоступен. \n"
        "Прежняя история вычислений не используется:"
    )
    TEXT_ERROR_SYMBOL = "Ошибка. Недопустимый символ"
    TEXT_ERROR_WRITE = "Не удалось записать историю вычислений в файл\n:"
    TEXT_SYNTAX_ERROR = "Ошибка синтаксиса"
    TEXT_TITLE_ERROR = "Ошибка"
    TEXT_TITLE_HELP = "Справка"
    WIDTH_COLUMN_BUTTON = 50
    WIDTH_COLUMN_FORMULA = 275
    WIDTH_COLUMN_RESULT = 275
