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
    QWidget

)

from math import (
    sin,
    cos,
    tan,
    degrees
)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        measure_theta_line = QDoubleSpinBox()
        measure_theta_line.setRange(0, 90)
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
        result_label = QLabel("Results: ")
        measure_theta_line_label = QLabel("Measure of Theta")
        known_side_length_line_label = QLabel("Length of the Known Side")
        known_side_hoa_line_label = QLabel("HOA of the Known Side")
        unknown_side_hoa_line_label = QLabel("HOA of the Unknown Side")
        submit_button = QPushButton("Calculate")
        layout = QVBoxLayout()
        widgets = [
            title_label,
            measure_theta_line_label,
            measure_theta_line,
            known_side_length_line_label,
            known_side_length_line,
            known_side_hoa_line_label,
            known_side_hoa_line,
            unknown_side_hoa_line_label,
            unknown_side_hoa_line,
            submit_button,
            result_label
        ]

        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

        def calculate():
            known_side_hoa_line_var = str(known_side_hoa_line.currentText())
            unknown_side_hoa_line_var = str(unknown_side_hoa_line.currentText())
            known_side_length_line_var = float(known_side_length_line.value())
            measure_theta_line_var = float(measure_theta_line.value())
            if known_side_hoa_line_var == "Opposite" or unknown_side_hoa_line_var == "Opposite":
                if known_side_hoa_line_var == "Hypotenuse" or unknown_side_hoa_line_var == "Hypotenuse":
                    trig_function = "sin"
            elif known_side_hoa_line_var == "Adjacent" or unknown_side_hoa_line_var == "Adjacent":
                if known_side_hoa_line_var == "Hypotenuse" or unknown_side_hoa_line_var == "Hypotenuse":
                    trig_function = "cos"
            elif known_side_hoa_line_var == "Opposite" or unknown_side_hoa_line_var == "Opposite":
                if known_side_hoa_line_var == "Adjacent" or unknown_side_hoa_line_var == "Adjacent":
                    trig_function = "tan"
            else:
                exit("NO TRIG FUNCTION FOUND")
            
            if trig_function == "sin":
                if known_side_hoa_line_var == "Opposite":
                    trig_1 = known_side_length_line_var
                    trig_2 = "x"
                else:
                    trig_1 = "x"
                    trig_2 = known_side_length_line_var
            elif trig_function == "cos":
                if known_side_hoa_line == "Adjacent":
                    trig_1 = known_side_length_line_var
                    trig_2 = "x"
                else:
                    trig_1 = "x"
                    trig_2 = known_side_length_line_var
            elif trig_function == "tan":
                if known_side_hoa_line == "Opposite":
                    trig_1 = known_side_length_line_var
                    trig_2 = "x"
                else:
                    trig_1 = "x"
                    trig_2 = known_side_length_line_var
            if trig_function == "sin":
                theta_trig = sin(degrees(measure_theta_line_var))
            elif trig_function == "cos":
                theta_trig = cos(degrees(measure_theta_line_var))
            else:
                theta_trig = tan(degrees(measure_theta_line_var))
            if trig_2 == "x":
                missing_length = trig_1 / theta_trig
            else:
                missing_length = theta_trig * trig_2
            print(theta_trig)
            result_label.setText("Results: " + str(missing_length))

        submit_button.clicked.connect(calculate)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
