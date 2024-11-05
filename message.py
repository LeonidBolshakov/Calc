from PyQt6.QtWidgets import (
    QMessageBox,
    QDialog,
    QVBoxLayout,
    QPushButton,
    QLabel,
)
import constants as c


class CustomDialog(QDialog):
    """Пользовательский класс диалога"""

    def __init__(self, warning, parent=None):
        super().__init__(parent)
        self.setWindowTitle(c.Const.DIALOG_TITLE)

        # Выводим текст сообщения
        layout = QVBoxLayout(self)
        label = QLabel(warning, self)
        layout.addWidget(label)

        # Выводим кнопки "Согласен", "Отказываюсь".
        accept_button = QPushButton(c.Const.DIALOG_ACCEPT, self)
        rejection_button = QPushButton(c.Const.DIALOG_REJECTION, self)
        layout.addWidget(accept_button)
        layout.addWidget(rejection_button)

        # Назначение нажатию кнопки стандартной функции "Согласен"
        accept_button.clicked.connect(self.accept)
        # Назначение нажатию кнопки стандартной функции "Отказ"
        rejection_button.clicked.connect(self.reject)
        rejection_button.setFocus()  # По умолчанию - "Отказ"


def ask_for_continuation(warning: str) -> int:
    """Организуем диалог "Согласен <-> Отказ"""

    dialog = CustomDialog(warning)
    return dialog.exec()


def show_error_message(parent, message: str):
    """Выводим сообщение об ошибке"""

    QMessageBox.critical(parent, c.Const.ERROR_MESSAGE_TITLE, message)
