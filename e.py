class CustomTextEdit(QTextEdit):
    """Класс для перехвата вставки текста из буфера обмена"""

    def insertFromMimeData(self, source: QMimeData):
        if source.hasText():
            text = source.text()
        super().insertFromMimeData(source)
