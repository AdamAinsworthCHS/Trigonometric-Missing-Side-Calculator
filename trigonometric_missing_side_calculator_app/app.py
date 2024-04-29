import sys
import controller

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QDoubleSpinBox,
    QComboBox,
    QLabel,
    QPushButton,
    QMainWindow,
    QApplication,
    QWidget,
    QGridLayout,
    
)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        measure_theta_line = QDoubleSpinBox()
        measure_theta_line.setRange(0, 89.99)
        known_side_length_line = QDoubleSpinBox()
        known_side_length_line.setRange(0, 999999999999)
        known_side_hoa_line = QComboBox()
        known_side_hoa_line.addItems([
            "--",
            "Hypotenuse",
            "Opposite",
            "Adjacent"
        ])
        unknown_side_hoa_line = QComboBox()
        unknown_side_hoa_line.addItems([
            "--",
            "Hypotenuse",
            "Opposite",
            "Adjacent"
        ])
        title_label = QLabel("Trigonometric Missing Side Calculator")
        title_label.setIndent(0)
        title_label.setMargin(5)
        result_label = QLabel("Results: ")
        measure_theta_line_label = QLabel("Measure of Theta")
        known_side_length_line_label = QLabel("Length of the Known Side")
        known_side_hoa_line_label = QLabel("HOA of the Known Side")
        unknown_side_hoa_line_label = QLabel("HOA of the Unknown Side")
        submit_button = QPushButton("Calculate")
        layout = QGridLayout()

        layout.addWidget(title_label, 1, 1, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(measure_theta_line_label, 2, 1, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(measure_theta_line, 2, 2, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(known_side_length_line_label, 3, 1, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(known_side_length_line, 3, 2, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(known_side_hoa_line_label, 4, 1, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(known_side_hoa_line, 4, 2, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(unknown_side_hoa_line_label, 5, 1, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(unknown_side_hoa_line, 5, 2, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(submit_button, 6, 1, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(result_label, 6, 2, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

        def calculate_self():
            hoa_known = str(known_side_hoa_line.currentText())
            hoa_unknown = str(unknown_side_hoa_line.currentText())
            known_length = float(known_side_length_line.value())
            theta_measure = float(measure_theta_line.value())
            results = controller.calculate(hoa_known, hoa_unknown, known_length, theta_measure)
            result_label.setText(results)
        
        submit_button.clicked.connect(calculate_self)

        
        
        
        


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
