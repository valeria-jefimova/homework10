from functions import *

if __name__ == '__main__':

    pc_input = int(input("Введите номер студента\n"))
    # получить ввод pk пользователя (student - множество навыков студента)
    student, student_name = get_student_by_pk(pc_input)

    title = input(f"Выберите специальность для оценки студента {student_name}\n")
    # Получите ввод title профессии
    profession = get_profession_by_title(title)

    # Если да – получите соответствие с помощью check_fitness
    # Если нет – завершитесь

    selection_result = check_fitness(student, profession)
    print(f"Пригодность {selection_result['fit_percent']}%")
    print(f"{student_name} знает {' '.join(selection_result['has'])}")
    print(f"{student_name} не знает {' '.join(selection_result['lacks'])}")