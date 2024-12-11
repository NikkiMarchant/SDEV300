"""Lab3. Nicole Marchant. This is a state lookup module."""
import os
import sys
# import subprocess

from matplotlib import pyplot
from PIL import Image
import numpy

class State():
    """List the states and their capital, population, and flower"""
    def __init__(self, name, capital, population, flower):
        self.name = name
        self.capital = capital
        self.population = population
        self.flower = flower

    def dummy(self):
        """Dummy function for pylint"""

    def __str__(self):
        return f"{self.name}\n" \
               f"\tCapital: {self.capital}\n" \
               f"\tPopulation: {self.population}\n" \
               f"\tFlower: {self.flower}"

us_state_to_abbrev = {
    "alabama": State("Alabama", "Montgomery", 5108468, "Camellia"),
    "alaska": State("Alaska", "Juneau", 733391, "Forget-me-not"),
    "arizona": State("Arizona", "Phoenix", 7151502, "Saguaro cactus blossoms"),
    "arkansas": State("Aekansas", "Little Rock", 3011524, "Apple blossom"),
    "california": State("California", "Sacramento", 38940231, "California poppy"),
    "colorado": State("Colorado", "Denver", 5877610, "Colorado blue columbine"),
    "connecticut": State("Connecticut","Hartford", 3605944, "Mountain laurel"),
    "delaware": State("Delaware", "Dover", 1031890, "Peach blossom"),
    "florida": State("Florida", "Tallahassee", 22610726, "Orange blossom"),
    "georgia": State("Georgia", "Atlanta", 11029227, "Azalea"),
    "hawaii": State("Hawaii", "Honolulu", 1452771, "Hawaiian hibiscus"),
    "idaho": State("Idaho", "Boise", 1964726, "Syringa, mock orange"),
    "illinois": State("Illinios", "Springfield", 12812508, "Violet"),
    "indiana": State("Indiana", "Indianapolis", 6785528, "Peony"),
    "iowa": State("Iowa", "Des Moines", 3190369, "Wild Rose"),
    "kansas": State("Kansas", "Topeka", 2940865, "Sunflower"),
    "kentucky": State("Kentucky", "Frankfort", 4505836, "Goldenrod"),
    "louisiana": State("Louisiana", "Baton Rouge", 4657757, "Magnolia"),
    "maine": State("Maine", "Augusta", 1362359, "White pine cone and tassel"),
    "maryland": State("Maryland", "Annapolis", 6177224, "Black-eyed susan"),
    "massachusetts": State("Massachusetts", "Boston", 7001399, "Mayflower"),
    "michigan": State("Michigan", "Lansing", 10077331, "Apple blossom"),
    "minnesota": State("Minnesota", "Saint Paul", 5737915, "Pink and white lady's slipper"),
    "mississippi": State("Mississippi", "Jackson", 2963914, "Magnolia"),
    "missouri": State("Missouri", "Jefferson City", 6160281, "Hawthorn"),
    "montana": State("Montana", "Helena", 1122867, "Bitterroot"),
    "nebraska": State("Nebraska", "Lincoln", 1961504, "Goldenrod"),
    "nevada": State("Nevada", "Carson City", 3104614, "Sagebrush"),
    "new hampshire": State("New Hampshire", "Concord", 1402054, "Purple lilac"),
    "new jersey": State("New Jersey", "Trenton", 9288994, "Violet"),
    "new mexico": State("New Mexico", "Santa Fe", 2117522, "Yucca flower"),
    "new york": State("New York", "Albany", 19571216, "Rose"),
    "north carolina": State("North Carolina", "Raleigh", 10439388, "Flowering dogwood"),
    "north dakota": State("North Dakota", "Bismarck", 779179, "Wild prairie rose"),
    "ohio": State("Ohio", "Columbus", 11780017, "Scarlet carnation"),
    "oklahoma": State("Oklahoma", "Oklahoma City", 4053824, "Oklahoma rose"),
    "oregon": State("Oregon", "Salem", 4233358, "Oregon grape"),
    "pennsylvania": State("Pennsylvania", "Harrisburg", 13002700, "Mountain laurel"),
    "rhode island": State("Rhode Island", "Providence", 1098163, "Violet"),
    "south carolina": State("South Carolina", "Columbia", 5118425, "Yellow jessamine"),
    "south dakota": State("South Dakota", "Pierre", 909824, "Pasque flower"),
    "tennessee": State("Tennessee", "Nashville", 7126489, "Iris"),
    "texas": State("Texas", "Austin", 30503301, "Bluebonnet sp"),
    "utah": State("Utah", "Salt Lake City", 3271616, "Sego lily"),
    "vermont": State("Vermont", "Montpelier", 647464, "Red clover"),
    "virginia": State("Virginia", "Richmond", 8715698, "American dogwood"),
    "washington": State("Washington", "Olympia", 7812880, "Coast rhododendron"),
    "west virginia": State("West Virginia", "Charleston", 1793716, "Rhododendron"),
    "wisconsin": State("Wisconsin", "Madison", 5893718, "Wood violet"),
    "wyoming": State("Wyoming", "Cheyenne", 576851, "Indian paintbrush")
}

