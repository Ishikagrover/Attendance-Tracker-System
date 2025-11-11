# -----------------------------------------------------------
# Name -> Ishika grover 
# Roll No. -> 2201940059
# Course -> MCA(AI and ML)
# Date -> 8-11-2025
# Assignment Title -> ATTENDENCE TRACKER (Assigment no. 1)
# -----------------------------------------------------------


# Task 1: Welcome Message
print("==============================================================")
print("                   WELCOME TO ATTENDANCE TRACKER              ")
print("==============================================================")
print("\nHello User! 👋")
print("This tool helps in collecting and storing student attendance data.")
print("You will enter each student's name and their check-in time.")
print("The program will store this information safely using a dictionary,")
print("where each student's name is linked to their check-in time.")
print("\nLet's begin entering the attendance details!\n")

print("\n------------------------ THANK YOU! ------------------------")

# Task 2 & 3: Input, Collection and Validation 
print("==============================================================")
print("                   THIS IS TASK 2 AND 3              ")
print("==============================================================")
attendance = {}   
num = int(input("How many students do you want to record? "))
count = 1   
while count <= num:
    print("\nEntry", count)

    name = input("Enter Student Name: ")
    if name == "":
        print("Name cannot be empty. Please try again.")
        continue

    if name in attendance:
        print("This student is already recorded. Try another name.")
        continue

    time = input("Enter Check-in Time (example: 09:15 AM): ")
    if time == "":
        print("Time cannot be empty. Please try again.")
        continue

    attendance[name] = time
    count = count + 1   

# Task 4: Attendance Summary Display

print("\n==============================================================")
print("                    ATTENDANCE SUMMARY                        ")
print("==============================================================\n")

# Display table headers
print("Student Name\t\tCheck-in Time")
print("--------------------------------------------------------------")

# Display each student's name and time
for student_name, check_in_time in attendance.items():
    print(f"{student_name:<20}\t{check_in_time}")

print("--------------------------------------------------------------")
print(f"\nTotal Students Present: {len(attendance)}\n")
print("==============================================================")
print("                 END OF ATTENDANCE SUMMARY                    ")
print("==============================================================\n")

# Task 5: Absentee Validation
print("\nWould you like to calculate absentees? (yes/no)")
choice = input("Enter choice: ").lower()

if choice == "yes":
    total_students = int(input("Enter total number of students in class: "))
    absentees = total_students - len(attendance)
    
    print("\n---------------- Absentee Report ----------------")
    print(f"Total Present : {len(attendance)}")
    print(f"Total Absent  : {absentees}")
    print("------------------------------------------------")

# 4Task 6: Save Attendance Report to a File (Beginner Friendly)

import datetime   
save_choice = input("\nDo you want to save the attendance report? (yes/no): ").strip().lower()

if save_choice == "yes":

    file = open("attendance_log.txt", "w")
    file.write("Attendance Report\n")
    file.write("------------------------------\n")
    file.write("Student Name      Check-in Time\n")
    file.write("------------------------------\n")

    for name in attendance:
        file.write(name + " " * (20 - len(name)) + attendance[name] + "\n")
    file.write("------------------------------\n")
    file.write("Total Students Present: " + str(len(attendance)) + "\n")
    file.write("Report Generated On: " + str(datetime.datetime.now()) + "\n")
    file.close()

    print("Attendance report successfully saved as 'attendance_log.txt'!")
else:
    print("Report not saved.")


