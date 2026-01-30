class Person:
    def __init__(self, pid, name, age, ):
        self.pid = pid
        self.name = name
        self.age = age
    
class Student:
    def __init__(self, pid, name, age, Student_id):
        self.pid = pid
        self.name = name
        self.age = age
        self.Student_id =Student_id

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, pid, name, age, Student_id):
        super().__init__(self, pid, name, age)
        self.Student_id = Student_id

    def __str__(self):
        return f"Student_ID, {self.Student_id}, Name: {self.name}, Age: {self.age}"

class Staff(Person):
    def __init__(self, pid, name, age, Staff_id):
        super().__init__(pid, name, age)
        self.Staff_id = Staff_id
    def __str__(self):
        return f"Staff_ID:{self.Staff_id}, Name: {self.name}, Age: {self.age}"

Student = Student(Person)(68114540124, "Kong", 20)
Staff = Staff(68114540123, "Chongdet", 20)
print(Student)
print(Staff)

