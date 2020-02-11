"""
Разработать класс Student для представления
сведений об успешности слушателя некого
курса. Объект класса должен содержать поля
для сохранения имени студента и баллов,
полученных им за выполнение практических
заданий и финального экзамена.
"""


class Student:
    """класс студент"""
    current_sum = 0
    success = False
    lub_number = {}

    def __init__(self, name, args):
        self.name = name
        self.args = args.copy()
        for i in range(self.args["lab_max"]):
            self.lub_number[i] = [3, 0]

    def make_lab(self, m, n=1):
        """сдать лабу"""
        try:
            if 0 <= n <= (self.args['lab_num'] - 1):
                if self.lub_number[n][0] != 0:
                    if m > self.args['lab_max']:
                        self.lub_number[n][1] = self.args['lab_max']
                    else:
                        self.lub_number[n][1] = m
                    self.lub_number[n][0] -= 1
                else:
                    print("количество попыток не осталось ")
            else:
                print("некорректный номер задачи")
            return self
        except ValueError:
            print(ValueError)

    def make_exam(self, m):
        """сдать экзамен"""
        try:
            if m > self.args['exam_max']:
                self.current_sum += self.args['exam_max']
            else:
                self.current_sum += m
            return self
        except ValueError:
            print(ValueError)

    def is_certified(self):
        """получить сертификат"""
        for i in self.lub_number:
            self.current_sum += self.lub_number[i][1]
        if self.current_sum/100 >= self.args['k']:
            self.success = True
        return self.current_sum, self.success

    def __str__(self):
        return "{}".format(self.args)


CONF = {"exam_max": 30, "lab_max": 7, "lab_num": 10, "k": 0.61}
STUDENT_1 = Student("Tom", CONF)
for j in range(CONF["lab_max"]):
    STUDENT_1.make_lab(5, j)
STUDENT_1.make_exam(28)
print(STUDENT_1.is_certified())
