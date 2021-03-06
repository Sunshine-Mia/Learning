
class Person(object):
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return self.name


class Student(Person):
    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        return f"{self.name} studies {self.branch} and is in {self.year} year."


class Teacher(Person):
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.name = name
        self.papers = papers

    def get_details(self):
        return f"{self.name} teches {self.papers}."


person1 = Person('Sachin')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
