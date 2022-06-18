class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def average_rate(self):
        average_rate_list = []
        for key, value in self.grades.items():
            average_rate_list += value
        mean = round((sum(average_rate_list) / len(average_rate_list)), 1)
        return mean


    def __str__(self):
        return f"""\nИмя: {self.name} 
             Фамилия: {self.surname}
             # Средняя оценка за домашние задания: {self.average_rate()}
             Курсы в процессе изучения: {self.courses_in_progress}
             Завершенные курсы: {self.finished_courses} """


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.average_rate() < other.average_feedback()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}


    def average_feedback(self):
        average_feedback_list = []
        for key, value in self.grades.items():
            average_feedback_list += value
        mean = round((sum(average_feedback_list) / len(average_feedback_list)), 1)
        return mean


    def __str__(self):
        return f"""\nИмя: {self.name} 
             Фамилия: {self.surname}
             Средняя оценка за лекции: {self.average_feedback()}"""


class Reviewer(Mentor):
    pass


    def __str__(self):
        return f"""\nИмя: {self.name} 
             Фамилия: {self.surname}"""


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def average_rating_students(course, *students):
    list1 = []
    for student in students:
        if student.grades.get(course):
            list1.extend(student.grades[course])
    return round(sum(list1) / len(list1), 1)

def average_rating_lecturers(course, *lecturers):
    list1 = []
    for lecturer in lecturers:
        if lecturer.grades.get(course):
            list1.extend(lecturer.grades[course])
    return round(sum(list1) / len(list1), 1)


good_student = Student('Harry', 'Potter', 'male')
good_student.courses_in_progress += ['Java', 'Python', 'C#']
good_student.finished_courses += ['C++']

best_student = Student('Hermione', 'Granger', 'female')
best_student.courses_in_progress += ['Java', 'Python', 'Git', 'C++']
best_student.finished_courses += ['C#', 'Ruby']

cool_mentor = Reviewer('Albus', 'Dumbledore')
cool_mentor.courses_attached += ['Python', 'Java', 'Git', 'Ruby', 'C++']

black_mentor = Reviewer('Severus', 'Snape')
black_mentor.courses_attached += ['C#']

cool_mentor.rate_hw(good_student, 'Python', 8)
cool_mentor.rate_hw(good_student, 'C++', 7)
black_mentor.rate_hw(good_student, 'C#', 8)

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Git', 10)
cool_mentor.rate_hw(best_student, 'Java', 10)
black_mentor.rate_hw(best_student, 'C#', 10)

print(good_student.grades)
print(best_student.grades)

best_lecturer = Lecturer('Minerva', 'McGonagall')
best_lecturer.courses_attached += ['Java', 'Python', 'C++']

good_lecturer = Lecturer('Madam', 'Trick')
good_lecturer.courses_attached += ['C#', 'Ruby', 'Git']

good_student.rate_lect(best_lecturer, 'Java', 8)
good_student.rate_lect(best_lecturer, 'C++', 9)
best_student.rate_lect(best_lecturer, 'Python', 10)

good_student.rate_lect(good_lecturer, 'C#', 6)
good_student.rate_lect(good_lecturer, 'Git', 9)
best_student.rate_lect(good_lecturer, 'Ruby', 10)

print(best_lecturer.grades)
print(good_lecturer.grades)

print(f'Проверяющий: {cool_mentor}')
print(f'Лектор: {best_lecturer}')
print(f'Студент: {good_student}')
print(f'Студент: {best_student}')

print(good_student < best_lecturer)
course = 'C#'
print(average_rating_students(course, good_student, best_student))
print(average_rating_lecturers(course, best_lecturer, good_lecturer))

