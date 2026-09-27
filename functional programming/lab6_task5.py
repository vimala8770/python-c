from functools import reduce

employees = [
    {"name": "Ravi", "department": "IT", "salary": 40000},
    {"name": "Anu", "department": "HR", "salary": 35000},
    {"name": "Kiran", "department": "IT", "salary": 50000},
    {"name": "Sita", "department": "Finance", "salary": 45000},
    {"name": "Rahul", "department": "IT", "salary": 30000}
]
# Select employees from IT department
it_employees = list(
    filter(lambda emp: emp["department"] == "IT", employees)
)
# Give 10% salary hike without modifying original dictionaries
hiked_employees = list(
    map(
        lambda emp: {
            **emp,
            "salary": emp["salary"] * 1.10
        },
        it_employees
    )
)
# Calculate total salary after hike
total_salary = reduce(
    lambda total, emp: total + emp["salary"],
    hiked_employees,
    0
)
print("IT Employees after 10% hike:")
for emp in hiked_employees:
    print(emp)
print("Total salary expenditure:", total_salary)
OUTPUT:
IT Employees after 10% hike:
{'name': 'Ravi', 'department': 'IT', 'salary': 44000.0}
{'name': 'Kiran', 'department': 'IT', 'salary': 55000.00000000001}
{'name': 'Rahul', 'department': 'IT', 'salary': 33000.0}
Total salary expenditure: 132000.0








