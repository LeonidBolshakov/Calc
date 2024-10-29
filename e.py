from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
import sys


class BrowserOpener(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Open MHT in Default Browser")
        self.setGeometry(100, 100, 300, 100)

        layout = QVBoxLayout()

        # Кнопка для открытия MHT файла
        self.open_button = QPushButton("Open MHT File")
        self.open_button.clicked.connect(self.open_mht_file)
        layout.addWidget(self.open_button)

        self.setLayout(layout)

    def open_mht_file(self):
        mht_file_path = "help.mht"
        QDesktopServices.openUrl(QUrl.fromLocalFile(mht_file_path))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserOpener()
    window.show()
    sys.exit(app.exec())
