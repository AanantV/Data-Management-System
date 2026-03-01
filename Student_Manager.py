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
            Test2 = int(input(f"Enter the score of {Name} in test 2: "))
            Test3 = int(input(f"Enter the score of {Name} in test 3: "))
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

    def update_student(filename):
        try:
            name_update = input("Enter the Name of the student you want to update: ")
            value = input(f"Enter the field you want to update for {name_update}: ")
            found = False
            rows = []

            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                fieldname = reader.fieldnames
                for row in reader:
                    if row['Name'] == name_update:
                        found = True
                        if value == "Test 1":
                            update_val1 = int(input("Enter the score to be updated for test 1: "))
                            row['Test 1'] = update_val1
                        elif value == "Test 2":
                            update_val2 = int(input("Enter the value to be updated for test 2: "))
                            row['Test 2'] = update_val2
                        elif value == "Test 3":
                            update_val3 = int(input("Enter the value to be updated for test 3: "))
                            row['Test 3'] = update_val3
                        avg = (int(row['Test 1']) + int(row['Test 2']) + int(row['Test 3']))/3
                        row['Average'] = f"{avg:.2f}"
                    rows.append(row)
            if found:
                with open(filename, "w", newline ='') as file:
                        writer = csv.DictWriter(file, fieldname)
                        writer.writeheader()
                        writer.writerows(rows)
                        print(f"The {row[value]} for {name_update} is updated")
        except Exception as e:
            print(f"The Data is not updated: {e}")

    def statistics(filename):
            max_score= max_test1= max_test2= max_test3 = 0
            min_score= min_test1= min_test2= min_test3 = None
            max_name = max_test1_name = max_test2_name = max_test3_name = ""
            min_name = min_test1_name = min_test2_name = min_test3_name = ""
            avg_score = 0
            try:
                with open(filename, "r") as file:
                    reader = csv.DictReader(file)
                    fieldname = reader.fieldnames
                    for row in reader:
                        average = float(row['Average']) 
                        test1 = int(row['Test 1'])
                        test2 = int(row['Test 2'])
                        test3 = int(row['Test 3'])

                        if average > max_score:
                            max_score = average
                            max_name = row['Name']
                        if test1 > max_test1:
                            max_test1 = test1
                            max_test1_name = row['Name']
                        if  test2 > max_test2:
                            max_test2 = test2
                            max_test2_name = row['Name']
                        if test3 > max_test3:
                            max_test3 = test3
                            max_test3_name = row['Name']

                        if min_score is None or average < min_score:
                            min_score = average
                            min_name = row['Name']
                        if min_test1 is None or test1 < min_test1:
                            min_test1 = test1
                            min_test1_name = row['Name']
                        if min_test2 is None or test2 < min_test2:
                            min_test2 = test2
                            min_test2_name = row['Name']
                        if min_test3 is None or test3 < min_test3:
                            min_test3 = test3
                            min_test3_name = row['Name']
                print(f"The maximum score based on average is {max_score} and the name is {max_name}")
                print(f"The highest mark in test 1 is {max_test1} and the name is {max_test1_name}")
                print(f"The highest mark in test 2 is {max_test2} and the name is {max_test2_name}")
                print(f"The highest mark in test 3 is {max_test3} and the name is {max_test3_name}")

                print(f"The minimum score based on average is {min_score} and the name is {min_name}")
                print(f"The lowest mark in test 1 is {min_test1} and the name is {min_test1_name}")
                print(f"The lowest mark in test 2 is {min_test2} and the name is {min_test2_name}")
                print(f"The lowest mark in test 3 is {min_test3} and the name is {min_test3_name}")


            except Exception as e:
                print(f"The Data is not updated: {e}")


    #initialize(filename)
    #add_student(filename)
    #view_students(filename)
    #search_student(filename)
    #delete_student(filename)
    #update_student(filename)
    statistics(filename)

student_manager()