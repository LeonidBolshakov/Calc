from PyQt6.QtWidgets import (
    QMessageBox,
    QDialog,
    QVBoxLayout,
    QPushButton,
    QLabel,
)
import constant as c


class CustomDialog(QDialog):
    def __init__(self, warning, parent=None):
        super().__init__(parent)
        self.setWindowTitle(c.Const.DIALOG_TITLE)

        layout = QVBoxLayout(self)
        label = QLabel(warning, self)
        layout.addWidget(label)

        ok_button = QPushButton(c.Const.DIALOG_AGREE, self)
        cancel_button = QPushButton(c.Const.DIALOG_REJECTION, self)
        layout.addWidget(ok_button)
        layout.addWidget(cancel_button)

        # noinspection PyUnresolvedReferences
        ok_button.clicked.connect(self.accept)
        # noinspection PyUnresolvedReferences
        cancel_button.clicked.connect(self.reject)
        cancel_button.setFocus()


def ask_for_continuation(warning: str) -> int:
    dialog = CustomDialog(warning)
    return dialog.exec()


def show_error_message(parent, message: str):
    """Выводим сообщение об ошибке"""
    QMessageBox.critical(parent, c.Const.TEXT_TITLE_ERROR, message)
