import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import QMimeData


class CustomTextEdit(QTextEdit):
    def insertFromMimeData(self, source: QMimeData):
        # Изменяем текст перед вставкой
        if source.hasText():
            original_text = source.text()
            modified_text = f"Измененный текст: {original_text}"

            # Создаем новый QMimeData с измененным текстом
            new_mime_data = QMimeData()
            new_mime_data.setText(modified_text)

            # Вызываем родительский метод с новым QMimeData
            super().insertFromMimeData(new_mime_data)
        else:
            super().insertFromMimeData(source)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom QMimeData Example")

        self.text_edit = CustomTextEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
