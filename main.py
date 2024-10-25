import csv
import io
from contextlib import redirect_stderr

from PyQt6 import QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem

FILE_NAME = "results.csv"  # Имя файла с историй формул и результатов
CALC_UI = "calc.ui"  # Имя файла UI для калькулятора
# Словарь для замены нестандартных символов на стандартные
REPLACE_SYMBOLS = {",": ".", " ": "", "'": "", "_": "", ":": "/", "\t": "", "^": "**"}
# Набор допустимых символов для формул
SAFE_SYMBOLS = "0123456789.+-*/()%"


class NullIO(io.StringIO):
    """Класс для подавления вывода ошибок в консоль."""

    def write(self, *args, **kwargs):
        pass


class CalculatorApp(QtWidgets.QMainWindow):
    """Главный класс приложения калькулятора, наследующий от QMainWindow."""

    # Определение кнопок и текстовых полей
    btnCopy: QtWidgets.QPushButton
    btnClear: QtWidgets.QPushButton
    btnExit: QtWidgets.QPushButton
    btnRun: QtWidgets.QPushButton
    lblInf2: QtWidgets.QLabel
    tblResults: QtWidgets.QTableWidget
    txtFormula: QtWidgets.QTextEdit
    txtResult: QtWidgets.QTextBrowser

    def __init__(self) -> None:
        """Инициализация приложения и загрузка UI."""
        super().__init__()

        # Загрузка UI
        uic.loadUi(CALC_UI, self)

        self.setup()  # Настройка элементов интерфейса
        self.setup_connections()  # Установка соединений сигналов и слотов

    def closeEvent(self, event):
        """Переопределение метода выхода из программы"""
        self.write_history()
        event.accept()

    def setup(self) -> None:
        """Настройка начальных параметров интерфейса."""
        self.txtFormula.setFocus()  # Установка фокуса на поле ввода формулы
        self.setup_table_results()  # Настройка таблицы результатов
        self.init_table_results()  # Инициализация таблицы результатов
        self.setup_info()  # Настройка информационной части окна
        self.setup_bold()  # Установка жирного шрифта для некоторых элементов

    def setup_table_results(self):
        """Настройка внешнего вида таблицы результатов"""

        self.setup_tbl_columns()

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
        """Привязка сигналов к методам обработки событий,
        кроме кнопок копирования строк таблицы результатов"""

        # Привязка кнопок к соответствующим методам
        self.btnRun.clicked.connect(self.calculate_formula)
        self.btnCopy.clicked.connect(self.copy_result_clipboard)
        self.btnClear.clicked.connect(self.clear_all)
        self.btnExit.clicked.connect(QtWidgets.QApplication.quit)
        # Переопределение обработки нажатий клавиш
        self.txtFormula.keyPressEvent = self.handle_key_press  # type: ignore

    @staticmethod
    def bold_font(font: QtGui.QFont) -> QtGui.QFont:
        """Возвращает шрифт с установленным жирным начертанием."""

        font.setBold(True)
        return font

    def handle_key_press(self, event: QtGui.QKeyEvent) -> None:
        """Обработка нажатий клавиш, включая клавиши Enter, Esc"""

        if all([self.check_enter(event), self.check_esc(event)]):
            # Если нажатая клавиша не специальная, передаем событие дальше
            QtWidgets.QTextEdit.keyPressEvent(self.txtFormula, event)

    def check_enter(self, event: QtGui.QKeyEvent) -> bool:
        """Обработка нажатия клавиши Enter для вычисления формулы."""

        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.calculate_formula()  # Вычисление формулы при нажатии Enter
            return False
        return True

    def check_esc(self, event: QtGui.QKeyEvent) -> bool:
        """Обработка нажатия клавиши Esc для удаления символов из формулы."""

        if event.key() == Qt.Key.Key_Escape:
            self.clear_formula_result()
            return False
        return True

    def calculate_formula(self) -> None:
        """Получение формулы из текстового поля и вычисление результата"""

        formula = self.txtFormula.toPlainText()  # Получение текста формулы
        self.formula_processing(formula)  # Обработка формулы
        self.txtFormula.setFocus()  # Установка фокуса обратно на поле ввода

    def copy_result_clipboard(self) -> None:
        """Копирование результата в буфер обмена"""

        text = self.txtResult.toPlainText()  # Получение текста результата
        clipboard = (
            QtWidgets.QApplication.clipboard()
        )  # Получение доступа к буферу обмена
        clipboard.setText(text)  # type: ignore # Установка текста в буфер обмена
        self.txtFormula.setFocus()  # Установка фокуса обратно на поле ввода

    def clear_all(self):
        """Очистка екстового поля формулы и поля результата и истории результатов"""

        self.clear_formula_result()
        self.tblResults.setRowCount(0)  # Очищаем историю
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

        self.add_button_in_row(new_row)  # Добавляем кнопку в новую строку
        self.add_item_in_row(new_row, 1, formula)  # Добавляем формулу в новую строку
        # Добавляем результат в новую строку и выравниваем по правому краю.
        self.add_item_in_row(new_row, 2, result, "right")
        self.tblResults.scrollToBottom()  # Прокручиваем таблицы к последней строке

    def copy_history_clipboard(self, row: int) -> None:
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
        )  # Установка выравнивания в зависимости от параметра
        item.setTextAlignment(qt_align)  # Применение выравнивания к элементу

        # Добавление элемента в таблицу
        self.tblResults.setItem(row, column, item)

    def add_button_in_row(self, row: int) -> None:
        """Создание кнопки в строке таблицы. Для копирования формулы."""

        button = QtWidgets.QPushButton("C")  # Создание кнопки с текстом "C"

        # Привязка события нажатия кнопки к методу копирования формулы
        button.clicked.connect(lambda checked, r=row: self.copy_history_clipboard(r))

        # Добавление кнопки в соответствующую строку таблицы
        self.tblResults.setCellWidget(row, 0, button)

    def out_in_result(self, result: str) -> None:
        """Вывод результата вычисления в текстовое поле результата."""

        # Установка текста результата в текстовое поле
        self.txtResult.setPlainText(result)

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
                return str(eval(formula))  # Вычисление по формуле
        except ZeroDivisionError:
            return "Ошибка. Деление на 0"  # Обработка деления на ноль
        except Exception:
            return "Ошибка синтаксиса"  # Обработка других ошибок

    @staticmethod
    def antivirus(formula: str) -> bool:
        """Проверка формулы на наличие только допустимых символов.
        Защищает программу от ввода вредоносного кода"""

        return all(
            c in SAFE_SYMBOLS for c in formula
        )  # Возвращает True, если все символы допустимы

    def write_history(self):
        """Записывает историю вычислений и результатов в csv файл"""

        results = self.read_from_tblResults()

        # Запись данных в CSV файл
        try:
            with open(FILE_NAME, mode="w", newline="", encoding="utf-8-sig") as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(("Выражение", "Результат"))
                writer.writerows(results)
        except Exception as e:
            self.show_error_message(
                f"Не удалось записать историю вычислений в файл: \n {e}"
            )

    def init_table_results(self):
        """Историю из csv файла переписываем в таблицу результатов"""

        try:
            with open(FILE_NAME, mode="r", encoding="utf-8-sig") as file:
                reader = csv.reader(file, delimiter=";")
                next(reader)
                for row, rec in enumerate(reader):
                    self.out_in_tbl_results(formula=rec[0], result=rec[1])
        except FileNotFoundError:
            pass
        except Exception as e:
            self.show_error_message(
                f"Не удалось обработать файл с историей результатов:\n{e}"
            )

    def setup_info(self):
        """В строки информации проставляем имя файла вывода"""
        self.lblInf2.setText(self.lblInf2.text().replace("#", FILE_NAME))

    def show_error_message(self, message: str):
        """Выводим сообщение об ошибке"""
        QMessageBox.critical(self, "Ошибка", message)

    def clear_formula_result(self):
        """Очищаем текстовые поля ввода формулы и вывода результата"""

        self.txtFormula.clear()  # Очищаем поле формулы
        self.txtResult.clear()  # Очищаем поле результата

    def setup_tbl_columns(self):
        self.tblResults.setColumnCount(3)  # Установка количества колонок
        self.tblResults.setColumnWidth(0, 50)  # Ширина колонки с кнопкой
        self.tblResults.setColumnWidth(1, 275)  # Ширина колонки с формулой
        self.tblResults.setColumnWidth(2, 275)  # Ширина колонки с результатом

    def read_from_tblResults(self) -> list[tuple]:
        """Чтение данных из таблицы результатов"""

        total = self.tblResults.rowCount()  # Количество строк в таблице результатов
        return [
            (self.tblResults.item(row, 1).text(), self.tblResults.item(row, 2).text())
            for row in range(total)
        ]  # Передача пар (Формула, Результат)


# Запуск приложения
if __name__ == "__main__":
    app = QtWidgets.QApplication([])  # Создание экземпляра приложения
    calc_app = CalculatorApp()  # Создание экземпляра калькулятора
    calc_app.start()  # Запуск калькулятора
