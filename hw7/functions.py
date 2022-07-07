import json


def load_students() -> list:
    """Загружает студентов из файла в список"""
    with open("students.json", "r") as read_file:
        st = json.load(read_file)
    return st


def load_professions() -> list:
    '''Загружает навыки из файла в список'''
    with open("professions.json", "r") as read_file:
        pr = json.load(read_file)
    return pr


def get_student_by_pk(pk):
    '''Получает словарь с данными студента по его pk'''
    students = load_students()
    for student in students:
        if int(student["pk"]) == pk:
            print(f"Студент {student['full_name']}\nЗнает {' '.join(student['skills'])}")
            return set(student["skills"]), student['full_name']
    print("У нас нет такого студента")
    quit()


def get_profession_by_title(title):
    '''Получает словарь с инфо о профессии по названию'''
    professions = load_professions()
    for profession in professions:
        if profession["title"] == title.title():
            return set(profession["skills"])
    print("У нас нет такой специальности")
    quit()


def check_fitness(students: set, professions: set):
    '''Функция, которая получив студента и профессию, возвращала бы словарь типа'''
    # Эта функция должна использовать методы множеств
    has_skills = professions.intersection(students)
    lacks_skills = professions.difference(students)
    fit_percent = round(len(has_skills) / len(professions) * 100)
    return {"has": has_skills, "lacks": lacks_skills, "fit_percent": fit_percent}