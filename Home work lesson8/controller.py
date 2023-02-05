import importstudent
import view


students = {
}
names = []
lessons = []


def start():
    while True:
        choise = view.choise()
        if choise == 1:
            name = importstudent.get_student()
            if name not in students:
                names.append(name)
                students[name] = {}
                for lesson in lessons:
                    students[name][lesson] = []

        elif choise == 2:
            lesson = importstudent.get_less()
            if lesson not in lessons:
                lessons.append(lesson)
                for name in names:
                    students[name][lesson] = []

        elif choise == 3:
            name, lesson, mark = importstudent.get_mark()
            students[name][lesson].append(mark)

        elif choise == 4:
            print(students)
        elif choise == 5:
            importstudent.find_student()
            print(students[name])
        elif choise == 6:
            break
