class Classroom:
    def __init__(self, name):
        self.students = []
        self.name = name

    def add_student(self, student):
        self.students.append(student)


    def len(self):
        return len(self.students)
    
    def __geitem__(self, index):
        return self.students[index]