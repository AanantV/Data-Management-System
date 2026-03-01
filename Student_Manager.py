import os
import csv

def student_manager():
    filename = "Data Management System/student.csv"

    def initialize(filename):
        try:
            if not os.path.exists(filename):
                with open(filename, "a", newline = '') as file:
                    writer = csv.DictWriter(file, fieldnames = ["Name","Age","Test 1","Test 2","Test 3","Average"])
                    writer.writeheader()
                    print("Student.csv has been created with headers")
        except FileNotFoundError:
                print("File is not created")

    def add_student(filename):
        try:
            Name = input("Enter the name you want to add in the list: ")
            Age = int(input(f"Enter the age of {Name}: "))
            Test1 = int(input(f"Enter the score of {Name} in test 1: "))
            Test2 = int(input(f"Enter the score of {Name} in test 1: "))
            Test3 = int(input(f"Enter the score of {Name} in test 1: "))
            avg = (Test1+Test2+Test3)/3
            Average = f"{avg:.2f}"
            columns = ["Name","Age","Test 1","Test 2","Test 3","Average"]
            with open(filename, "a", newline = '') as file:
                 writer = csv.DictWriter(file, fieldnames = columns)
                 writer.writerow({"Name":Name, "Age":Age, "Test 1":Test1, "Test 2":Test2, "Test 3":Test3, "Average":Average})

        except Exception as e:
             print(f"Unable to add record :{e}")

    def view_students(filename):
        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(f"Name: {row['Name']}, Age: {row['Age']}, Test1: {row['Test 1']}, Test2: {row['Test 2']}, Test3: {row['Test 3']}, Average: {row['Average']} ")
        except Exception as e:
            print(f"File not found: {e}")
            
         
                   


    #initialize(filename)
    #add_student(filename)
    view_students(filename)


student_manager()