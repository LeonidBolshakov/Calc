import sys
import unittest
from unittest.mock import patch
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt6.QtTest import QTest
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

    def keyPressEvent(self, event: QKeyEvent):
        print(f"Перехватили клавишу {event.modifiers()=} {event.key()=}")
        if event.key() == Qt.Key.Key_F1:
            print("F1")
            self.text_edit.insertPlainText("F1 was pressed\n")
        elif (
            event.modifiers() == Qt.KeyboardModifier.ControlModifier
            and event.key() == Qt.Key.Key_V
        ):
            print("elif")
            self.text_edit.insertPlainText("Ctrl+V was pressed\n")
        else:
            print("else")
            self.text_edit.insertPlainText("Другая клавиша\n")
        print("?????")


class TestKeyPress(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow()
        self.window.show()

    def test_f1_key_press(self):
        # Имитируем нажатие клавиши F1
        QTest.keyPress(self.window, Qt.Key.Key_F1)

        # Проверяем, что текст был добавлен
        self.assertIn("F1 was pressed", self.window.text_edit.toPlainText())

    def test_ctrl_v_key_press(self):
        # Устанавливаем текст в буфер обмена
        clipboard = QApplication.clipboard()
        clipboard.setText("Тестовый текст")

        # Имитируем нажатие Ctrl+V
        # QTest.keyClick(self.window, Qt.Key.Key_V, Qt.KeyboardModifier.ControlModifier)
        QTest.keyPress(
            self.window.windowHandle(), "V", Qt.KeyboardModifier.ControlModifier
        )


if __name__ == "__main__":
    unittest.main()
    #
    # app = QApplication(sys.argv)
    # window = MainWindow()
    # window.show()
    # sys.exit(app.exec())
