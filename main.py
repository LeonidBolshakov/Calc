import io
from contextlib import redirect_stderr

from PyQt6 import QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem

# Словарь для замены нестандартных символов на стандартные
REPLACE_SYMBOLS = {",": ".", " ": "", "'": "", "_": "", ":": "/", "\t": ""}
CALC_UI = "calc.ui"  # Имя файла UI для калькулятора
# Набор допустимых символов для формул
SAFE_SYMBOLS = {
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    ".",
    "+",
    "-",
    "*",
    "/",
    "(",
    ")",
}


class NullIO(io.StringIO):
    """Класс для подавления вывода ошибок в консоль."""

    def write(self, *args, **kwargs):
        pass


class CalculatorApp(QtWidgets.QMainWindow):
    """Главный класс приложения калькулятора, наследующий от QMainWindow."""

    # Определение кнопок и текстовых полей
    btnRun: QtWidgets.QPushButton
    btnCopy: QtWidgets.QPushButton
    btnClear: QtWidgets.QPushButton
    btnExit: QtWidgets.QPushButton
    txtFormula: QtWidgets.QTextEdit
    txtResult: QtWidgets.QTextBrowser
    tblResults: QtWidgets.QTableWidget

    def __init__(self) -> None:
        """Инициализация приложения и загрузка UI."""
        super().__init__()

        # Загрузка UI
        uic.loadUi(CALC_UI, self)

        self.setup()  # Настройка элементов интерфейса
        self.setup_connections()  # Установка соединений сигналов и слотов

    def setup(self) -> None:
        """Настройка начальных параметров интерфейса."""
        self.txtFormula.setFocus()  # Установка фокуса на поле ввода формулы
        self.setup_table_results()  # Настройка таблицы результатов
        self.setup_bold()  # Установка жирного шрифта для некоторых элементов

    def setup_table_results(self):
        """Настройка внешнего вида таблицы результатов"""
        self.tblResults.setColumnCount(3)  # Установка количества колонок
        self.tblResults.setColumnWidth(0, 50)  # Ширина колонки с кнопкой
        self.tblResults.setColumnWidth(1, 275)  # Ширина колонки с формулой
        self.tblResults.setColumnWidth(2, 275)  # Ширина колонки с результатом
        self.tblResults.horizontalHeader().setVisible(
            False
        )  # Скрыть горизонтальный заголовок
        self.tblResults.verticalHeader().setVisible(
            False
        )  # Скрыть вертикальный заголовок

    def setup_bold(self):
        """Установка жирного начертания для шрифтов элементов управления."""
        for widget in (self.btnRun, self.btnExit, self.txtFormula, self.txtResult):
            widget.setFont(self.bold_font(widget.font()))  # Установка жирного шрифта

    def setup_connections(self) -> None:
        """Привязка сигналов к методам обработки событий"""

        # Привязка кнопок к соответствующим методам
        self.btnRun.clicked.connect(self.click_button_calc)
        self.btnCopy.clicked.connect(self.click_button_copy)
        self.btnClear.clicked.connect(self.click_button_clear)
        self.btnExit.clicked.connect(QtWidgets.QApplication.quit)
        # Переопределение обработки нажатий клавиш
        self.txtFormula.keyPressEvent = self.handle_key_press  # type: ignore

    @staticmethod
    def bold_font(font: QtGui.QFont) -> QtGui.QFont:
        """Возвращает шрифт с установленным жирным начертанием."""

        font.setBold(True)
        return font

    def handle_key_press(self, event: QtGui.QKeyEvent) -> None:
        """Обработка нажатий клавиш, включая клавишу Enter."""

        self.check_enter(event)  # Проверка нажатия клавиши Enter

    def check_enter(self, event: QtGui.QKeyEvent) -> None:
        """Обработка нажатия клавиши Enter для вычисления формулы."""
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.click_button_calc()  # Вычисление формулы при нажатии Enter
            return

        # Если нажатая клавиша не Enter, передаем событие дальше
        QtWidgets.QTextEdit.keyPressEvent(self.txtFormula, event)

    def click_button_calc(self) -> None:
        """Получение формулы из текстового поля и вычисление результата"""

        formula = self.txtFormula.toPlainText()  # Получение текста формулы
        self.formula_processing(formula)  # Обработка формулы
        self.txtFormula.setFocus()  # Установка фокуса обратно на поле ввода

    def click_button_copy(self) -> None:
        """Копирование результата в буфер обмена"""
        text = self.txtResult.toPlainText()  # Получение текста результата
        clipboard = (
            QtWidgets.QApplication.clipboard()
        )  # Получение доступа к буферу обмена
        clipboard.setText(text)  # type: ignore # Установка текста в буфер обмена
        self.txtFormula.setFocus()  # Установка фокуса обратно на поле ввода

    def click_button_clear(self):
        """Очистка текстового поля формулы."""
        self.txtFormula.clear()  # Очистка поля ввода
        self.txtFormula.setFocus()  # Установка фокуса обратно на поле ввода

    def start(self) -> None:
        """Запуск приложения и отображение главного окна."""
        self.show()  # Показ формы
        QtWidgets.QApplication.exec()  # Запуск основного цикла приложения

    def formula_processing(self, formula: str) -> None:
        """Обработка формулы: стандартизация, проверка и вычисление."""
        formula_st = self.symbol_standardization(formula)  # Стандартизация формулы
        if self.antivirus(formula_st):  # Проверка на допустимые символы
            self.out_result(formula, self.calculation(formula_st))  # Вывод результата
        else:
            self.out_result(formula, "Ошибка. Недопустимый символ")

    def out_result(self, formula: str, result: str) -> None:
        """Вывод результата вычисления в текстовое поле и таблицу результатов."""
        self.out_in_result(result)  # Вывод результата в текстовое поле
        self.out_in_tbl_results(formula, result)  # Вывод формулы и результата в таблицу

    def out_in_tbl_results(self, formula: str, result: str):
        """Добавление новой строки с формулой и результатом в таблицу результатов."""
        new_row = self.tblResults.rowCount()  # Получение текущего количества строк
        self.tblResults.insertRow(new_row)  # Вставка новой строки

        # Добавляем кнопку в новую строку
        self.add_button_in_row(new_row)

        # Добавляем формулу в новую строку
        self.add_item_in_row(new_row, 1, formula, "left")

        # Добавляем результат в новую строку и выравниваем по правому краю.
        self.add_item_in_row(new_row, 2, result, "right")

        # Прокручиваем таблицы до последнего результата
        self.tblResults.scrollToBottom()

    def click_button_C(self, row: int) -> None:
        """Копирование формулы из таблицы результатов в буфер обмена."""
        text = self.tblResults.item(  # type: ignore
            row, 1
        ).text()  # Получение текста формулы из таблицы
        clipboard = (
            QtWidgets.QApplication.clipboard()
        )  # Получение доступа к буферу обмена
        clipboard.setText(text)  # type: ignore # Установка текста в буфер обмена

    def add_item_in_row(self, row: int, column: int, text: str, align: str = "left"):
        """Добавляем элемент в таблицу,
        делаем недоступным для редактирования и выравниваем"""

        item = QTableWidgetItem(text)  # Создание нового элемента таблицы
        # Запрет редактирования
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
        qt_align = (
            Qt.AlignmentFlag.AlignRight
            if align == "right"
            else Qt.AlignmentFlag.AlignLeft
        )  # Установка выравнивания
        item.setTextAlignment(qt_align)  # Применение выравнивания к элементу
        self.tblResults.setItem(row, column, item)  # Добавление элемента в таблицу

    def add_button_in_row(self, row: int) -> None:
        """Создание кнопки в строке таблицы. Для копирования формулы."""

        button = QtWidgets.QPushButton("C")  # Создание кнопки с текстом "C"
        # Привязка события нажатия кнопки к методу копирования формулы
        button.clicked.connect(lambda checked, r=row: self.click_button_C(r))

        # Добавление кнопки в соответствующую таблицы
        self.tblResults.setCellWidget(row, 0, button)

    def out_in_result(self, result: str) -> None:
        """Вывод результата вычисления в текстовое поле результата."""
        self.txtResult.setPlainText(
            result
        )  # Установка текста результата в текстовое поле

    @staticmethod
    def symbol_standardization(formula: str) -> str:
        """Заменяем нестандартные символы стандартными"""
        translation_table = str.maketrans(REPLACE_SYMBOLS)  # Создание таблицы перевода
        return formula.translate(translation_table)  # Применение замены к формуле

    @staticmethod
    def calculation(formula: str) -> str:
        """Вычисление результата формулы с обработкой ошибок."""
        try:
            with redirect_stderr(NullIO()):  # Подавление вывода ошибок на консоль
                return str(eval(formula))  # Вычисление формулы
        except ZeroDivisionError:
            return "Ошибка. Деление на 0"  # Обработка деления на ноль
        except Exception:
            return "Ошибка"  # Обработка других ошибок

    @staticmethod
    def antivirus(formula: str) -> bool:
        """Проверка формулы на наличие только допустимых символов.
        Защищает программу от ввода вредоносного текста"""

        return all(
            c in SAFE_SYMBOLS for c in formula
        )  # Возвращает True, если все символы допустимы


# Запуск приложения
if __name__ == "__main__":
    app = QtWidgets.QApplication([])  # Создание экземпляра приложения
    calc_app = CalculatorApp()  # Создание экземпляра калькулятора
    calc_app.start()  # Запуск калькулятора
