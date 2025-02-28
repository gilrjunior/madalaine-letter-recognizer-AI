from madaline import *
from presets import *

def get_learn_rate(input):

    value = input.get()

    return value

def get_option_value(option):

    opt = option[0].get()
    value = option[1].get()

    return [opt, value]

def start_training(lr_input, option, madaline):

    learn_rate = get_learn_rate(lr_input)
    option_data = get_option_value(option)

    madaline.set_learn_rate(learn_rate)
    madaline.set_condition(option_data[0])
    madaline.set_stop_value(option_data[1])

    madalaine.training()

def clear_matrix(matrix):

    for r in matrix:
        for c in r:
            c.set(0)

def get_matrix_value(matrix):

    matrix_letter = []

    for r in matrix:
        row = []
        for c in r:
            row.append(c.get())
        matrix_letter.append(row)

    return matrix_letter

def set_matrix_value(cb, matrix):

    value = cb.get()

    function = globals()[f"get_{value}"]
    matrix_data = function()

    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            c.set(matrix_data[i][j])

def start_model(matrix, madaline, letter_text_label):

    matrix_value = get_matrix_value(matrix)

    letter = madaline.model(matrix_value)

    letter_text_label.config(text=letter)

