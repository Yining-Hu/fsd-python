import csv
import random

class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.mark >= 85:
            return "HD"
        elif self.mark >= 75:
            return "D"
        elif self.mark >= 65:
            return "C"
        elif self.mark >= 50:
            return "P"
        else:
            return "Z"

    def __str__(self):
        return f"{self.name} -> {self.grade}"
    
class Faculty:
    def __init__(self):
        self.students = {}

    def enroll_students(self):
        for i in range(100, 110):
            name = f"Student_{i}"
            mark = random.randint(1, 100)
            student = Student(name, mark)
            self.students[name] = student

    def save(self):
        with open("grades.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Mark", "Grade"])
            for student in self.students.items():
                writer.writerow([student[1].name, student[1].mark, student[1].grade])

    def show(self):
        with open("grades.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def menu(self):
        while True:
            choice = input("Menu: (p) enroll, (s) save, (v) show, (x) exit: ").strip().lower()
            if choice == 'p':
                self.enroll_students()
            elif choice == 's':
                self.save()
                print("Students saved to grades.csv")
            elif choice == 'v':
                print("Contents of grades.csv:")
                self.show()
            elif choice == 'x':
                break
            else:
                self.help()
    
    def help(self):
        print("Menu options (p/s/v/x)")
        print("(p) enrol - to add 10 students")
        print("(s) save - to save the student list to a csv file")
        print("(v) show - to read and show the content of the csv file")
        print("x = exit")

# Example usage:
faculty = Faculty()
faculty.menu()
    
