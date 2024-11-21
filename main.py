""" Приложение Калькулятор — позволяет вводить формулу и производить по ней вычисления.
     В формуле можно использовать числа, скобки и арифметические действия.
     Формулы можно копировать в буфер обмена.
     При вводе из буфера обмена вся
     ненужная информация в формулу не записывается.
     Программа ведёт и записывает на диск историю расчётов.
     Историю можно просматривать в программе MS EXCEL и как текст."""

import csv
import sys
from pathlib import Path

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QMainWindow

from customtextedit import CustomTextEdit
from constants import Const
from formulas import F
from message import ask_for_continuation, show_error_message
from functions import bold_font, open_help


class CalculatorApp(QMainWindow):
    """Главный класс приложения калькулятора, наследующий от QMainWindow."""

    # Определение кнопок и текстовых полей формы
    btnClear: QtWidgets.QPushButton
    btnCopy: QtWidgets.QPushButton
    btnExit: QtWidgets.QPushButton
    btnHelp: QtWidgets.QPushButton
    btnRound: QtWidgets.QPushButton
    btnRun: QtWidgets.QPushButton
    lblInf2: QtWidgets.QLabel
    lineRoundDigit: QtWidgets.QLineEdit
    txtFormula: CustomTextEdit
    txtResult: QtWidgets.QTextBrowser
    tblResults: QtWidgets.QTableWidget

    # Определение метода класса
    f: F

    def __init__(self) -> None:
        """Инициализация приложения"""
        super().__init__()

        self.init_vars()  # Инициализация атрибутов класса
        self.setup_interface()  # Настройка элементов интерфейса
        self.setup_connections()  # Установка соединений сигналов и слотов

    def init_vars(self):
        """Присвоение значений переменным"""

        self.f = F(self)  # Методы работы с формулой

        # Загрузка UI и переменных в объект класса
        exe_directory = (  # Директория, из которой был запущен файл
            Path(sys.argv[0]).parent
            if hasattr(sys, "frozen")  # exe файл, получен с помощью PyInstaller
            else Path(__file__).parent  # Если файл запущен как обычный Python-скрипт
        )

        ui_config_abs_path = exe_directory / Const.UI_CONFIG_REL_PATH
        uic.loadUi(ui_config_abs_path, self)

    def setup_interface(self) -> None:
        """Настройка начальных параметров интерфейса."""

        self.txtFormula.setFocus()  # Установка фокуса на поле ввода формулы
        # установка текста подсказки в поля вводу формулы и вывода результата
        self.txtResult.setPlaceholderText(Const.PLACEHOLDER_RESULT)
        self.f.set_decimal_places_input()  # Настройка поля ввода числа знаков округления
        self.customize_results_table()  # Настройка таблицы результатов
        self.import_history_from_csv()  # Инициализация таблицы результатов
        self.set_output_filename_label()  # Установка имени файла в метку формы
        self.setup_bold()  # Установка жирного шрифта для некоторых элементов

    # noinspection PyUnresolvedReferences
    def setup_connections(self) -> None:
        """Привязка сигналов к слотам"""

        # Привязка статичных кнопок к слотам
        self.btnClear.clicked.connect(self.clear_all_fields)
        self.btnCopy.clicked.connect(self.copy_result_to_clipboard)
        self.btnExit.clicked.connect(QtWidgets.QApplication.quit)
        self.btnHelp.clicked.connect(open_help)
        self.btnRound.clicked.connect(self.f.round_result)
        self.btnRun.clicked.connect(self.f.formula_processing)

        # Переопределение обработки нажатий клавиш при вводе формулы
        self.txtFormula.keyPressEvent = self.f.handle_key_press  # type: ignore

    def customize_results_table(self):
        """Настройка внешнего вида таблицы результатов"""

        self.customize_results_columns()  # Настройка колонок таблицы результатов

        self.tblResults.horizontalHeader().setVisible(
            False
        )  # Скрыть горизонтальный заголовок
        self.tblResults.verticalHeader().setVisible(
            False
        )  # Скрыть вертикальный заголовок

    def import_history_from_csv(self):
        """Историю из csv файла переписываем в таблицу результатов"""

        try:
            with open(Const.HISTORY_FILE_NAME, mode="r", encoding="utf-8-sig") as file:
                reader = csv.reader(file, delimiter=Const.EXCEL_LIST_SEPARATOR)
                next(reader)  # Пропускаем шапку файла
                # Построчно записываем данные файла в таблицу истории результатов
                for row_data in reader:
                    self.move_row_in_results(formula=row_data[0], result=row_data[1])
        except FileNotFoundError:
            pass  # отсутствие файла не ошибка — начинаем историю с чистого листа
        except Exception as e:
            # При ошибке чтении файла — выдаём сообщение Пользователю
            show_error_message(self, f"{Const.HISTORY_READ_ERROR} \n{e}")

    def set_output_filename_label(self):
        """В строку информации проставляем имя файла вывода"""

        self.lblInf2.setText(self.lblInf2.text().replace("#", Const.HISTORY_FILE_NAME))

    def setup_bold(self):
        """Установка жирного начертания для шрифтов элементов управления."""
        widgets = (self.btnRun, self.btnExit, self.txtFormula, self.txtResult)
        for widget in widgets:
            widget.setFont(bold_font(widget.font()))  # Установка жирного шрифта

    def clear_all_fields(self):
        """Очистка формулы, поля результата и истории"""

        self.clear_formula_and_result()
        if ask_for_continuation(Const.DIALOG_ASK):
            self.clear_table_results()
        self.txtFormula.setFocus()  # Установка фокуса обратно на поле ввода

    def copy_result_to_clipboard(self) -> None:
        """Копирование результата вычислений в буфер обмена"""

        text = self.txtResult.toPlainText()  # Получение текста результата вычислений
        clipboard = (
            QtWidgets.QApplication.clipboard()
        )  # Получение доступа к буферу обмена
        clipboard.setText(text)  # Запись текста в буфер обмена
        self.txtFormula.setFocus()  # Установка фокуса на поле ввода

    def customize_results_columns(self):
        """Настраиваем ширину колонок таблицы результатов"""

        self.tblResults.setColumnCount(3)  # Установка количества колонок
        self.tblResults.setColumnWidth(0, Const.COLUMN_WIDTH_BUTTON)
        table_widget_width = self.tblResults.width()
        table_width = table_widget_width - self.tblResults.verticalScrollBar().width()
        column_width = int((table_width - Const.COLUMN_WIDTH_BUTTON) / 2)
        self.tblResults.setColumnWidth(1, column_width)
        self.tblResults.setColumnWidth(2, column_width)

    def clear_formula_and_result(self):
        """Очищаем поля ввода формулы и вывода результата"""

        self.txtFormula.clear()  # Очищаем поле формулы
        self.txtResult.clear()  # Очищаем поле результата

    def output_result_to_text_field_and_history(
        self, formula: str, result: str
    ) -> None:
        """Вывод результата вычисления в текстовое поле и таблицу истории."""

        self.output_result_to_result_field(result)  # Вывод результата в текстовое поле
        self.insert_new_row_in_results(
            formula, result
        )  # Вывод формулы и результата в таблицу

    def output_result_to_result_field(self, result: str) -> None:
        """Вывод результата вычисления в поле 'Результат'"""

        self.txtResult.setPlainText(result)

    def insert_new_row_in_results(self, formula: str, result: str):
        """В таблицу результатов добавляем новую строку.
        Строку записываем в начало таблицы."""

        table_row = self.get_history_table_data()  # Считываем таблицу истории
        self.clear_table_results()

        self.move_row_in_results(formula, result)
        for row in table_row:
            self.move_row_in_results(row[0], row[1])

    def clear_table_results(self):
        """Очищаем таблицу истории"""

        self.tblResults.setRowCount(0)  # Удаляем строки

    def move_row_in_results(self, formula: str, result: str):
        """Добавление новой строки с формулой и результатом в таблицу истории."""

        # Новую строку вставляем в конец таблицы
        new_row = self.tblResults.rowCount()
        self.tblResults.insertRow(new_row)  # Вставка новой строки

        self.create_copy_button_in_row(new_row)  # Добавляем кнопку в новую строку
        self.add_and_lock_element_to_table(
            new_row, 1, formula
        )  # Добавляем формулу в новую строку
        # Добавляем результат в новую строку и выравниваем по правому краю.
        self.add_and_lock_element_to_table(new_row, 2, result, Const.ALIGN_RIGHT)

    # noinspection PyUnresolvedReferences
    def create_copy_button_in_row(self, row: int) -> None:
        """Создание кнопки в строке таблицы. Кнопка нужна для копирования формулы."""

        # Создание кнопки с текстом "C"
        button = QtWidgets.QPushButton(Const.BUTTON_TEXT_COPY_LINE)

        # Привязка метода к событию нажатия кнопки
        button.clicked.connect(
            lambda checked, r=row: self.copy_history_formula_to_clipboard(r)
        )

        # Добавление кнопки в соответствующую строку таблицы
        self.tblResults.setCellWidget(row, 0, button)

    def add_and_lock_element_to_table(
        self, row: int, column: int, text: str, align: str = Const.ALIGN_LEFT
    ):
        """Добавляем элемент в таблицу,
        делаем его недоступным для редактирования и выравниваем."""

        element = QTableWidgetItem(text)  # Создание нового элемента таблицы

        # Запрет редактирования
        element.setFlags(element.flags() & ~Qt.ItemFlag.ItemIsEditable)

        # Установка выравнивания текста
        qt_align = (
            Qt.AlignmentFlag.AlignRight
            if align == Const.ALIGN_RIGHT
            else Qt.AlignmentFlag.AlignLeft
        )  # Установка выравнивания в зависимости от параметра
        element.setTextAlignment(qt_align)  # Применение выравнивания к элементу

        # Добавление элемента в таблицу
        self.tblResults.setItem(row, column, element)

    def copy_history_formula_to_clipboard(self, row: int) -> None:
        """Копирование формулы из таблицы результатов в буфер обмена."""

        text = self.tblResults.item(  # type: ignore
            row, 1
        ).text()  # Получение текста формулы из таблицы
        clipboard = (
            QtWidgets.QApplication.clipboard()
        )  # Получение доступа к буферу обмена
        clipboard.setText(text)  # type: ignore # Установка текста в буфер обмена
        self.txtFormula.setFocus()

    def showEvent(self, event):
        super().showEvent(event)
        self.customize_results_columns()

    def resizeEvent(self, event):
        """Переопределение изменения размера окна"""
        super().resizeEvent(event)
        self.customize_results_columns()

    def keyPressEvent(self, event):
        """Переопределение обработки нажатия клавиши"""

        # При нажатии клавиши F1 вызов справки.
        if event.key() == Qt.Key.Key_F1:
            open_help()  # открываем файл со справкой

    def closeEvent(self, event):
        """Переопределение метода выхода из программы"""

        self.write_history_to_csv_file()  # записываем таблицу истории вычислений в файл
        event.accept()

    def write_history_to_csv_file(self):
        """Записывает историю вычислений и результатов в csv файл"""

        history_table_row = self.get_history_table_data()

        # Запись данных в CSV файл
        try:
            with open(
                Const.HISTORY_FILE_NAME, mode="w", newline="", encoding="utf-8-sig"
            ) as file:
                writer = csv.writer(file, delimiter=Const.EXCEL_LIST_SEPARATOR)
                writer.writerow(Const.CSV_HEADERS)
                writer.writerows(history_table_row)
        except Exception as e:
            show_error_message(self, f"{Const.FAILED_TO_WRITE_HISTORY_TEXT}\n {e}")

    def get_history_table_data(self) -> list[tuple]:
        """Чтение данных из таблицы истории"""
        total_row_history = (
            self.tblResults.rowCount()
        )  # Количество строк в таблице истории
        return [
            (self.tblResults.item(row, 1).text(), self.tblResults.item(row, 2).text())
            for row in range(total_row_history)
        ]  # Передаём пары [Формула, Результат]

    def start(self) -> int:
        """Запуск приложения и отображение главного окна."""

        self.show()  # Показ формы
        return QtWidgets.QApplication.exec()  # Запуск основного цикла приложения


# Запуск приложения
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Создание экземпляра приложения
    calc_app = CalculatorApp()  # Создание экземпляра калькулятора
    sys.exit(calc_app.start())  # Запуск калькулятора
