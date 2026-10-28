students_data = [
    {"name": "Ravi", "marks": "85", "total": "100"},
    {"name": "Priya", "marks": "abc", "total": "100"},    # Bad marks
    {"name": "Amit", "marks": "90", "total": "0"},         # Division by zero
    {"name": "Sneha", "marks": "78", "total": "100"},
]

try:
    print("Processing all student records...\n")

    for student in students_data:
        try:
            name = student["name"]
            marks = int(student["marks"])      # Could raise ValueError
            total = int(student["total"])
            percentage = (marks / total) * 100  # Could raise ZeroDivisionError

            print(f"  ✅ {name}: {percentage:.1f}%")

        except ValueError:
            print(f"  ❌ {student['name']}: Invalid marks data!")
        except ZeroDivisionError:
            print(f"  ❌ {student['name']}: Total marks is zero!")

    print("\nAll records processed successfully!")

except Exception as e:
    # Catches any unexpected error in the overall process
    print(f"\nFatal error in processing: {e}")
    