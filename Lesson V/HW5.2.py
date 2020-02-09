"""
Разработать класс Student для представления сведений об успешности слушателя некого
курса. Объект класса должен содержать поля для сохранения имени студента и баллов,
полученных им за выполнение практических заданий и финального экзамена.
"""


class Student(object):
    def __init__(self, name, args={}):
        self.name = name
        self.args = args.copy()

    def make_lab(self, m,n):
        try:
            if m > self.args[2]:
                raise IndexError
        except IndexError:
            return self

    def make_exam(self, m):
        return self

    def is_certified(self):
        return tuple




conf = {"exam_max":30, "lab_max":7, "lab_num":10, "k": 0.61}
STUDENT_1 = Student("Tom", conf)