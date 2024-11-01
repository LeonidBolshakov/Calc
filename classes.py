from PyQt6.QtCore import QMimeData
from PyQt6.QtWidgets import QTextEdit

from constant import Const
from formulas import F


class CustomTextEdit(QTextEdit):
    """Класс для перехвата вставки текста из буфера обмена"""

    def __init__(self, parent=None):
        super().__init__(parent)

    def insertFromMimeData(self, source: QMimeData):
        """Подмена метода вставки данных из буфера обмена"""

        # Из текста убираем все лишние символы и передаём управление дальше
        if source.hasText():
            source = self.only_safe_symbols(source)
        super().insertFromMimeData(source)

    @staticmethod
    def only_safe_symbols(source: QMimeData) -> QMimeData:
        """Убираем из текста контейнера для данных лишние символы"""

        # заменяем символы синонимы на стандартные (':' на '/').
        text_standard = F.symbol_standardization(source.text())
        # Убираем лишние символы и корректируем контейнер для данных
        text_safe = "".join([c for c in text_standard if c in Const.SAFE_SYMBOLS])
        new_source = QMimeData()
        new_source.setText(text_safe)

        return new_source
