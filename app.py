from services import *
from archives import *

PATH_CSV = "list.csv"

# ================= VALIDATIONS =================

control = True

def val_string(msg):
    while control:
        val = input(msg)
        if val.strip():
            return val
        print("Error: invalid valor (Only Letters entrance)")

def val_int(msg):
    while control:
        try:
            val = int(input(msg))
            if val != 0 or val >= 0:
                return val
        except:
            pass
        print("Error: invalid valor (Only Numeric entrance)")

def val_bool(msg):
    while control:
        try:
            val = int(input(msg))
            if isinstance(val, int):
                return val
            else:
                return False
        except:
            pass
        print("Error: invalid valor (only letters entrance)")


# ================= MENU =================

def menu():
    print("\n--- Student List ---")
    print("1. Create Student")
    print("2. Search List")
    print("3. Search Student")
    print("4. Upgrade Info")
    print("5. Delete Student")
    print("6. Save CSV")
    print("7. Load CSV")
    print("8. Exit")


def main():
    # 🔹 Auto load on startup
    list, _ = load_csv(PATH_CSV)

    control = True

    while control:
        menu()
        op = input("Option: ")

        if op == "1":
            id=val_int("ID: ")
            name = val_string("Name: ")
            years = val_int("Years: ")
            program = val_string("Program: ")
            status =val_bool("Status: ")
            add_student(list, id, name, years, program, status)
            auto_save_csv(list, PATH_CSV)

        elif op == "2":
            stats=show_list(list)
            if stats:
                print(stats)
            else:
                print('Void data')

        elif op == "3":
            name = val_string("Search with ID or Name: ")
            p = search_student(list, id, name)
            print(p if p else "No data found")

        elif op == "4":
            id = val_int("ID: ")
            name = val_string("Name: ")
            years = val_int("Years: ")
            program = val_string("Program: ")
            status = val_bool("Status: ")
            
            if upgrade_student(list, id, name, years, program, status):
                auto_save_csv(list, PATH_CSV)
                print("Upgrade")
            else:
                print("No data found")

        elif op == "5":
            name = val_string("Delete Student: ")
            if delete_student(list, name):
                auto_save_csv(list, PATH_CSV)
                print("Deleted info")
            else:
                print("No data found")

        elif op == "6":
            path = input("File path: ")
            save_csv(list, path)

        elif op == "7":
            path = input("File path: ")
            news, mistakes = load_csv(path)

            if news:
                decision = input("Overwrite inventory? (Y/N): ").lower()

                if decision == "y":
                    list = news
                else:
                    for new in news:
                        exist = search_student(list, new["name"])
                        if exist:
                            exist["id"] += new["id"]
                        else:
                            list.append(new)

                auto_save_csv(list, PATH_CSV)
                print(f"Invalid rows: {mistakes}")

        elif op == "8":
            control = False

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()