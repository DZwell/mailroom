
names = {'Will store donor names in here.': ['donations here']}


def opening_screen():
    """Return function call to next step in program"""
    print("This will welcome the user to the program.")
    user_input = input()

    if user_input == send_thank_you:
        return send_thank_you()
    elif user_input == create_report:
        return create_report()
    elif user_input == 'q':
        quit


def send_thank_you():
    full_name = input('Prompt user for full name')
    donation = input("Prompt user for donation")
            assert is int

        #Use names.setdefault(full_name, []).append(donation)
        #Instead of if/elif block
    if full_name not in names:
        names.update({full_name: [donation]})
    elif full_name in names:
        names[full_name].append(donation)
    elif full_name == 'q':
        quit
    print("Donor letter using .format with name and donation")


def create_report():
    print("names dict in a formatted way")
    user_input = input("go back to previous screen or quit")
    if user_input == 'q':
        quit




