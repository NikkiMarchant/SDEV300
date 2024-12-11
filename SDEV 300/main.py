"""Week 1 discussion 1. Nicole Marchant.
The program asks user if they like anime if yes ask a followup question."""


def main():
    """This is the main function of the program."""
    print("Do you watch anime?")


    checkadc = adc(1, 1)
    print(checkadc)
    answer = input('Enter yes or no:')
    if answer.lower() == "yes":
        response = input('What is your favorite?')
        print(f'{response} is a great choice')
    elif answer.lower() == "no":
        print('Thank you for your time.')
    else:
        print('Please enter yes or no.')


def adc(a, b):
    return a+b


if __name__ == "__main__":
    main()
