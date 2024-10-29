import csv
import sys

import constant as c
from formula import F
from message import ask_for_continuation, show_error_message

from PyQt6 import QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt, QFileInfo, QUrl
from PyQt6.QtWidgets import QTableWidgetItem, QMainWindow, QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView


class CalculatorApp(QMainWindow):
    """Главный класс приложения калькулятора, наследующий от QMainWindow."""

    # Определение кнопок и текстовых полей
    btnClear: QtWidgets.QPushButton
    btnCopy: QtWidgets.QPushButton
    btnExit: QtWidgets.QPushButton
    btnHelp: QtWidgets.QPushButton
    btnRun: QtWidgets.QPushButton
    lblInf2: QtWidgets.QLabel
    txtFormula: QtWidgets.QTextEdit
    txtResult: QtWidgets.QTextBrowser
    tblResults: QtWidgets.QTableWidget

    def __init__(self) -> None:
        """Инициализация приложения и загрузка UI."""
        super().__init__()

        # Загрузка UI
        uic.loadUi(c.Const.CALC_UI, self)

        self.f = F(self)  # Методы работы с формулой
        self.browser = QWebEngineView()  # браузер для просмотра Help
        self.setup()  # Настройка элементов интерфейса
        self.setup_connections()  # Установка соединений сигналов и слотов
        # Атрибут необходим для того, что бы окно не было удалено сборщиком мусора.
        self.help_window = None

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

    # noinspection PyUnresolvedReferences
    def setup_connections(self) -> None:
        """Привязка сигналов к методам обработки событий,
        кроме кнопок копирования."""

        # Привязка кнопок к соответствующим методам
        self.btnClear.clicked.connect(self.clear_all)
        self.btnCopy.clicked.connect(self.copy_result_clipboard)
        self.btnExit.clicked.connect(QtWidgets.QApplication.quit)
        self.btnHelp.clicked.connect(self.open_help)
        self.btnRun.clicked.connect(self.f.calculate_formula)

        # Переопределение обработки нажатий клавиш при вводе формулы
        self.txtFormula.keyPressEvent = self.f.handle_key_press  # type: ignore

    @staticmethod
    def bold_font(font: QtGui.QFont) -> QtGui.QFont:
        """Возвращает шрифт с установленным жирным начертанием."""

        font.setBold(True)
        return font

    def keyPressEvent(self, event):
        # Проверяем, была ли нажата клавиша F1
        if event.key() == Qt.Key.Key_F1:
            self.open_help()

    def copy_result_clipboard(self) -> None:
        """Копирование результата в буфер обмена"""

        text = self.txtResult.toPlainText()  # Получение текста результата
        clipboard = (
            QtWidgets.QApplication.clipboard()
        )  # Получение доступа к буферу обмена
        clipboard.setText(text)  # type: ignore # Установка текста в буфер обмена
        self.txtFormula.setFocus()  # Установка фокуса обратно на поле ввода

    def clear_all(self):
        """Очистка формулы, поля результата и истории"""

        self.clear_formula_result()
        if ask_for_continuation(c.Const.DIALOG_ASK):
            self.tblResults.setRowCount(0)  # Очищаем историю
        self.txtFormula.setFocus()  # Установка фокуса обратно на поле ввода

    def start(self) -> None:
        """Запуск приложения и отображение главного окна."""

        self.show()  # Показ формы
        QtWidgets.QApplication.exec()  # Запуск основного цикла приложения

    def out_result(self, formula: str, result: str) -> None:
        """Вывод результата вычисления в текстовое поле и таблицу истории."""

        self.out_in_result(result)  # Вывод результата в текстовое поле
        self.out_in_tbl_results(formula, result)  # Вывод формулы и результата в таблицу

    def out_in_tbl_results(self, formula: str, result: str):
        """Добавление новой строки с формулой и результатом в таблицу истории."""

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
        self.txtFormula.setFocus()

    def add_item_in_row(self, row: int, column: int, text: str, align: str = "left"):
        """Добавляем элемент в таблицу,
        делаем недоступным для редактирования и выравниваем"""

        item = QTableWidgetItem(text)  # Создание нового элемента таблицы

        # Запрет редактирования
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

        # Установка выравнивания текста
        qt_align = (
            Qt.AlignmentFlag.AlignRight
            if align == c.Const.DIRECTION_RIGHT
            else Qt.AlignmentFlag.AlignLeft
        )  # Установка выравнивания в зависимости от параметра
        item.setTextAlignment(qt_align)  # Применение выравнивания к элементу

        # Добавление элемента в таблицу
        self.tblResults.setItem(row, column, item)

    # noinspection PyUnresolvedReferences
    def add_button_in_row(self, row: int) -> None:
        """Создание кнопки в строке таблицы. Для копирования формулы."""

        # Создание кнопки с текстом "C"
        button = QtWidgets.QPushButton(c.Const.TEXT_BUTTON_COPY)

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
                c.Const.FILE_HISTORY, mode="w", newline="", encoding="utf-8-sig"
            ) as file:
                writer = csv.writer(file, delimiter=c.Const.DELIMITER)
                writer.writerow(c.Const.HEAD_CSV_FILE)
                writer.writerows(results)
        except Exception as e:
            show_error_message(self, f"{c.Const.TEXT_ERROR_WRITE}\n {e}")

    def init_table_results(self):
        """Историю из csv файла переписываем в таблицу результатов"""

        try:
            with open(c.Const.FILE_HISTORY, mode="r", encoding="utf-8-sig") as file:
                reader = csv.reader(file, delimiter=c.Const.DELIMITER)
                next(reader)  # Пропускаем шапку документа

                # Построчно записываем данные файла в таблицу истории результатов
                for row, rec in enumerate(reader):
                    self.out_in_tbl_results(formula=rec[0], result=rec[1])
        except FileNotFoundError:
            pass  # отсутствие файла не ошибка — начинаем историю с чистого листа
        except Exception as e:
            # При ошибке чтения файла выдаём сообщение Пользователю
            show_error_message(self, f"{c.Const.TEXT_ERROR_READ} \n{e}")

    def setup_info(self):
        """В строку информации проставляем имя файла вывода"""

        self.lblInf2.setText(self.lblInf2.text().replace("#", c.Const.FILE_HISTORY))

    def clear_formula_result(self):
        """Очищаем текстовые поля ввода формулы и вывода результата"""

        self.txtFormula.clear()  # Очищаем поле формулы
        self.txtResult.clear()  # Очищаем поле результата

    def setup_tbl_columns(self):
        """Определяем количество и ширину колонок"""

        self.tblResults.setColumnCount(3)  # Установка количества колонок
        self.tblResults.setColumnWidth(0, c.Const.WIDTH_COLUMN_BUTTON)
        self.tblResults.setColumnWidth(1, c.Const.WIDTH_COLUMN_FORMULA)
        self.tblResults.setColumnWidth(2, c.Const.WIDTH_COLUMN_RESULT)

    def read_from_tblResults(self) -> list[tuple]:
        """Чтение данных из таблицы результатов"""

        total = self.tblResults.rowCount()  # Количество строк в таблице результатов
        return [
            (self.tblResults.item(row, 1).text(), self.tblResults.item(row, 2).text())
            for row in range(total)
        ]  # Передача пар (Формула, Результат)

    # noinspection PyUnresolvedReferences
    def open_help(self):
        """Вызов Help файла"""

        absolute_path = self.create_window_help()
        self.show_window_help(absolute_path)

    def on_load_finished(self):
        """После завершения загрузки файла — показываем окно справки."""

        # Без данного оператора программа не знает об окончании загрузки файла и
        # окно долго остаётся чёрным.
        self.help_window.show()

    def create_window_help(self) -> str:
        """Создаём окно для вывода справки"""

        if not self.help_window:
            self.help_window = QMainWindow()
            self.help_window.setWindowTitle(c.Const.TEXT_TITLE_HELP)
        # Получаем абсолютный путь к файлу справки
        file_info = QFileInfo(c.Const.FILE_HELP)
        return file_info.absoluteFilePath()

    # noinspection PyUnresolvedReferences
    def show_window_help(self, absolute_path: str) -> None:
        """Показываем окно справки"""

        # Создаём центральный виджет и компоновщик
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        # Добавляем QWebEngineView в компоновщик
        layout.addWidget(self.browser)
        # Устанавливаем центральный виджет нового окна
        self.help_window.setCentralWidget(central_widget)
        # Подключаем сигнал loadFinished к слоту
        self.browser.loadFinished.connect(self.on_load_finished)
        # Показываем новое окно
        self.help_window.resize(*c.Const.SIZE_WINDOW_HELP)
        self.help_window.show()

        # Настраиваем QWebEngineView
        self.browser.setUrl(QUrl.fromLocalFile(absolute_path))


# Запуск приложения
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Создание экземпляра приложения
    calc_app = CalculatorApp()  # Создание экземпляра калькулятора
    calc_app.start()  # Запуск калькулятора
