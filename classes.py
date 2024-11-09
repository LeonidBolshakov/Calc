from PyQt6.QtCore import QMimeData
from PyQt6.QtWidgets import QTextEdit

from functions import filter_out_unsafe_symbols


class CustomTextEdit(QTextEdit):
    """Класс для перехвата вставки текста из буфера обмена"""

    def __init__(self, parent=None):
        super().__init__(parent)

    def insertFromMimeData(self, source: QMimeData):
        """Подмена метода вставки данных из буфера обмена"""

        # Из текста убираем все лишние символы и передаём управление дальше
        if source.hasText():
            source = filter_out_unsafe_symbols(source)
        super().insertFromMimeData(source)
