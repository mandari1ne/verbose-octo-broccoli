class Student:
    university = "БНТУ"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Метод экземпляра класса
    def get_info(self):
        return f"Студент {self.name}, возраст {self.age}"

    #Статический метод
    @staticmethod
    def greet():
        return "Привет, студент!"

    #Метод класса
    @classmethod
    def change_university(cls, new_university):
        cls.university = new_university

student1 = Student("Иван", 18)
student2 = Student("Борис", 19)

print(student1.get_info())
print(student2.get_info())

print(Student.greet())

Student.change_university("БГУИР")

print(f"Университет {student1.name} после изменения: {student1.university}")
print(f"Университет {student2.name} после изменения: {student2.university}")