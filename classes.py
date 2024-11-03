from PyQt6.QtCore import QMimeData
from PyQt6.QtWidgets import QTextEdit

from formulas import F
from fuctions import only_safe_symbols


class CustomTextEdit(QTextEdit):
    """Класс для перехвата вставки текста из буфера обмена"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.f = F(self)  # Методы работы с формулой

    def insertFromMimeData(self, source: QMimeData):
        """Подмена метода вставки данных из буфера обмена"""

        # Из текста убираем все лишние символы и передаём управление дальше
        if source.hasText():
            source = only_safe_symbols(source)
        super().insertFromMimeData(source)
