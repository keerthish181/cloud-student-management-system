import pyodbc

server = 'student-sql-server123.database.windows.net'
database = 'StudentDB'
username = 'sqladmin'
password = 'YOUR_SQL_PASSWORD'

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
    'Encrypt=yes;'
    'TrustServerCertificate=no;'
    'Connection Timeout=30;'
)

cursor = conn.cursor()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll number: ")
        dept = input("Enter department: ")

        cursor.execute(
            "INSERT INTO Students (name, rollno, department) VALUES (?, ?, ?)",
            name, roll, dept
        )
        conn.commit()
        print("Student added successfully!")

    elif choice == "2":
        cursor.execute("SELECT * FROM Students")
        for row in cursor.fetchall():
            print(row)

    elif choice == "3":
        break

conn.close()


