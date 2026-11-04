# Employee Data Analyzer

## Project Overview
A Python/Pandas project that loads employee data from CSV, cleans duplicate and missing values, calculates salary statistics, performs department-wise grouping, filters salaries, and displays a Matplotlib chart.

## Files
- `one.py` - complete project code in one Python file
- `employees.csv` - supporting CSV data
- `README.md` - project documentation
- `TEST_CASE_SCREENSHOTS.pdf` - test execution report
- `test_case_1.png` through `test_case_4.png` - individual execution captures

## Requirements
Python 3.x, Pandas, Matplotlib.

Install:
```bash
pip install pandas matplotlib
```

## Run
Keep `one.py` and `employees.csv` in the same folder. In VS Code Terminal:
```bash
python one.py
```

## Features
1. Employee summary: count, average salary, highest-paid employee, total payroll.
2. Department-wise employee count and average salary.
3. Salary filtering.
4. Display all cleaned employees.
5. Department-wise average salary bar chart.
6. Duplicate removal and missing-salary filling using the mean.

## CSV Format
```csv
Emp_ID,Name,Department,Salary,Experience
E1,Aman,IT,50000,3
E2,Riya,HR,40000,2
E3,Karan,IT,70000,5
```

## Test Cases

### Test Case 1 - Normal Input
Three employees:
- E1 Aman IT 50000
- E2 Riya HR 40000
- E3 Karan IT 70000

Expected:
- Employees: 3
- Average salary: 53333.33
- Highest paid: Karan (70000)
- Total payroll: 160000

### Test Case 2 - Boundary / Minimum Input
One employee:
- E1 Aman IT 50000

Expected:
- Employees: 1
- Average salary: 50000.00
- Highest paid: Aman (50000)
- Total payroll: 50000

### Test Case 3 - Invalid Input
Use one duplicate E1 row and one missing salary for Neha:
```csv
Emp_ID,Name,Department,Salary,Experience
E1,Aman,IT,50000,3
E1,Aman,IT,50000,3
E4,Neha,HR,,4
E2,Riya,HR,40000,2
E3,Karan,IT,70000,5
```
Expected:
- Duplicates removed: 1
- Missing salary filled with mean: 53333.33
- Cleaned rows: 4

### Test Case 4 - Different Valid Scenario
Use the normal three-employee data. Select menu option `2` and enter salary limit `45000`.
Expected:
- HR: 1 employee, average 40000
- IT: 2 employees, average 60000
- Filtered: Aman and Karan
- Menu option `4` opens the department-wise average salary chart.

## Testing Procedure
For each test:
1. Stop the previous run with `Ctrl+C`.
2. Put that test's data in `employees.csv`.
3. Save the CSV.
4. Run `python one.py`.
5. Select the required menu option.
6. Compare the output with the expected result.
7. Capture a clear screenshot showing the input/output.
8. Keep all captures in the submission PDF.

## Submission Checklist
- [x] one.py
- [x] README.md
- [x] employees.csv
- [x] TEST_CASE_SCREENSHOTS.pdf
- [x] Individual PNG execution captures

Before GitHub submission, run all tests yourself and replace any sample captures with your own VS Code screenshots if your instructor specifically requires literal screenshots from your computer.
