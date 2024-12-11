"""Lab5. Nicole Marchant. This is a data analysis module."""
import csv
import sys
import statistics
from matplotlib import pyplot

def main():
    """Main function"""
    print('Welcome to the Python Data Analysis App. ')

    lab5_menu = {1: population_data,
                 2: housing_data,
                 3: menu_exit}

    while True:
        print('Select the file you want to analyze: ')
        print('1. Population Data')
        print('2. Housing Data')
        print('3. Exit the program')
        try:
            choice = int(input("> "))
            lab5_menu.get(choice)()
        except (TypeError, ValueError):
            print('Invalid Input')
        except KeyboardInterrupt:
            menu_exit()

def population_data():
    """Function for population data"""
    lab5_population = {'a': pop_apr_1,
                       'b': pop_jul_1,
                       'c': change_pop}
    while True:
        print('You have entered Population Data. '
              'Select the Column you want to analyze: ')
        print('a. Pop Apr 1')
        print('b. Pop Jul 1')
        print('c. Change Pop')
        print('d. Exit Column')
        try:
            choice = input(">")
            if choice == 'd':
                return
            lab5_population.get(choice)()
        except (TypeError, ValueError):
            print("Invalid Input")
        except KeyboardInterrupt:
            return

def col_pop(col:int):
    """access column data for month"""
    col_list = []
    print('The statistics for this column are: ')

    with open('PopChange.csv', 'r', encoding='utf-8') as pop_change:
        reader = csv.reader(pop_change)
        next(reader, None)
        for row in reader:
            col_list.append(int(row[col]))
        pop_change.close()
    print(f'Count = {len(col_list):.1f}')
    print(f'Mean = {statistics.mean(col_list):.1f}')
    print(f'Standard Deviation = {statistics.pstdev(col_list):.1f}')
    print(f'Min = {min(col_list):.1f}')
    print(f'Max = {max(col_list):.1f}')
    print('The Histogram of this column is now displayed. ')
    pyplot.hist(col_list)
    pyplot.show()

def pop_apr_1():
    """population on april 1"""
    print('You selected Apr 1. ')
    col_pop(4)

def pop_jul_1():
    """function for populaton on July 1st"""
    print('You selected Jul 1. ')
    col_pop(5)

def change_pop():
    """function for population change"""
    print('You selected Change Pop. ')
    col_pop(6)

def housing_data():
    """function for housing data"""
    lab5_housing = {'a': house_age,
                    'b': bedrooms_house,
                    'c': built_house,
                    'd': rooms_house,
                    'e': house_utility}
    while True:
        print('You have entered housing data.'
              'Please select the column you want to analyze')
        print('a. Age of the house')
        print('b. Number of Bedrooms')
        print('c. Year house was built')
        print('d. Number of Rooms')
        print('e. Utility')
        print('f. Exit Column')
        try:
            choice = input(">")
            if choice == 'f':
                return
            lab5_housing.get(choice)()
        except (TypeError, ValueError):
            print('Invalid Input')
        except KeyboardInterrupt:
            return
def col_house(col:int):
    """access coloum data for house"""
    col_list = []
    print('The statistics for this colomn are: ')

    with open('Housing.csv', 'r', encoding='utf-8') as house_lab:
        reader = csv.reader(house_lab)
        next(reader, None)
        for row in reader:
            col_list.append(float(row[col]))
        house_lab.close()
    print(f'Count = {len(col_list):.1f}')
    print(f'Mean = {statistics.mean(col_list):.1f}')
    print(f'Standard Deviation = {statistics.pstdev(col_list):.1f}')
    print(f'Min = {min(col_list):.1f}')
    print(f'Max = {max(col_list):.1f}')
    print('The Histogram of this column is now displayed. ')
    pyplot.hist(col_list)
    pyplot.show()

def house_age():
    """access column data for age"""
    print('You selected Age')
    col_house(0)

def bedrooms_house():
    """access column data for number of bedrooms"""
    print('You selected Bedrooms. ')
    col_house(1)

def built_house():
    """access column data for built"""
    print('You selected Built')
    col_house(2)

def rooms_house():
    """access column data for rooms"""
    print('You selected Rooms')
    col_house(4)

def house_utility():
    """access column data for utility"""
    print('You selected Utility')
    col_house(6)

def menu_exit():
    """Exit program"""
    print('Thanks for using the Data Analysis App. ')
    sys.exit()

if __name__ == "__main__":
    main()
