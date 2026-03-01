import os
import csv

def student_manager():
    filename = "Data_Management_System/student.csv"

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

    def search_student(filename):
        try:
            name_search = input("Enter the name of the student you want to find: ")
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Name"] == name_search:
                        print(f"Name: {row['Name']}, Age: {row['Age']}, Test1: {row['Test 1']}, Test2: {row['Test 2']}, Test3: {row['Test 3']}, Average: {row['Average']}")
                        return row
        except Exception as e:
            print(f"The name you entered is invalid: {e}")

    def delete_student(filename):
        try:
            name_delete = input("Enter the Name to be deleted: ")
            update_list = []
            found = False
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                fieldname = reader.fieldnames
                for row in reader:
                    if name_delete == row['Name']:
                        found = True
                    else:
                        update_list.append(row)
                if found:
                    with open(filename, "w", newline = '') as file:
                        writer = csv.DictWriter(file, fieldname)
                        writer.writeheader()
                        writer.writerows(update_list)
                        print(f"The {name_delete} is deleted")
                else:
                    print("Data not found")


        except Exception as e:
            print(f"Student not found : {e}")

            
         
                   


    #initialize(filename)
    #add_student(filename)
    #view_students(filename)
    #search_student(filename)
    delete_student(filename)


student_manager()