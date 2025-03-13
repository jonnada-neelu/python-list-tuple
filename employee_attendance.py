# employees attendence system
```
employees = [
    (101, "Alice Johnson", "HR"),
    (102, "Bob Smith", "IT"),
    (103, "Charlie Brown", "Finance"),
    (104, "David White", "IT"),
    (105, "Eve Black", "Marketing")
]
attendance_records = [
    (101, "2025-03-01", "Present"),
    (102, "2025-03-01", "Absent"),
    (103, "2025-03-01", "Present"),
    (104, "2025-03-01", "Present"),
    (105, "2025-03-01", "Absent"),
]
def mark_attendance(attendance_records, employee_id, date, status):
    attendance_records.append((employee_id, date, status))
    print(f"Attendance marked for employee {employee_id}: {status}")
def search_attendance(attendance_records, employee_id):
    print(f"\n Searching attence for employee ID {employee_id}:")
    found = False
    for record in attendance_records:
        if record[0]==employee_id:
            print(f"Date: {record[1]}, Status: {record[2]}")
            found=True
    if not found:
        print("No records found.")
mark_attendance(attendance_records, 101, "2025-03-02", "Present")
mark_attendance(attendance_records, 103, "2025-03-02", "Absent")
mark_attendance(attendance_records, 105, "2025-03-02", "Present")

search_attendance(attendance_records, 101)
```

