from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableWidget with Resizable Columns")
        self.setGeometry(100, 100, 800, 600)

        # Create the QTableWidget
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)

        # Populate the table with some data
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                item = QTableWidgetItem(f"Item {row},{col}")
                self.tableWidget.setItem(row, col, item)

        # Create the layout and add the QTableWidget
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)

        # Create the central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def showEvent(self, event):
        super().showEvent(event)
        self.resizeColumns()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resizeColumns()

    def resizeColumns(self):
        table_width = self.tableWidget.width()
        num_columns = self.tableWidget.columnCount()
        column_width_percent = 100 / num_columns
        for column in range(num_columns):
            self.tableWidget.setColumnWidth(
                column, int(table_width * (column_width_percent / 100))
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
