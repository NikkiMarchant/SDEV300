"""Lab3. Nicole Marchant. This is a state lookup module."""
import re
import sys
import numpy as np


def float_formatter(num:float):
    """Formatter for np.set_printoptions"""
    return f'{num:.2f}'

def main():
    """This is the main function"""
    np.set_printoptions(formatter={'float_kind':float_formatter})
    print('Welcome to the Python Matrix Application')
    while True:
        print('Do you want to play the Matrix Game?')

        answer = validate('Enter Y for Yes and N for No: ', r'[YyNn]')
        if answer.lower() == 'n':
            print('Thanks for playing Python Numpy')
            sys.exit()

        validate('Enter phone number XXX-XXX-XXXX:',r'^\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}$')

        validate('Enter zip code+4 XXXXX-XXXX: ', r'^\(?\d{5}\)?[-\s]?\d{4}$')

        matrix1 = get_matrix(3,3)
        matrix2 = get_matrix(3,3)

        lab4_menu = ['a','b','c','d']

        while True:
            print('Select an operation')
            print('a. Addition')
            print('b. Subtraction')
            print('c. Matrix Multiplication')
            print('d. Element by element multiplication')
            choice = input("> ")
            if choice in lab4_menu:
                break
            print('Invalid choice')
        print(matrix1)
        if choice == 'a':
            matrix3 = matrix1+matrix2
            print('\t\t+')
        elif choice == 'b':
            matrix3 = matrix1-matrix2
            print('\t\t-')
        elif choice == 'c':
            matrix3 = matrix1*matrix2
            print('\t\t*')
        else:
            matrix3 = np.matmul(matrix1,matrix2)
            print('\t\tmatmul')
        print(matrix2, '\n\t\t=\n', matrix3)

def get_matrix(rows, cols):
    """Promps for matrix from user"""
    matrix = []

    print('Enter numbers for your matrix')

    for i in range(rows*cols):
        while True:
            try:
                num = float(input(f'Entry {i+1}: '))
                matrix.append(num)

            except ValueError:
                continue
            break
    return np.array(matrix).reshape((rows,cols))

def validate(question, reg_ex):
    """Prompts for user input and validates using regular expression"""
    invalid = True
    while invalid:
        answer = input(question)

        if re.search(reg_ex, answer):
            break
        print('Incorrect Format')

    return answer

if __name__ == '__main__':
    main()
