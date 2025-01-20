# attributes - first_name, last_name, year
# methods - get_info()


class Person:
    def __init__(self, first_name, last_name, year):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year


    def get_info(self):
        print(f"My fullname is {self.first_name} {self.last_name}")

    def get_age(self):
        present_year = 2025
        print(present_year - self.year)


person1 = Person("Hilola","Uljabaeva", 2008)
person1.get_info()
person1.get_age()

# TAKRORLAB KELISH
# git, github
# oop
# function, data types

# UY ISHI CLASS(OOP)
# PDP School o'quvchisi
# ism, familiya, sinfi, yoshi, ... 5ta attribute bo'lishi kerak
# misol uchun: fanlar(), ... 3 ta method bo'lishi kerak


class PDPstudent:
    def __init__(self, name, last_name, age, grade, favorite_subject):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.grade = grade
        self.favorite_subject = favorite_subject

    def familiarization(self):
        print(f"Salom men {self.name} {self.last_name}man. Men PDP Schoolning {self.grade} sinf o'quvchisiman")

    def subject(self):
        print(f"Men yoqtirgan fan bu {self.favorite_subject}")

    def age1(self):
        print(f"Mening yoshim {self.age} da")

student = PDPstudent("Hilola", "O'ljabaeva", 16, 10, "Python")

student.familiarization()
student.subject()
student.age1()

# loyiha talabalari:PDP
# Talaba ma'lumotlarini  saqlash uchun Pupil klassi yaratiladi

# Atributlar: ism, familiya, yil, GPA
# Methodlar: ma'lumotlarni ko'rsatish


class Pupil:
    def __init__(self, ism, familiya, yil, gpa):
        self.ism = ism
        self.familiya = familiya
        self.yil = yil
        self.gpa = gpa

    def getting_info(self):
        print(f"Ism: {self.ism} Familiya: {self.familiya} Tug'ilgan yil: {self.yil} GPA: {self.gpa}")
        # print(f"Familiya: {self.familiya}")
        # print(f"Tug'ilgan yil: {self.yil}")
        # print(f"GPA: {self.gpa}")

pupil1 = Pupil("Hilola", "O'ljabaeva", 2008, 85)
pupil1.getting_info()

# Talabalarni boshqarish uchun PupilManager klassi yaratiladi.
#
# Funksiyalar:
# Talaba qo'shish.
# Talaba ma'lumotlarini yangilash.
# Talabalar ro'yxatini chiqarish.
# Eng yuqori GPAga ega talabani topish.


class PupilManager:
    def __init__(self):
        self.pupils =[]

    def add_pupil(self,pupil):
        self.pupils.append(pupil)

    def get_pupils(self):
        for pupil in self.pupils:
            print(pupil.get_info())


    def highest_gpa(self):
        gpa = 0
        for pupil in self.pupils:
            if pupil.gpa > gpa:
                gpa = pupil.gpa


        return gpa

    def update_info(self, first_name, last_name, birth_year, gpa):
        for pupil in self.pupils:
            if first_name == first_name and last_name == last_name:
                pupil.birth_year = birth_year
                pupil.gpa = gpa
                pupil.save(pupil)
                





pupil1 = Pupil("Hilola", "O'ljabaeva", 2008, 85)
pupil2 = Pupil("Chingiz", "Shukurov", 2008, 75)


manager = PupilManager()
manager.add_pupil(pupil1)
manager.get_pupils()
print(manager.highest_gpa())


























