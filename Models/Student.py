from Models.Person import Person


class Student(Person):
    def __init__(self, pid, name, age, Student_id):
        super().__init__(self, pid, name, age)
        self.Student_id = Student_id

    def __str__(self):
        return f"Student_ID, {self.Student_id}, Name: {self.name}, Age: {self.age}"