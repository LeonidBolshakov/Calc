""" Приложение Калькулятор — позволяет проводить вычисления по формуле.
    В формуле можно использовать числа, скобки и арифметические действия.
     Ведётся и записывается на диск журнал расчётов.
     Журнал можно просматривать как текст и в программе MS EXCEL.
     Формулы можно копировать в буфер обмена.
     При вводе из буфера обмена вся
     ненужная информация в формулу не записывается."""

import csv
import sys

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QMainWindow

from classes import CustomTextEdit
from constants import Const
from formulas import F
from message import ask_for_continuation, show_error_message
from fuctions import bold_font, open_help


class CalculatorApp(QMainWindow):
    """Главный класс приложения калькулятора, наследующий от QMainWindow."""

    # Определение кнопок и текстовых полей
    btnClear: QtWidgets.QPushButton
    btnCopy: QtWidgets.QPushButton
    btnExit: QtWidgets.QPushButton
    btnHelp: QtWidgets.QPushButton
    btnRun: QtWidgets.QPushButton
    lblInf2: QtWidgets.QLabel
    txtFormula: CustomTextEdit
    txtResult: QtWidgets.QTextBrowser
    tblResults: QtWidgets.QTableWidget

    def __init__(self) -> None:
        """Инициализация приложения и загрузка UI."""
        super().__init__()

        # Загрузка UI
        uic.loadUi(Const.CALC_UI, self)

        self.f = F(self)  # Методы работы с формулой
        self.setup()  # Настройка элементов интерфейса
        self.setup_connections()  # Установка соединений сигналов и слотов

    def closeEvent(self, event):
        """Переопределение метода выхода из программы"""

        # self.write_history()  # записываем таблицу истории вычислений в файл
        self.write_history()  # записываем таблицу истории вычислений в файл

        event.accept()

    def keyPressEvent(self, event):
        """Переопределение обработки нажатия клавиши"""

        # При нажатии клавиши F1 вызов справки.
        if event.key() == Qt.Key.Key_F1:
            open_help()  # открываем файл со справкой

    def setup(self) -> None:
        """Настройка начальных параметров интерфейса."""

        self.txtFormula.setFocus()  # Установка фокуса на поле ввода формулы
        self.setup_table_results()  # Настройка таблицы результатов
        self.init_table_results()  # Инициализация таблицы результатов
        self.setup_info()  # Настройка информационной части окна
        self.setup_bold()  # Установка жирного шрифта для некоторых элементов

    def setup_table_results(self):
        """Настройка внешнего вида таблицы результатов"""

        self.setup_tbl_columns()  # Настройка колонок таблицы результатов

        self.tblResults.horizontalHeader().setVisible(
            False
        )  # Скрыть горизонтальный заголовок
        self.tblResults.verticalHeader().setVisible(
            False
        )  # Скрыть вертикальный заголовок

    def setup_bold(self):
        """Установка жирного начертания для шрифтов элементов управления."""
        widgets = (self.btnRun, self.btnExit, self.txtFormula, self.txtResult)
        for widget in widgets:
            widget.setFont(bold_font(widget.font()))  # Установка жирного шрифта

    # noinspection PyUnresolvedReferences
    def setup_connections(self) -> None:
        """Привязка сигналов к слотам"""

        # Привязка статичных кнопок к слотам
        self.btnClear.clicked.connect(self.clear_all)
        self.btnCopy.clicked.connect(self.copy_result_clipboard)
        self.btnExit.clicked.connect(QtWidgets.QApplication.quit)
        self.btnHelp.clicked.connect(open_help)
        self.btnRun.clicked.connect(self.f.formula_processing)

        # Переопределение обработки нажатий клавиш при вводе формулы
        self.txtFormula.keyPressEvent = self.f.handle_key_press  # type: ignore

    def copy_result_clipboard(self) -> None:
        """Копирование результата вычислений в буфер обмена"""

        text = self.txtResult.toPlainText()  # Получение текста результата вычислений
        clipboard = (
            QtWidgets.QApplication.clipboard()
        )  # Получение доступа к буферу обмена
        clipboard.setText(text)  # type: ignore # Установка текста в буфер обмена
        self.txtFormula.setFocus()  # Установка фокуса обратно на поле ввода

    def clear_all(self):
        """Очистка формулы, поля результата и истории"""

        self.clear_formula_result()
        if ask_for_continuation(Const.DIALOG_ASK):
            self.tblResults.clear()  # Очищаем историю
            self.tblResults.setRowCount(0)  # Удаляем строки
        self.txtFormula.setFocus()  # Установка фокуса обратно на поле ввода

    def start(self) -> int:
        """Запуск приложения и отображение главного окна."""

        self.show()  # Показ формы
        return QtWidgets.QApplication.exec()  # Запуск основного цикла приложения

    def out_result(self, formula: str, result: str) -> None:
        """Вывод результата вычисления в текстовое поле и таблицу истории."""

        self.out_in_result(result)  # Вывод результата в текстовое поле
        self.out_in_tbl_results(formula, result)  # Вывод формулы и результата в таблицу

    def out_in_tbl_results(self, formula: str, result: str):
        """Добавление новой строки с формулой и результатом в таблицу истории."""

        new_row = 0  # Новую строку вставляем в начало таблицы
        self.tblResults.insertRow(new_row)  # Вставка новой строки

        self.add_button_in_row(new_row)  # Добавляем кнопку в новую строку
        self.add_item_in_row(new_row, 1, formula)  # Добавляем формулу в новую строку
        # Добавляем результат в новую строку и выравниваем по правому краю.
        self.add_item_in_row(new_row, 2, result, "right")

    def copy_history_clipboard(self, row: int) -> None:
        """Копирование формулы из таблицы результатов в буфер обмена."""

        text = self.tblResults.item(  # type: ignore
            row, 1
        ).text()  # Получение текста формулы из таблицы
        clipboard = (
            QtWidgets.QApplication.clipboard()
        )  # Получение доступа к буферу обмена
        clipboard.setText(text)  # type: ignore # Установка текста в буфер обмена
        self.txtFormula.setFocus()

    def add_item_in_row(self, row: int, column: int, text: str, align: str = "left"):
        """Добавляем элемент в таблицу,
        делаем его недоступным для редактирования и выравниваем."""

        item = QTableWidgetItem(text)  # Создание нового элемента таблицы

        # Запрет редактирования
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

        # Установка выравнивания текста
        qt_align = (
            Qt.AlignmentFlag.AlignRight
            if align == Const.DIRECTION_RIGHT
            else Qt.AlignmentFlag.AlignLeft
        )  # Установка выравнивания в зависимости от параметра
        item.setTextAlignment(qt_align)  # Применение выравнивания к элементу

        # Добавление элемента в таблицу
        self.tblResults.setItem(row, column, item)

    # noinspection PyUnresolvedReferences
    def add_button_in_row(self, row: int) -> None:
        """Создание кнопки в строке таблицы. Кнопка нужна для копирования формулы."""

        # Создание кнопки с текстом "C"
        button = QtWidgets.QPushButton(Const.TEXT_BUTTON_COPY)

        # Привязка события нажатия кнопки к методу копирования формулы
        button.clicked.connect(lambda checked, r=row: self.copy_history_clipboard(r))

        # Добавление кнопки в соответствующую строку таблицы
        self.tblResults.setCellWidget(row, 0, button)

    def out_in_result(self, result: str) -> None:
        """Вывод результата вычисления в поле 'Результат'"""

        self.txtResult.setPlainText(result)

    def write_history(self):
        """Записывает историю вычислений и результатов в csv файл"""

        results = self.read_from_tblResults()

        # Запись данных в CSV файл
        try:
            with open(
                Const.FILE_HISTORY, mode="w", newline="", encoding="utf-8-sig"
            ) as file:
                writer = csv.writer(file, delimiter=Const.DELIMITER)
                writer.writerow(Const.HEAD_CSV_FILE)
                writer.writerows(results)
        except Exception as e:
            show_error_message(self, f"{Const.TEXT_ERROR_WRITE}\n {e}")

    def init_table_results(self):
        """Историю из csv файла переписываем в таблицу результатов"""

        try:
            with open(Const.FILE_HISTORY, mode="r", encoding="utf-8-sig") as file:
                reader = csv.reader(file, delimiter=Const.DELIMITER)
                next(reader)  # Пропускаем шапку документа

                # Построчно записываем данные файла в таблицу истории результатов
                for rec in reader:
                    self.out_in_tbl_results(formula=rec[0], result=rec[1])
        except FileNotFoundError:
            pass  # отсутствие файла не ошибка — начинаем историю с чистого листа
        except Exception as e:
            # При чтении файла ошибке — выдаём сообщение Пользователю
            show_error_message(self, f"{Const.TEXT_ERROR_READ} \n{e}")

    def setup_info(self):
        """В строку информации проставляем имя файла вывода"""

        self.lblInf2.setText(self.lblInf2.text().replace("#", Const.FILE_HISTORY))

    def clear_formula_result(self):
        """Очищаем текстовые поля ввода формулы и вывода результата"""

        self.txtFormula.clear()  # Очищаем поле формулы
        self.txtResult.clear()  # Очищаем поле результата

    def setup_tbl_columns(self):
        """Настраиваем ширину колонок таблицы результатов"""

        self.tblResults.setColumnCount(3)  # Установка количества колонок
        self.tblResults.setColumnWidth(0, Const.WIDTH_COLUMN_BUTTON)
        self.tblResults.setColumnWidth(1, Const.WIDTH_COLUMN_FORMULA)
        self.tblResults.setColumnWidth(2, Const.WIDTH_COLUMN_RESULT)

    def read_from_tblResults(self) -> list[tuple]:
        """Чтение данных из таблицы результатов"""

        total = self.tblResults.rowCount()  # Количество строк в таблице результатов
        return [
            (self.tblResults.item(row, 1).text(), self.tblResults.item(row, 2).text())
            for row in range(total)
        ]  # Передаём пары (Формула, Результат)


# Запуск приложения
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Создание экземпляра приложения
    calc_app = CalculatorApp()  # Создание экземпляра калькулятора
    sys.exit(calc_app.start())  # Запуск калькулятора
