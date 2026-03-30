"""
Persistence module: manage CVS files
"""

import csv


def save_csv(list, path, add_header=True):
    """
    Manually save list in CSV file
    """
    if not list:
        print("⚠️ I don't have data yet to save.")
        return

    try:
        with open(path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if add_header:
                writer.writerow(["id", "name", "years", "program", "status"])

            for p in list:
                writer.writerow([p["id"],p["name"], p["years"], p["program"], p["status"]])

        print(f"✅ Save list in: {path}")

    except Exception as e:
        print(f"❌ Error to save file: {e}")


def auto_save_csv(list, path):
    """
    Auto save list (uso interno del sistema)
    """
    try:
        with open(path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(["id", "name", "years", "program", "status"])

            for p in list:
                writer.writerow([p["id"],p["name"], p["years"], p["program"], p["status"]])

    except Exception as e:
        print(f"❌ Auto save error: {e}")


def load_csv(path):
    """
    Load list from CSV with validation
    """
    list = []
    mistakes = 0

    try:
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)

            if header != ["id", "name", "years", "program", "status"]:
                print("❌ Invalid header.")
                return [], 0

            for row in reader:
                try:
                    if len(row) != 3:
                        raise ValueError
                    
                    id = row[0]
                    name = row[1]
                    years = int(row[2])
                    program = row[3]
                    status = bool(row[4])

                    if id < 0 or years < 0:
                        raise ValueError

                    list.append({
                        "id": id,
                        "name": name,
                        "years": years,
                        "program": program,
                        "status": status,
                    })

                except:
                    mistakes += 1

        return list, mistakes

    except FileNotFoundError:
        return [], 0
    except UnicodeDecodeError:
        print("❌ Coding Error.")
    except Exception as e:
        print(f"❌ Error: {e}")

    return [], 0