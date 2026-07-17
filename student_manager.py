import json
import os
from datetime import datetime

class Student:
    def __init__(self, student_id, name, age, department, cgpa):
        self.student_id = student_id
        self.name = name 
        self.age = age
        self.department = department
        self.cgpa = cgpa

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "cgpa": self.cgpa
        }
    

class StudentManager:
    def __init__(self):
        self.students = []
        self.records_added = 0
        self.records_updated = 0
        self.records_deleted = 0

        if not os.path.exists("students.json"):
            with open("students.json","w") as file:
                json.dump([], file)

        self.load_students()

    def load_students(self):
        try:
            with open("students.json", "r") as file:
                self.students = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.students = []
    
    def save_students(self):
        with open ("students.json", "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self):
        student_id = input("Enter Student ID: ")
        for student in self.students:
            if student["id"] == student_id:
                print("Student ID already exists.")
                return
            
        name = input("Enter Name: ")

        try:
            age = int(input("Enter Student Age: "))
            department = input("Enter Department: ")
            cgpa = float(input("Enter CGPA: "))
        except ValueError:
            print("Invalid input! Age must be a whole number and CGPA must be a number.")
            return

        student = Student(student_id, name, age, department, cgpa)

        self.students.append(student.to_dict())

        self.save_students()

        self.records_added += 1

        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return
        for student in self.students:
            print("----------------------------")
            print("Student ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Department:", student["department"])
            print("CGPA:", student["cgpa"])
            print()

    def search_student(self):
        search_id = input("Enter Student ID to search: ")

        for student in self.students:
            if student["id"] == search_id:
              print("Student Found")
              print("----------------------------")
              print("Student ID:", student["id"])
              print("Name:", student["name"])
              print("Age:", student["age"])
              print("Department:", student["department"])
              print("CGPA:", student["cgpa"])
              return
            
        print("Student not found.")

    def update_student(self):
        update_id = input("Enter Student ID to update: ")

        for student in self.students:
            if student["id"] == update_id:
                student["name"] = input("Enter New Name: ")
                
                try:
                    student["age"] = int(input("Enter New Age: "))
                    student["cgpa"] = float(input("Enter New CGPA: "))
                except ValueError:
                    print("Invalid input! Age and CGPA must be numeric.")
                    return
                
                student["department"] = input("Enter New Department: ")

                self.save_students()

                self.records_updated += 1

                print("Student updated successfully!")
                return
        print("Student not found.")

    def delete_student(self):
        delete_id = input("Enter Student ID to delete: ")
        for student in self.students:
            if student["id"] == delete_id:

                self.students.remove(student)

                self.save_students()

                self.records_deleted += 1
                print("Student deleted successfully!")
                return
        print("Student not found.")

    def generate_report(self):
        with open("report.txt", "w") as file:
            file.write("=====================================\n")
            file.write("     STUDENT RECORD MANAGER REPORT\n")
            file.write("=====================================\n\n")

            current_time = datetime.now().strftime("%d %B %Y %I:%M:%S %p")
            file.write(f"Execution Time: {current_time}\n\n")

            file.write(f"Total Student Records : {len(self.students)}\n")
            file.write(f"Records Added         : {self.records_added}\n")
            file.write(f"Records Updated       : {self.records_updated}\n")
            file.write(f"Records Deleted       : {self.records_deleted}\n")
        print("Report generated successfully!")

        