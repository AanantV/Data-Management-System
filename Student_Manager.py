import os
import csv

def student_manager():
    filename = "Data_Management_System/student.csv"
    report = "Data_Management_System/reports/reports.txt"

    def initialize(filename):
        try:
            if not os.path.exists(filename):
                with open(filename, "a", newline = '') as file:
                    writer = csv.DictWriter(file, fieldnames = ["Name","Age","Test 1","Test 2","Test 3","Average"])
                    writer.writeheader()
                    print("Student.csv has been created with headers")
        except FileNotFoundError:
                print("File is not created")

    def add_student():
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

    def view_students():
        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(f"Name: {row['Name']}, Age: {row['Age']}, Test1: {row['Test 1']}, Test2: {row['Test 2']}, Test3: {row['Test 3']}, Average: {row['Average']} ")
        except Exception as e:
            print(f"File not found: {e}")

    def search_student():
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

    def delete_student():
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

    def update_student():
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

    def statistics():
            max_score= max_test1= max_test2= max_test3 = 0
            min_score= min_test1= min_test2= min_test3 = None
            max_name = max_test1_name = max_test2_name = max_test3_name = ""
            min_name = min_test1_name = min_test2_name = min_test3_name = ""
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

                return {
                    "max_score": max_score,
                    "max_name": max_name,
                    "max_test1": max_test1,
                    "max_test1_name": max_test1_name,
                    "max_test2": max_test2,
                    "max_test2_name": max_test2_name,
                    "max_test3": max_test3,
                    "max_test3_name": max_test3_name,
                    "min_score": min_score,
                    "min_name": min_name,
                    "min_test1": min_test1,
                    "min_test1_name": min_test1_name,
                    "min_test2": min_test2,
                    "min_test2_name": min_test2_name,
                    "min_test3": min_test3,
                    "min_test3_name": min_test3_name
                     }


            except Exception as e:
                print(f"The Data is not updated: {e}")

    def display_statistics():

        stats = statistics()
    
        if stats is None:
            print("No data available!")
            return
    
    
        print(f"The maximum score based on average is {stats['max_score']} and the name is {stats['max_name']}")
        print(f"The highest mark in test 1 is {stats['max_test1']} and the name is {stats['max_test1_name']}")
        print(f"The highest mark in test 2 is {stats['max_test2']} and the name is {stats['max_test2_name']}")
        print(f"The highest mark in test 3 is {stats['max_test3']} and the name is {stats['max_test3_name']}")

        print(f"The minimum score based on average is {stats['min_score']} and the name is {stats['min_name']}")
        print(f"The lowest mark in test 1 is {stats['min_test1']} and the name is {stats['min_test1_name']}")
        print(f"The lowest mark in test 2 is {stats['min_test2']} and the name is {stats['min_test2_name']}")
        print(f"The lowest mark in test 3 is {stats['min_test3']} and the name is {stats['min_test3_name']}")



    def top_student():
        try:
            max_score = 0
            max_sum = 0
            topper = ''
            with open(filename, "r") as file:
                
                reader = csv.DictReader(file)
                for row in reader:
                    avg = float(row['Average'])
                    sum = (int(row['Test 1'])) + (int(row['Test 2'])) + (int(row['Test 3']))
                    if avg > max_score and sum > max_sum:
                        max_score = avg
                        max_sum = sum
                        topper = row['Name']
                    
                
                print(f"The topper in the class is {topper}, the total mark is {max_sum} and average is {max_score}")
        
        except Exception as e:
            print(f"Sum error: {e}")

    def export_report(filename, report):
        try:
            from datetime import datetime
            now = datetime.now()
            timestamp = now.strftime("%A, %B %d, %Y at %I:%M %p")
            stats = statistics()
            count = 0
            class_avg = 0
            max_score = 0
            max_sum = 0
            topper = ''
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    count+=1
                    class_avg += float(row['Average'])
                    avg = float(row['Average'])
                    sum = (int(row['Test 1'])) + (int(row['Test 2'])) + (int(row['Test 3']))
                    if avg > max_score and sum > max_sum:
                        max_score = avg
                        max_sum = sum
                        topper = row['Name']
                

                class_average = f"{class_avg/count:.2f}"
              

            reports = f"""================================================================================\n                    STUDENT MANAGEMENT SYSTEM - CLASS REPORT\n================================================================================\n
Generated on: {timestamp}
Report Generated by: Student Management System\n
--------------------------------------------------------------------------------\n                          CLASS OVERVIEW\n--------------------------------------------------------------------------------\n
Total Students: {count}
Average Class Score: {class_average}
Highest Score: {stats['max_score']:.2f} ({stats['max_name']})
Lowest Score: {stats['min_score']:.2f} ({stats['min_name']})

--------------------------------------------------------------------------------
                           TOP PERFORMERS BY TEST
--------------------------------------------------------------------------------
Test 1 - Highest: {stats['max_test1']} ({stats['max_test1_name']})
Test 2 - Highest: {stats['max_test2']} ({stats['max_test2_name']})
Test 3 - Highest: {stats['max_test3']} ({stats['max_test3_name']})

--------------------------------------------------------------------------------
                        STUDENTS NEEDING IMPROVEMENT
--------------------------------------------------------------------------------
Test 1 - Lowest: {stats['min_test1']} ({stats['min_test1_name']})
Test 2 - Lowest: {stats['min_test2']} ({stats['min_test2_name']})
Test 3 - Lowest: {stats['min_test3']} ({stats['min_test3_name']}) """

            with open(report, "w") as file:
                file.write(reports)

        except Exception as e:
            print(f"File not found: {e}")

    while True:
        print("Student Management System")
        print("1. Add a Student")
        print("2. View All Student Info")
        print("3. Search a Student")
        print("4. Delete Student Information")
        print("5. Update Student Info")
        print("6. View Statistics")
        print("7. View Topper")
        print("8. Export report")
        print("9. Quit")

        choice = input("Enter a number between 1-9 to perform operation: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            display_statistics()
        elif choice == "7":
            top_student()
        elif choice == "8":
            export_report(filename, report)
        elif choice == "9":
            print("Quitting...")
            break
        else:
            print("Invalid value")

        

    #initialize(filename)
    #add_student(filename)
    #view_students(filename)
    #search_student(filename)
    #delete_student(filename)
    #update_student(filename)
    #statistics(filename)
    #top_student(filename)
    #export_report(filename, report)
    #display_statistics()

student_manager()