def main():
    """Main function """
    lab3_menu = {1 : alphabetical_all,
                 2 : specific,
                 3 : bar_graph,
                 4 : update_population,
                 5 : menu_exit}

    while True:
        print("U.S. State Information")
        print("1. Display States alphabetically with capital, population, and image of flower")
        print("2. Search for specific state with capital, population, and image of flower")
        print("3. Display Bar graph of top 5 populated states and overall population")
        print("4. Update state population for a specific state")
        print("5. Exit program")
        try:
            choice = int(input("> "))
            lab3_menu.get(choice)()
        except (TypeError, ValueError):
            print("Invalid input")
        except KeyboardInterrupt:
            menu_exit()


def alphabetical_all():
    """List states in alphabetical order"""
    for item in us_state_to_abbrev:
        print(us_state_to_abbrev.get(item))

def specific():
    """Displays a specific states information"""
    while True:
        try:
            print("Choose a State or exit")
            choice = input("> ").lower()
        except (TypeError, ValueError):
            print("Invalid input")
        except KeyboardInterrupt:
            menu_exit()
        if choice in us_state_to_abbrev:
            print(us_state_to_abbrev.get(choice))
            open_image(us_state_to_abbrev.get(choice).flower)
            return
        if choice == "exit":
            return

def bar_graph():
    """disolays state populations on a bar graph"""
    state_list = []
    for key in us_state_to_abbrev:
        state_list.append([us_state_to_abbrev.get(key).name,
                           us_state_to_abbrev.get(key).population])
    state_list.sort(reverse = True, key = lambda x: x[1])
    state_names = []
    state_pop = []
    for item in state_list[:5]:
        state_names.append(item[0])
        state_pop.append(item[1])
    pyplot.figure(figsize=(10,7))
    pyplot.bar(state_names, state_pop)
    pyplot.ylabel("Population (10 millions)")
    pyplot.title("Top Five Populated States")
    pyplot.show()

def update_population():
    """Updates the population of the state"""
    while True:
        try:
            print("Choose a State or exit")
            choice = input("> ").lower()
        except (TypeError, ValueError):
            print("Invalid input")
        except KeyboardInterrupt:
            menu_exit()
        if choice in us_state_to_abbrev:
            print("Set new value")
            value = int(input("> "))
            us_state_to_abbrev.get(choice).population = value
            print(us_state_to_abbrev.get(choice))
            return
        if choice == "exit":
            return
    return

def menu_exit():
    """Exit program"""
    print("Thank you for using this program!")
    sys.exit()

def open_image(file_name):
    """Calls and opens image of state flower"""
    flower = os.getcwd() + "\\state_flowers\\"
    file_name = file_name + ".jpg"
    if not os.path.exists(flower):
        print("Missing state_flower folder in Current Working Directory")
        return
    if not os.path.isfile(flower + file_name):
        print(f"Missing file: {file_name} in {flower} directory")
        return
    image = numpy.asarray(Image.open(flower + file_name))
    pyplot.imshow(image)
    pyplot.axis('off')
    pyplot.show()
    # subprocess.call(flower + file_name, shell=True)
    # os.startfile(flower + file_name)

if __name__ == '__main__':
    main()
