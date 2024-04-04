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
    radians
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
            known_hoa_var = str(known_side_hoa_line.currentText())
            known_side_length_line_var = float(known_side_length_line.value())
            measure_theta_line_var = float(measure_theta_line.value())
            trig_function = find_trig_function()
            print(trig_function)
            if trig_function == "error":
                return
            if trig_function == "sin":
                if known_hoa_var == "Opposite":
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
                theta_trig = (sin(radians(measure_theta_line_var)))
                print("it's sin time!")
            elif trig_function == "cos":
                theta_trig = (cos(radians(measure_theta_line_var)))
                print("it's cos time!")
            elif trig_function == "tan":
                theta_trig = (tan(radians(measure_theta_line_var)))
                print("it's tan time!")
            print(theta_trig)
            if trig_2 == "x":
                missing_length = trig_1 / theta_trig
            else:
                missing_length = theta_trig * trig_2
            result_label.setText("Results: " + str(missing_length))

        submit_button.clicked.connect(calculate)

        def find_trig_function():
            known_hoa_var = str(known_side_hoa_line.currentText())
            unknown_hoa_var = str(unknown_side_hoa_line.currentText())
            if known_hoa_var == "Opposite" or unknown_hoa_var == "Opposite":
                if known_hoa_var == "Hypotenuse" or unknown_hoa_var == "Hypotenuse":
                    trig_function = "sin"
                elif known_hoa_var == "Adjacent" or unknown_hoa_var == "Adjacent":
                    trig_function = "tan"
                else:
                    result_label.setText("Results: " + "Error! Couldn't find trig function.")
                    return ("error")
            elif known_hoa_var == "Adjacent" or unknown_hoa_var == "Adjacent":
                if known_hoa_var == "Hypotenuse" or unknown_hoa_var == "Hypotenuse":
                    trig_function = "cos"
                elif known_hoa_var == "Opposite" or unknown_hoa_var == "Opposite":
                    trig_function = "tan"
                else:
                    result_label.setText("Results: " + "Error! Couldn't find trig function.")
                    return ("error")
            elif known_hoa_var == "Hypotenuse" or unknown_hoa_var == "Hypotenuse":
                if known_hoa_var == "Adjacent" or unknown_hoa_var == "Adjacent":
                    trig_function = "cos"
                elif known_hoa_var == "opposite" or unknown_hoa_var == "opposite":
                    trig_function = "sin"
                else:
                    result_label.setText("Results: " + "Error! Couldn't find trig function.")
                    return ("error")
            else:
                result_label.setText("Results: " + "Error! Couldn't find trig function.")
                return ("error")
            return (trig_function)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
