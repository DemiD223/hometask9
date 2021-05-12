from func_logic import phonebook

if __name__ == '__main__':

    phonebook("contacts.json")

    # while True:
    #     user_input = input(lang.MSG_CHOOSE)
    #
    #     if user_input == "9":
    #         cl = chose_language()
    #         if cl == "ENG":
    #             import language_ENG as lang
    #         else:
    #             import language_RU as lang
    #         print(f"You chose a {cl}", lang.MSG_CHOOSE)
"""
Extend Phonebook application

Functionality of Phonebook application:

Add new entries
Search by first name
Search by last name
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program
The first argument to the application should be the name of the phonebook.
Application should load JSON data, if it is present in the folder with application, else raise an error.
After the user exits, all data should be saved to loaded JSON.
"""
