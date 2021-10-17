class Student:  # Студенты
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.sum_grade = 0  #Куда будет записывать средняя

    def student_grades(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lec:
                lecturer.grades_lec[course] += [grade]
            else:
                lecturer.grades_lec[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):  # то, что будтет напечатано
        self.calculate_average()
        # self.progress_crs = '' Убираем кавычки
        # for self.courses_in_progress in self.courses_in_progress:
        #     self.progress_crs += self.courses_in_progress
        progress_crs = ', '.join(self.courses_in_progress) #Тоже самое, убираем кавычки ставим пробел и запятую

        # self.fin_courses = ''
        # for self.finished_courses in self.finished_courses:
        #     self.fin_courses += self.finished_courses
        fin_courses = ', '.join(self.finished_courses)

        return 'Студент: \nИмя: ' + self.name + '\nФамилия: ' + self.surname + \
               '\nСредняя оценка за лекции: ' + str(round(self.sum_grade, 1)) \
               + '\nКурсы в процессе изучения: ' + progress_crs \
               + '\nЗавершенные курсы: ' + fin_courses

    def calculate_average(self): #Подсчет ср. оцен.
        all_gr = []
        for value in self.grades.values():
            for grade in value:
                all_gr.append(grade)
        self.sum_grade = sum(all_gr) / len(all_gr)
        # print(all_gr)

    def __gt__(self, other): #Сравнение
        return self.sum_grade > other.sum_grade


class Mentor:  # Настваники
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):  # Лекторы наследуют у менторов имя и фамилию
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades_lec = {}
        self.sum_grade = 0

    def __str__(self):  # то, что будтет напечатано
        sum_grades = 0
        for sum_grades in self.grades_lec.values():
            sum_grades = sum(sum_grades) / len(sum_grades)
        return 'Лектор: \nИмя: ' + self.name + '\nФамилия: ' + self.surname + \
               '\nСредняя оценка за лекции: ' + str(round(sum_grades, 1))  # Средняя оценка у лекторов за лекцию

    def calculate_average(self):
        all_gr = []
        for value in self.grades_lec.values():
            for grade in value:
                all_gr.append(grade)
        self.sum_grade = sum(all_gr) / len(all_gr)
        # print(all_gr)

    def __gt__(self, other): #метод сравнениия gt (>) lt (<)
        return self.sum_grade > other.sum_grade


class Reviewer(Mentor):  # Проверяющие
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):  # то, что будет напечатано
        return 'Проверяющий: \nИмя: ' + self.name + '\nФамилия: ' + self.surname


# Студенты
student_1 = Student('Григгорий', 'Вечный', 'м')  # Студент
student_1.courses_in_progress += ['JS', 'GIT']  # Курсы заполнять через ", пробле " уж не надо, смотри строку 20
student_1.finished_courses += ['Введение в программирование']

student_1_1 = Student('Григгорий', 'Дуб', 'м')  # Студент
student_1_1.courses_in_progress += ['JS', 'GIT']  # Курсы заполнять через ", пробле "
student_1_1.finished_courses += ['Введение в программирование']

student_2 = Student('Ольга', 'Вечная', 'ж')  # Студент
student_2.courses_in_progress += ['С++']
student_2.finished_courses += ['Введение в программирование']

# Лекторы
lec_1 = Lecturer('Виталий', 'Богомолов')  # Лекторы
lec_1.courses_attached += ['JS']

lec_1_1 = Lecturer('Жан', 'Батист')  # Лекторы
lec_1_1.courses_attached += ['JS']

lec_2 = Lecturer('Игнат', 'Богомолов')  # Лекторы
lec_2.courses_attached += ['С++']

# #Проверяющие
rev_1 = Reviewer('Виталий', 'Оболонский')  # Проверяющие
rev_1.courses_attached += ['JS']  # Курсы

rev_2 = Reviewer('Максим', 'Суббота')  # Проверяющие
rev_2.courses_attached += ['С++']

#Проверяющие ставят оценнки студнтам
rev_1.rate_hw(student_1, 'JS', 8)
rev_1.rate_hw(student_1, 'JS', 8)
rev_1.rate_hw(student_1, 'JS', 8)

rev_1.rate_hw(student_1_1, 'JS', 10)
rev_1.rate_hw(student_1_1, 'JS', 10)
rev_1.rate_hw(student_1_1, 'JS', 10)

rev_2.rate_hw(student_2, 'С++', 9)
rev_2.rate_hw(student_2, 'С++', 9)
rev_2.rate_hw(student_2, 'С++', 9)

#Студенты ставят оценки лекторам
student_1.student_grades(lec_1, 'JS', 10)
student_1.student_grades(lec_1, 'JS', 9)
student_1.student_grades(lec_1, 'JS', 8)

student_1_1.student_grades(lec_1_1, 'JS', 8)
student_1_1.student_grades(lec_1_1, 'JS', 8)
student_1_1.student_grades(lec_1_1, 'JS', 8)

student_2.student_grades(lec_2, 'С++', 10)
student_2.student_grades(lec_2, 'С++', 10)
student_2.student_grades(lec_2, 'С++', 10)


# print(f'Лектор: {lec_1_1.name} {lec_1_1.surname} {lec_1_1.grades_lec}')
# print()
# print(rev_1)   #Проверяющие
# print()
# print(lec_1)  #Лекторы
# print()
# print(student_1)  #Студенты
# print()
# print(student_2)

# print(f'Студент: {student_2.name} {student_2.surname} {student_2.grades}')

# student_1.calculate_average()  # мы вызываем этот метод, можно не принтовать его самого
# student_2.calculate_average()
#
# lec_1.calculate_average()  #Вызываем подсчёт оценок у Виталия
# lec_2.calculate_average() #Вызываем подсчёт оценок у Игната
#
# print(student_1 < student_2)
# print(lec_1 > lec_2)

students_list = [student_1, student_1_1]
def calculate_average_students(student_list, course):
    total = []
    all_grades = 0
    for i in student_list:
        if course in i.grades.keys():
            total.extend(i.grades[course])
            sum_grades = sum(total)
            len_grades = len(total)
            all_grades = sum_grades / len_grades
    print(f'Средняя оценка всех студентов по курсу {course}: {all_grades}')

calculate_average_students(students_list, 'JS')


lec_list = [lec_1, lec_1_1]
def calculate_average_lec(lec_list, course):
    total = []
    all_grades = 0
    for i in lec_list:
        if course in i.grades_lec.keys():
            total.extend(i.grades_lec[course])
            sum_grades_1 = sum(total)
            len_grades_1 = len(total)
            all_grades = sum_grades_1 / len_grades_1
    print(f'Средняя оценка всех лекторов по курсу {course}: {all_grades}')

calculate_average_lec(lec_list, 'JS')