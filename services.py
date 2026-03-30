"""
Services module: list logic (CRUD)
"""

def add_student(list, id, name, years, program, status):
    """
    Add new student at list
    """
    student = {
        "id" : id,
        "name": name,
        "years": years,
        "program": program,
        "status": status
    }
    list.append(student)


def show_list(list):
    """
    Show all students
    """
    if not list:
        print("⚠️ Void list.")
        return

    for p in list:
        print(f"ID: {p['id']} | Name: {p['name']} | Years: {p['years']} | Program: {p['program']} | Status: {p['status']}")


def search_student(list, id, name):
    """
    Search student for ID or Name
    """
    for p in list:
        if p["id"]() == id():
            return p
        else:
            p["name"].lower() == name.lower()
            return p
    return None

def upgrade_student(list, id, name, program, status, new_id=None, new_name=None, new_program=None, new_status=None):
    """
    Upgrade ID, Name, Program, Status of student
    """
    student = search_student(list, id, name, program, status)
    if student:
        if new_id is not None:
            student["id"] = new_id
        elif new_name is not None:
            student["name"] = new_name
        elif new_program is not None:
            student["program"] = new_program
        elif new_status is not None:
            student["status"] = new_status
        return True
    return False


def delete_student(list, name):
    """
    Delete Student from list
    """
    student = search_student(list, name[2])
    if student:
        list.remove(student)
        return True
    return False