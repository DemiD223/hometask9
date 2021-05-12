from typing import Dict, List
import json
import lang.language_ENG as lang


def phonebook(filename: str):
    global lang

    while True:
        show_menu()
        user_input = input(lang.MSG_CHOOSE)

        if user_input == "1":
            add_contact(filename)

        elif user_input == "2":
            search_menu(filename)

        elif user_input == "9":
            cl = chose_language()
            if cl == '1':
                import lang.language_ENG as lang
            elif cl == '2':
                import lang.language_RU as lang

        elif user_input == "0":
            break


def show_menu():
    print(f"{lang.MSG_ADD}\t{lang.MSG_SEARCH}\n"
          f"{lang.MSG_CHANGE_LANG}\t{lang.MSG_EXIT}")


def chose_language():
    show_lang_var()
    return input(lang.MSG_CHOOSE)


def show_lang_var():
    print(lang.MSG_ENGLISH, lang.MSG_RUSSIAN)


def save_phonebook(data: List[Dict], filename: str):
    with open(filename, 'w') as fw:
        json.dump(data, fw)
    print(lang.MSG_SUCCS_SAVE)


def get_phonebook(filename) -> List[Dict]:
    try:
        with open(filename, 'r') as fr:
            print("Open and read")
            return json.load(fr)

    except:
        print("dont open")
        return []


def get_fname() -> str:
    return input(lang.MSG_GET_FIRST_NAME)


def get_lname() -> str:
    return input(lang.MSG_GET_LAST_NAME)


def get_phnumber() -> str:
    return input(lang.MSG_GET_PHONE_NUMBER)


def get_city() -> str:
    return input(lang.MSG_GET_CITY)


def add_contact(filename):
    contacts = get_phonebook(filename)
    contacts.append({"First name": get_fname(),
                     "Last name": get_lname(),
                     "Phone number": get_phnumber(),
                     "City": get_city()})
    save_phonebook(contacts, filename)


def search_menu(filename):
    while True:
        rez = None
        print(lang.MSG_SEARCH_VAR)
        key_search = input(lang.MSG_CHOOSE)
        if key_search == '0':
            break
        elif key_search == '1':
            rez = searchbyfname(get_fname(), filename)
        elif key_search == '2':
            rez = searchbylname(get_lname(), filename)
        elif key_search == '3':
            rez = searchbypnumber(get_phnumber(), filename)
        elif key_search == '4':
            rez = searchbycity(get_city(), filename)
        else:
            print(lang.MSG_ERROR_KEY)

        if rez is not []:
            for i, contact in enumerate(rez):
                print(f"{i + 1}. - {contact}")
            user_input = input(lang.MSG_NO_SUITABLE)
            if not user_input.isdigit():
                print("not digit")
                break
            elif user_input == "0" or int(user_input) not in range(1, len(rez) + 1):
                print("out of len")
                break
            else:
                print(rez[int(user_input) - 1])
                user_input2 = input(lang.MSG_OPERATIONS)

                if not user_input2.isdigit() or user_input == '0':
                    break
                elif user_input2 == '1':
                    update_contact(rez[int(user_input) - 1], filename)
                elif user_input2 == '2':
                    delete_contact(rez[int(user_input) - 1], filename)
                else:
                    break


def __search(key, val, filename) -> List[Dict]:
    contancts = get_phonebook(filename)
    rez = []
    for contanct in contancts:
        if val.lower() in contanct.get(key).lower():
            rez.append(contanct)
    return rez


def searchbyfname(val, filename) -> List[Dict]:
    return __search("First name", val, filename)


def searchbylname(val, filename) -> List[Dict]:
    return __search("Last name", val, filename)


def searchbypnumber(val, filename) -> List[Dict]:
    return __search("Phone number", val, filename)


def searchbycity(val, filename) -> List[Dict]:
    return __search("City", val, filename)


def update_contact(contact: Dict, filename: str):
    contacts = get_phonebook(filename)
    contacts.pop(contacts.index(contact))

    while True:
        print(contact)
        print(lang.MSG_CHOOSE_INFO_UPDATE)
        user_input = input(lang.MSG_CHOOSE)
        if user_input == '1':
            contact["First name"] = get_fname()
        elif user_input == '2':
            contact["Last name"] = get_lname()
        elif user_input == '3':
            contact["Phone number"] = get_phnumber()
        elif user_input == '4':
            contact["City"] = get_city()
        elif user_input == '0':
            break
        else:
            continue

        contacts.append(contact)
        save_phonebook(contacts, filename)


def delete_contact(contact: Dict, filename: str):
    contacts = get_phonebook(filename)
    contacts.pop(contacts.index(contact))
    save_phonebook(contacts, filename)
