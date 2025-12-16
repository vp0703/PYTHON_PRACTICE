# 4. Highest Salary (Dictionary)
# --------------------------------------------------
# Find the employee(s) with the highest salary.

employees = {
    "Alice": 50000,
    "Bob": 70000,
    "Charlie": 70000,
    "David": 60000
}
# Expected Output:
# ["Bob", "Charlie"]


max_s = max(employees.values())
res =  [x for x, salary in employees.items() if salary == max_s]  
print(res)