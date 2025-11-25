from datetime import datetime

class Student:
    all = []

    def __init__(self, name):
        self.name = name
        self._enrollments = []  # list of Enrollment objects
        self._grades = {}       # dictionary: enrollment -> grade
        Student.all.append(self)

    def enroll(self, enrollment):
        self._enrollments.append(enrollment)

    def add_grade(self, enrollment, grade):
        self._grades[enrollment] = grade

    # Aggregate method: count number of courses
    def course_count(self):
        return len(self._enrollments)

    # Aggregate method: average grade across all courses
    def aggregate_average_grade(self):
        if not self._grades:
            return 0  # handle no grades
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        return total_grades / num_courses


class Course:
    all = []

    def __init__(self, title):
        self.title = title
        self._enrollments = []  # list of Enrollment objects
        Course.all.append(self)

    def enroll_student(self, enrollment):
        self._enrollments.append(enrollment)

    # Aggregate method: count students in this course
    def student_count(self):
        return len(self._enrollments)


class Enrollment:
    all = []

    def __init__(self, student, course, enrollment_date=None):
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date or datetime.now()
        Enrollment.all.append(self)

        # Link back to student and course
        student.enroll(self)
        course.enroll_student(self)

    def get_enrollment_date(self):
        return self.enrollment_date

    # Aggregate method: enrollments per day (class method)
    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count
