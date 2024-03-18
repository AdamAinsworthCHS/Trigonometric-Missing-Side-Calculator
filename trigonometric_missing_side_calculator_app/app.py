import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QDoubleSpinBox,
    QComboBox,
    QLabel,
    QPushButton,
    QMainWindow,
    QApplication,
    QVBoxLayout,
    QWidget,
    QSpinBox
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")
        
        measure_theta_line = QDoubleSpinBox()
        measure_theta_line.setRange(0, 90)
        self.setCentralWidget(measure_theta_line)
        known_side_length_line = QDoubleSpinBox()
        known_side_length_line.setRange(0, 999999999999)
        known_side_hoa_line = QComboBox()
        known_side_hoa_line.addItems(["Hypotenuse", "Opposite", "Adjacent"])
        layout = QVBoxLayout()
        widgets = [
            measure_theta_line,
            known_side_length_line,
            known_side_hoa_line
        ]

        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()