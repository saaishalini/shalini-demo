import csv
import json
# Create a CSV file to store employee data
def create_employee_csv(filename):
    header = ["Employee ID", "Name", "Age", "Designation", "Contact Number"]
    employees =[
        ["AA-001", "Saranya", 24, "Developer", "1234567890"],
        ["AA-002","Riya", 30, "Manager", "9876543210"],
        ["AA-003", "Jagan", 22, "Intern", "4567891230"],
        ["AA-004", "Janani", 26, "Designer", "7890123456"],
        ["AA-005", "Tamil", 35, "Analyst", "2345678901"],
        ["AA-006", "Sachin", 28, "Sales manager", "9012345678"],
        ["AA-007", "Saran", 23, "Developer", "5678901234"],
        ["AA-008", "Naveen ", 40, "Designer", "0123456789"],
        ["AA-009", " Jaya", 32, "Engineer", "3456789012"],
        ["AA-010", "Sai", 27, "Intern", "8901234567"]
    ]
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(employees)
create_employee_csv("employees.csv")

# Use generators to read employee data and write employees based on age into separate files
def read_employee_data(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row

def write_employees_to_file(employees, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=employees[0].keys())
        writer.writeheader()
        writer.writerows(employees)

def filter_employees_by_age(employees, min_age, max_age):
    filtered_employees = [employee
 for employee in employees if min_age <= int(employee["Age"]) <= max_age]
    return filtered_employees

employees = list(read_employee_data("employees.csv"))
young_employees = filter_employees_by_age(employees, 0, 25)
middle_aged_employees = filter_employees_by_age(employees, 26, 45)

write_employees_to_file(young_employees, "age_under_25.csv")
write_employees_to_file(middle_aged_employees, "age_25_to_45.csv")

# Read the CSV files and print employees' data in JSON format
def read_employees_from_file(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        employees = list(reader)
        return employees

def print_employees_as_json(employees):
    json_data = json.dumps(employees, indent=4)
    print(json_data)

young_employees = read_employees_from_file("age_under_25.csv")
middle_aged_employees = read_employees_from_file("age_25_to_45.csv")

print("age_25_to_45.csv:")
print_employees_as_json(young_employees)

print("\nage_25_to_45.csv:")
print_employees_as_json(middle_aged_employees)
