# class Pupil:
#     def init(self, name, fam, yil, sinf, GPA):
#         self.name = name
#         self.fam = fam
#         self.yil = yil
#         self.sinf = sinf
#         self.GPA = GPA
#
#     def info(self):
#         print(f"O'quvchi haqida ma'lumot:")
#         print(f"Ismi: {self.name}")
#         print(f"Familiyasi: {self.fam}")
#         print(f"Tug‘ilgan yili: {self.yil}")
#         print(f"Sinf: {self.sinf}")
#         print(f"GPA: {self.GPA}")
#
#     def get_age(self):
#         present_year = 2025
#         return present_year - self.yil
#
#
# class Student:
#     def init(self, name, yil, kursi, fakultet, GPA):
#         self.name = name
#         self.yil = yil
#         self.kursi = kursi
#         self.fakultet = fakultet
#         self.GPA = GPA
#
#     def info(self):
#         print(f"Talaba haqida ma'lumot:")
#         print(f"Ismi: {self.name}")
#         print(f"Tug‘ilgan yili: {self.yil}")
#         print(f"Kursi: {self.kursi}")
#         print(f"Fakulteti: {self.fakultet}")
#         print(f"GPA: {self.GPA}")
#
#     def get_age(self):
#         present_year = 2025
#         return present_year - self.yil
#
#
# class PDPManager:
#     def init(self):
#         self.students = []
#
#         self.pupils = []
#     def add_student(self, student):
#         self.students.append(student)
#
#     def add_pupil(self, pupil):
#         self.pupils.append(pupil)
#
#     def remove_st(self, student):
#         if student in self.students:
#             self.students.remove(student)
#         else:
#             print("Talaba ro'yxatda topilmadi!")
#
#     def remove_pu(self, pupil):
#         if pupil in self.pupils:
#             self.pupils.remove(pupil)
#         else:
#             print("O'quvchi ro'yxatda topilmadi!")
#
#     def check_students(self):
#         if not self.students:
#             print("Talabalar ro'yxati bo'sh.")
#         for student in self.students:
#             student.info()
#
#     def check_pupils(self):
#         if not self.pupils:
#             print("O'quvchilar ro'yxati bo'sh.")
#         for pupil in self.pupils:
#             pupil.info()
#
#     def get_max_student_gpa(self):
#         if not self.students:
#             print("Talabalar ro'yxati bo'sh.")
#             return
#         max_gpa_student = max(self.students, key=lambda s: s.GPA)
#         print("Eng yuqori GPA ga ega talaba:")
#         max_gpa_student.info()
#
#     def get_max_pupil_gpa(self):
#         if not self.pupils:
#             print("O'quvchilar ro'yxati bo'sh.")
#             return
#         max_gpa_pupil = max(self.pupils, key=lambda p: p.GPA)
#         print("Eng yuqori GPA ga ega o'quvchi:")
#         max_gpa_pupil.info()
#
#
#
# pupil1 = Pupil("Hilola", "O'ljabaeva", 2008, 10, 4.5)
# pupil2 = Pupil("MAdina", "Nodirova", 2009, 9, 3.8)
# student1 = Student("Sunnatxoja", "2003", 2, "Informatika", 3.9)
# student2 = Student("Sardor", "2002", 3, "Matematika", 4.8)
#
# manager = PDPManager()
# manager.add_pupil(pupil1)
# manager.add_pupil(pupil2)
# manager.add_student(student1)
# manager.add_student(student2)
#
# manager.check_pupils()
# manager.check_students()
#
# manager.get_max_student_gpa()
# manager.get_max_pupil_gpa()
#
#
# manager.remove_st(student1)
#
#
# manager.remove_pu(pupil2)
#
# manager.check_pupils()
# manager.check_students()





import uuid

class Pupil:
    def __init__(self, name, fam, yil, sinf, GPA):
        self.id = uuid.uuid4()
        self.name = name
        self.fam = fam
        self.yil = yil
        self.sinf = sinf
        self.GPA = GPA

    def info(self):
        print(f"O'quvchi haqida ma'lumot:")
        print(f"ID: {self.id}")
        print(f"Ismi: {self.name}")
        print(f"Familiyasi: {self.fam}")
        print(f"Tug‘ilgan yili: {self.yil}")
        print(f"Sinf: {self.sinf}")
        print(f"GPA: {self.GPA}")

    def get_age(self):
        present_year = 2025
        return present_year - self.yil


class Student:
    def __init__(self, name, yil, kursi, fakultet, GPA):
        self.id = uuid.uuid4()
        self.name = name
        self.yil = yil
        self.kursi = kursi
        self.fakultet = fakultet
        self.GPA = GPA

    def info(self):
        print(f"Talaba haqida ma'lumot:")
        print(f"ID: {self.id}")
        print(f"Ismi: {self.name}")
        print(f"Tug‘ilgan yili: {self.yil}")
        print(f"Kursi: {self.kursi}")
        print(f"Fakulteti: {self.fakultet}")
        print(f"GPA: {self.GPA}")

    def get_age(self):
        present_year = 2025
        return present_year - self.yil


class PDPManager:
    def __init__(self):
        self.id = uuid.uuid4()
        self.students = []
        self.pupils = []

    def add_student(self, student):
        self.students.append(student)

    def add_pupil(self, pupil):
        self.pupils.append(pupil)

    def remove_st(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
            print("Talaba ro'yxatda topilmadi!")

    def remove_pu(self, pupil):
        if pupil in self.pupils:
            self.pupils.remove(pupil)
        else:
            print("O'quvchi ro'yxatda topilmadi!")

    def check_students(self):
        if not self.students:
            print("Talabalar ro'yxati bo'sh.")
        for student in self.students:
            student.info()

    def check_pupils(self):
        if not self.pupils:
            print("O'quvchilar ro'yxati bo'sh.")
        for pupil in self.pupils:
            pupil.info()

    def get_max_student_gpa(self):
        if not self.students:
            print("Talabalar ro'yxati bo'sh.")
            return
        max_gpa_student = max(self.students, key=lambda s: s.GPA)
        print("Eng yuqori GPA ga ega talaba:")
        max_gpa_student.info()

    def get_max_pupil_gpa(self):
        if not self.pupils:
            print("O'quvchilar ro'yxati bo'sh.")
            return
        max_gpa_pupil = max(self.pupils, key=lambda p: p.GPA)
        print("Eng yuqori GPA ga ega o'quvchi:")
        max_gpa_pupil.info()


# Create instances
pupil1 = Pupil("Hilola", "O'ljabaeva", 2008, 10, 4.5)
pupil2 = Pupil("Madina", "Nodirova", 2009, 9, 3.8)
student1 = Student("Aziza", 2003, 2, "Informatika", 3.9)
student2 = Student("Sardor", 2002, 3, "Matematika", 4.8)


manager = PDPManager()
manager.add_pupil(pupil1)
manager.add_pupil(pupil2)
manager.add_student(student1)
manager.add_student(student2)


manager.check_pupils()
manager.check_students()


manager.get_max_student_gpa()
manager.get_max_pupil_gpa()


manager.remove_st(student1)
manager.remove_pu(pupil2)


manager.check_pupils()
manager.check_students()





