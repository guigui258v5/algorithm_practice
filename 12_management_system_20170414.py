import datetime


class PersonValueError(ValueError):
    pass


class PersonTypeError(TypeError):
    pass


class Person(object):
    """师生类"""
    __num = 0  # 计数

    def __init__(self, name, gender, ident, birthday):
        if not (isinstance(name, str) and isinstance(ident, str) and (gender in ('male', 'female'))):
            raise PersonTypeError(name, gender, ident)

        try:
            self.__birthday = datetime.date(*birthday)  # 通过*解包
        except ValueError:
            raise PersonValueError('Wrong date:', birthday)

        self.__name = name
        self.__gender = gender
        self.__ident = ident
        self.__age = datetime.date.today().year - self.__birthday.year
        Person.__num += 1

    def __str__(self):
        return ', '.join(('编号:'+self.__ident, '姓名:'+self.__name, '性别:'+self.__gender, '生日:'+str(self.__birthday)))

    def name(self):
        return self.__name

    def gender(self):
        return self.__gender

    def ident(self):
        return self.__ident

    def age(self):
        return self.__age

    def birthday(self):
        return self.__birthday

    def set_name(self, new_name):  # 其余属性同理
        if not isinstance(new_name, str):
            raise PersonTypeError(new_name)
        self.__name = new_name

    def __lt__(self, other):
        if not isinstance(other, Person):
            raise PersonTypeError(other)
        return self.__ident < other.__ident

    @classmethod
    def num(cls):
        return cls.__num


class Student(Person):
    """学生"""
    __id_num = 0

    @classmethod
    def __id_gen(cls):
        cls.__id_num += 1
        year = datetime.date.today().year
        # print('1{:04}{:05}'.format(year, cls.__id_num))
        # print(type('1{:04}{:05}'.format(year, cls.__id_num)))
        return '1{:04}{:05}'.format(year, cls.__id_num)

    def __init__(self, name, gender, birthday, department):
        Person.__init__(self, name, gender, Student.__id_gen(), birthday)
        self.__department = department
        self.__enroll_date = datetime.date.today()
        self.__courses = {}

    def __str__(self):
        return ', '.join((
            Person.__str__(self), '入学日期:'+str(self.__enroll_date), '院系:'+self.__department, '课程记录:'+str(self.scores())
        ))

    def set_course(self, course):
        if not isinstance(course, str):
            raise PersonTypeError(course)
        self.__courses[course] = None

    def set_score(self, course, score):
        if course not in self.__courses:
            raise PersonValueError('this course is not selected', course)
        if not (isinstance(score, int) or isinstance(score, float)):
            raise PersonTypeError(score)
        self.__courses[course] = score

    def scores(self):
        return [(course, self.__courses[course]) for course in self.__courses]


class Staff(Person):
    """教职工类"""
    __id_num = 0

    @classmethod
    def __id__gen(cls):
        cls.__id_num += 1
        year = datetime.date.today().year
        return '0{:04}{:05}'.format(year, cls.__id_num)

    def __init__(self, name, gender, birthday):
        Person.__init__(self, name, gender, Staff.__id__gen(), birthday)
        self.__entry_date = datetime.date.today()
        self.__department = None
        self.__position = None
        self.__salary = None

    def set_department(self, department):
        if not isinstance(department, str):
            raise PersonTypeError
        self.__department = department

    def set_position(self, position):
        if not isinstance(position, str):
            raise PersonTypeError
        self.__position = position

    def set_salary(self, salary):
        if (not isinstance(salary, int)) and (not isinstance(salary, float)):
            raise PersonTypeError
        self.__salary = salary

    def __str__(self):
        return ', '.join(
            (Person.__str__(self), '入职日期:'+str(self.__entry_date),
             '院系:'+self.__department, '职位:'+self.__position,
             '工资:'+str(self.__salary))
            )


def main():
    p1 = Person('song', 'male', '88888888', (1993, 12, 18))
    p2 = Person('song', 'male', '88288888', (1993, 12, 18))
    p3 = Person('song', 'male', '88388888', (1993, 12, 18))
    p4 = Person('song', 'male', '88488888', (1993, 12, 18))
    p5 = Person('song', 'male', '88588888', (1993, 12, 18))
    print(p1.name())
    print(p1.gender())
    print(p1.ident())
    print(p1.birthday())
    print(p1.age())
    print(Person.num())

    p1.set_name('Song')
    print(p1.name())
    print(p1)

    plist = [p1, p2, p3, p4, p5]
    for item in plist:
        print(item)

    print('-'*50)

    plist.sort()
    for item in plist:
        print(item)

    print('-'*50)

    s1 = Student('Song', 'male', (1993, 12, 1), 'Python')
    s2 = Student('Zhu', 'female', (1993, 3, 1), 'JavaScript')
    s1.set_course('Math')
    s1.set_score('Math', 200)
    s1.set_course('English')
    s1.set_score('English', 120)
    print(s1.scores())
    print(s1)
    print(s2)

    print('-'*50)

    t1 = Staff('Song', 'male', (1993, 12, 1))
    t1.set_department('Python')
    t1.set_position('Manager')
    t1.set_salary(600000)
    print(t1)
    t2 = Staff('Song', 'male', (1993, 12, 1))
    t2.set_department('Python')
    t2.set_position('Manager')
    t2.set_salary(600000)
    print(t2)

if __name__ == '__main__':
    main()
