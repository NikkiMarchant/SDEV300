"""Lab1. Nicole Marchant. This is a voter registration module."""
import re
import sys

def main():
    """This is the main flow control """
    print('Welcome to the Python Voter Registration Application. '\
          'You can cancel registration at any time by typing exit.')

    answer = input ('Do you want to continue with Voter Registration? ')

    if answer.lower() != 'yes':
        print('Thank you for your time.')
        return

    # https://www.w3schools.com/python/python_regex.asp
    # used regular expression for string validation
    fname = validate('What is your first name? ', r'^[a-zA-z]+$')

    lname = validate('What is your last name? ', r'^[a-zA-z]+$')

    # gets age and verifies range
    while True:
        try:
            age = input('What is your age? ')
            if age == 'exit':
                return
            if int(age) < 18:
                return
            if int(age) >= 120:
                continue
            break
        except ValueError:
            continue

    country = input("Are you a U.S. Citizen? ")
    if country.lower() != "yes":
        return

    # list of states for verifing valid state
    states = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA",
              "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO",
              "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK",
              "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI",
              "WV", "WY"]

    state = "state "
    while state.upper() not in states:
        state = input("What state do you live in? ")
        if state == 'exit':
            return

    # https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch04s14.html
    # regular expression from O'Reilly for validating zipcodes
    zip_code = validate("What is your zipcode? ", r'^[0-9]{5}(?:-[0-9]{4})?$')

    print('Thanks for registering to vote. Here is the information we received:')
    print(f'Name(first, last): {fname} {lname}')
    print(f'Age: {age}')
    print(f'U.S. Citizen: {country}')
    print(f'State: {state}')
    print(f'Zipcode: {zip_code}')
    print('Thank you for trying the Voter Registration Application. ' \
          'Your voter registration card should be shipped within 3 weeks.')

    return

def validate(question, reg_ex):
    """Prompts for user input and validates using regular expression"""
    invalid = True
    while invalid:
        answer = input(question)
        if answer == 'exit':
            sys.exit()
        if re.search(reg_ex, answer):
            break

    return answer

if __name__ == "__main__":
    main()
