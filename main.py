import sqlite3

# Connect to database (creates file automatically)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    student_id TEXT,
    math REAL,
    english REAL,
    science REAL,
    total REAL,
    average REAL,
    grade TEXT
)
""")

conn.commit()

def calculate_grade(avg):
    if avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 45:
        return "D"
    else:
        return "F"
def search_student():
    search_id = input("\nEnter Student ID to search: ")

    cursor.execute("SELECT * FROM students WHERE student_id = ?", (search_id,))
    result = cursor.fetchone()

    if result:
        print("\n===== STUDENT FOUND =====")
        print("ID:", result[0])
        print("Name:", result[1])
        print("Student ID:", result[2])
        print("Math:", result[3])
        print("English:", result[4])
        print("Science:", result[5])
        print("Total:", result[6])
        print("Average:", round(result[7], 2))
        print("Grade:", result[8])
    else:
        print("Student not found.")
def update_student():
    search_id = input("\nEnter Student ID to update: ")

    cursor.execute("SELECT * FROM students WHERE student_id = ?", (search_id,))
    result = cursor.fetchone()

    if result:
        print("\nEnter new details:")

        name = input("New Name: ")
        math = float(input("New Math Score: "))
        english = float(input("New English Score: "))
        science = float(input("New Science Score: "))

        total = math + english + science
        average = total / 3

        if average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 45:
            grade = "D"
        else:
            grade = "F"

        cursor.execute("""
        UPDATE students
        SET name=?, math=?, english=?, science=?, total=?, average=?, grade=?
        WHERE student_id=?
        """, (name, math, english, science, total, average, grade, search_id))

        conn.commit()
        print("Student updated successfully.")
    else:
        print("Student not found.")
def delete_student():
    search_id = input("\nEnter Student ID to delete: ")

    cursor.execute("DELETE FROM students WHERE student_id = ?", (search_id,))
    conn.commit()

    print("Student deleted successfully (if ID existed).") 

while True:
    print("\n===== STUDENT RESULT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. View All Students")
    print("6. Exit")

    choice = input("Select option: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        student_id = input("Enter Student ID: ")

        math = float(input("Math Score: "))
        english = float(input("English Score: "))
        science = float(input("Science Score: "))

        total = math + english + science
        average = total / 3
        grade = calculate_grade(average)

        cursor.execute("""
        INSERT INTO students (name, student_id, math, english, science, total, average, grade)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, student_id, math, english, science, total, average, grade))

        conn.commit()
        print("Student added successfully.")

    elif choice == "2":
        search_student()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        cursor.execute("SELECT * FROM students")
        records = cursor.fetchall()

        for r in records:
            print("\nID:", r[0], "Name:", r[1], "Student ID:", r[2],
                  "Avg:", round(r[7], 2), "Grade:", r[8])

    elif choice == "6":
        break

    else:
        print("Invalid choice.")