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


good_student = Student('Harry', 'Potter', 'male')
good_student.courses_in_progress += ['Java', 'Python']
good_student.finished_courses += ['C++']


cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Java']

cool_mentor.rate_hw(good_student, 'Python', 10)
cool_mentor.rate_hw(good_student, 'Python', 10)
cool_mentor.rate_hw(good_student, 'Java', 9)

print(good_student.grades)

best_lecturer = Lecturer('Minerva', 'McGonagall')
best_lecturer.courses_attached += ['Java', 'Python']

good_student.rate_lect(best_lecturer, 'Java', 8)
good_student.rate_lect(best_lecturer, 'Python', 9)
good_student.rate_lect(best_lecturer, 'Python', 10)

print(best_lecturer.grades)

print(f'Проверяющий: {cool_mentor}')
print(f'Лектор: {best_lecturer}')
print(f'Студент: {good_student}')

print(good_student < best_lecturer)

