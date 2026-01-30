class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} is {self.age} year old. ")
    
    def _str_(self):
        return f"{self.name} is {self.age} your oold "

    def main():
        my_dog = dog("Buddy",3)
        your_dog = dog("Paulia",2)
        print(my_dog)
        print(your_dog)

    