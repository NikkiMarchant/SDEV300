"""Lab2. Nicole Marchant. This is a secure password module."""
import string
import sys
import math
import secrets
import datetime

def main():
    """This is the main flow control"""
    # https://openbookproject.net/pybiblio/tips/wilson/dictionaryMenus.php
    # https://stackoverflow.com/questions/9168340/using-a-dictionary-to-select-function-to-execute
    # Use dictionary of functions for menu
    lab2_menu = {"a" : secure_password,
                 "b" : format_percent,
                 "c" : days_until,
                 "d" : triangle_leg,
                 "e" : cylinder_volume,
                 "f" : menu_exit}
    while True:
        print("This is a menu")
        print(" a. Generate Secure Password")
        print(" b. Calculate and Format a Percentage")
        print(" c. Days until July 4, 2025")
        print(" d. Calculate the leg of a triangle")
        print(" e. Calculate the volume of a Right Circular Cylinder")
        print(" f. Exit program")
        try:
            choice = input("> ")
            lab2_menu.get(choice.lower())()
        except (TypeError, ValueError):
            print("Invalid input")
        except KeyboardInterrupt:
            menu_exit()
        except ZeroDivisionError:
            print('Do not divide by zero')

def secure_password():
    """Generate Secure Password"""
    length = int(input("Enter length > "))
    uppers = int(input("Enter uppers > "))
    lowers = int(input("Enter lowers > "))
    numbers = int(input("Enter numbers > "))
    specials = int(input("Enter specials > "))
    if length < uppers + lowers + numbers + specials:
        print("Length is shorter than requirements")
        return

    alphabet = string.ascii_letters + string.digits +string.punctuation
    while True:
        password = "".join(secrets.choice(alphabet) for i in range(length))
        if (sum(c.isupper() for c in password) >= uppers
            and sum(c.islower() for c in password) >= lowers
            and sum(c.isdigit() for c in password) >= numbers
            and punctuation_count(password) >= specials):
            break
    print(password)
    # Reference Recipes and best practices example 2: https://docs.python.org/3/library/secrets.html

def format_percent():
    """Calculate and Format a Percentage"""
    numerator = int(input("Enter numerator > "))
    denominator = int(input("Enter denominator > "))
    precision = int(input("Enter precision > "))
    percent = numerator/denominator
    percent = round(percent, precision)
    print(f"{percent}")
    # Reference Expressing a percentage example: https://docs.python.org/3/library/string.html

def days_until():
    """Days until July 4, 2025"""
    today = datetime.date.today()
    future = datetime.date(2025, 7, 4)
    diff = future - today
    print(diff.days)
    # Reference:
    # https://stackoverflow.com/questions/7628036/how-much-days-left-from-today-to-given-date

def triangle_leg():
    """Calculate the leg of a triangle"""
    # c^2 = a^2 + b^2 − 2ab cos(C)
    side_a = int(input("Enter side a > "))
    side_b = int(input("Enter side b > "))
    angle_c = math.cos(math.radians(int(input("Enter angle C > "))))

    val = 2 * side_a * side_b
    side_a = pow(side_a,2)
    side_b = pow(side_b,2)

    side_c = math.sqrt(side_a + side_b - val * angle_c)

    print(side_c)

def cylinder_volume():
    """Calculate the volume of a Right Circular Cylinder"""
    # V = (Base Area) × Height
    # Base Area = pi * r^2
    height = int(input("Enter height > "))
    radius = int(input("Enter radius > "))
    base_area = math.pi * pow(radius, 2)

    # VOLUME
    volume = base_area * height
    print(volume)

def menu_exit():
    """Exit program"""
    print("Thank you for using this program!")
    sys.exit()

def punctuation_count(check_string):
    """Check for punctuation"""
    number = 0
    for i in check_string:
        if i in string.punctuation:
            number += 1
    return number

if __name__ == "__main__":
    main()
