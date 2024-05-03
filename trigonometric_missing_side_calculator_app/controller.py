"""controller.py
This program takes user inputs given by app.py to do the calculations
to find the missing side of a right triangle.
by Adam Ainsworth
"""

from math import (
    sin,
    cos,
    tan,
    radians,
)


def calculate(known_hoa_var: str, unknown_hoa_var: str, known_side_length_line_var: float, measure_theta_line_var: float):
    """Takes the user's inputs and calculates the missing side."""
    trig_function = find_trig_function(known_hoa_var, unknown_hoa_var)
    if trig_function == "error":
        return ("Error! Could not find trig function")
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
        if known_hoa_var == "Adjacent":
            trig_1 = known_side_length_line_var
            trig_2 = "x"
        else:
            trig_1 = "x"
            trig_2 = known_side_length_line_var
    elif trig_function == "tan":
        if known_hoa_var == "Opposite":
            trig_1 = known_side_length_line_var
            trig_2 = "x"
        else:
            trig_1 = "x"
            trig_2 = known_side_length_line_var
    if trig_function == "sin":
        theta_trig = sin(radians(measure_theta_line_var))
    elif trig_function == "cos":
        theta_trig = cos(radians(measure_theta_line_var))
    elif trig_function == "tan":
        theta_trig = tan(radians(measure_theta_line_var))
    print(trig_2)
    if trig_2 == "x":
        missing_length = trig_1 / theta_trig
    else:
        missing_length = theta_trig * trig_2
    return ("Results: " + str(missing_length))


def find_trig_function(known_hoa_var, unknown_hoa_var):
    """Finds the correct trigonometric function for the program
    to use based on the user's inputs."""
    if known_hoa_var == "Opposite" or unknown_hoa_var == "Opposite":
        if known_hoa_var == "Hypotenuse" or unknown_hoa_var == "Hypotenuse":
            trig_function = "sin"
        elif known_hoa_var == "Adjacent" or unknown_hoa_var == "Adjacent":
            trig_function = "tan"
        else:
            return ("error")
    elif known_hoa_var == "Adjacent" or unknown_hoa_var == "Adjacent":
        if known_hoa_var == "Hypotenuse" or unknown_hoa_var == "Hypotenuse":
            trig_function = "cos"
        elif known_hoa_var == "Opposite" or unknown_hoa_var == "Opposite":
            trig_function = "tan"
        else:
            return ("error")
    elif known_hoa_var == "Hypotenuse" or unknown_hoa_var == "Hypotenuse":
        if known_hoa_var == "Adjacent" or unknown_hoa_var == "Adjacent":
            trig_function = "cos"
        elif known_hoa_var == "opposite" or unknown_hoa_var == "opposite":
            trig_function = "sin"
        else:
            return ("error")
    else:
        return ("error")
    return (trig_function)