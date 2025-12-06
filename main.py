from inmemory_db import InMemoryDB

def print_main_menu():
    MAIN_MENU_OPTIONS = [
        "Get",
        "Put",
        "Begin Transaction",
        "Commit",
        "Rollback",
        "Exit",
    ]

    print("\nOptions:")
    for i, option in enumerate(MAIN_MENU_OPTIONS):
        print(f"{i + 1}. {option}")

    print("")
    choice = input("Choice: ")
    print("")
    return choice

def main():
    imdb = InMemoryDB()
    choice = print_main_menu()
    exit_choice = "6"

    while choice != exit_choice:
        if choice == "1":
            k = input("Key: ")
            x = imdb.get(k)
            if x:
                print("Account Balance:", x)
            else:
                print("No account with this key.")
        elif choice == "2":
            k = input("Key: ")
            v = int(input("Val: "))
            imdb.put(k,v)
            print("Temporarily put", v, "in account", k)
        elif choice == "3":
            imdb.begin_transaction()
            print("Began transaction.")
        elif choice == "4":
            imdb.commit()
            print("Commit made.")
        elif choice == "5":
            imdb.rollback()
            print("Temporary changes rolled back.")
        elif choice == "6":
            break
        else:
            print("Choice unrecognised")

        print("---------------------------")
        choice = print_main_menu()

    print("Goodbye!\n")

if __name__ == "__main__":
    main()