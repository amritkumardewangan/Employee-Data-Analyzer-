import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------
# EMPLOYEE DATA ANALYZER
# Project: Employee Data Analyzer
# ---------------------------------------------------------

FILE_NAME = "employees.csv"


# ---------------------------------------------------------
# FUNCTION 1: Load and clean employee data
# ---------------------------------------------------------
def load_and_clean_data():
    try:
        df = pd.read_csv(FILE_NAME)

        print("\nOriginal Data:")
        print(df)

        # Remove duplicate rows
        before_duplicates = len(df)
        df = df.drop_duplicates()
        duplicates_removed = before_duplicates - len(df)

        # Convert Salary to numeric
        df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

        # Calculate mean salary using valid salary values
        mean_salary = df["Salary"].mean()

        # Fill missing salaries with mean salary
        df["Salary"] = df["Salary"].fillna(mean_salary)

        # Remove rows with missing important information
        df = df.dropna(subset=["Emp_ID", "Name", "Department"])

        # Convert Experience to numeric
        df["Experience"] = pd.to_numeric(
            df["Experience"], errors="coerce"
        )

        print("\nData cleaned successfully.")

        if duplicates_removed > 0:
            print("Duplicates removed:", duplicates_removed)

        if pd.notna(mean_salary):
            print("Missing salaries filled with mean:",
                  f"{mean_salary:.2f}")

        print("Cleaned rows:", len(df))

        return df

    except FileNotFoundError:
        print("\nERROR: employees.csv file was not found.")
        print("Please keep employees.csv in the same folder as this Python file.")
        return None

    except Exception as e:
        print("\nERROR:", e)
        return None


# ---------------------------------------------------------
# FUNCTION 2: Summary
# ---------------------------------------------------------
def show_summary(df):
    if df.empty:
        print("\nNo employee data available.")
        return

    total_employees = len(df)
    average_salary = df["Salary"].mean()
    total_payroll = df["Salary"].sum()

    highest_salary = df["Salary"].max()
    highest_paid_employee = df.loc[
        df["Salary"].idxmax(), "Name"
    ]

    print("\n========== EMPLOYEE SUMMARY ==========")

    print(f"Employees: {total_employees}")
    print(f"Average salary: {average_salary:.2f}")
    print(
        f"Highest paid: {highest_paid_employee} "
        f"({highest_salary:.0f})"
    )
    print(f"Total payroll: {total_payroll:.0f}")

    print("=======================================")


# ---------------------------------------------------------
# FUNCTION 3: Department-wise analysis
# ---------------------------------------------------------
def department_analysis(df):
    if df.empty:
        print("\nNo employee data available.")
        return

    print("\n========== DEPARTMENT-WISE ANALYSIS ==========")

    department_data = df.groupby("Department").agg(
        Employees=("Emp_ID", "count"),
        Average_Salary=("Salary", "mean")
    )

    for department, row in department_data.iterrows():
        print(
            f"{department}: "
            f"{int(row['Employees'])} employees | "
            f"Avg salary: {row['Average_Salary']:.2f}"
        )

    print("==============================================")


# ---------------------------------------------------------
# FUNCTION 4: Filter employees above salary limit
# ---------------------------------------------------------
def filter_salary(df):
    try:
        limit = float(
            input("\nEnter salary limit: ")
        )

        filtered = df[df["Salary"] > limit]

        print(
            f"\nEmployees with salary above {limit:.0f}:"
        )

        if filtered.empty:
            print("No employees found.")
        else:
            for _, employee in filtered.iterrows():
                print(
                    f"{employee['Name']} - "
                    f"{employee['Department']} - "
                    f"{employee['Salary']:.0f}"
                )

    except ValueError:
        print("\nPlease enter a valid number.")


# ---------------------------------------------------------
# FUNCTION 5: Show employee details
# ---------------------------------------------------------
def show_all_employees(df):
    print("\n========== ALL EMPLOYEES ==========")

    print(
        df[
            [
                "Emp_ID",
                "Name",
                "Department",
                "Salary",
                "Experience"
            ]
        ].to_string(index=False)
    )

    print("===================================")


# ---------------------------------------------------------
# FUNCTION 6: Bar chart
# ---------------------------------------------------------
def show_bar_chart(df):
    if df.empty:
        print("\nNo data available for chart.")
        return

    department_average = (
        df.groupby("Department")["Salary"]
        .mean()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 5))

    department_average.plot(
        kind="bar"
    )

    plt.title("Department-wise Average Salary")
    plt.xlabel("Department")
    plt.ylabel("Average Salary")

    plt.xticks(rotation=0)

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------
def main():

    print("==========================================")
    print("       EMPLOYEE DATA ANALYZER")
    print("==========================================")

    # Load and clean CSV
    df = load_and_clean_data()

    if df is None:
        return

    while True:

        print("\n")
        print("========== MENU ==========")
        print("1. Employee Summary")
        print("2. Department-wise Analysis and Salary Filter")
        print("3. Show All Employees")
        print("4. Show Department-wise Bar Chart")
        print("5. Exit")
        print("==========================")

        choice = input("Enter your choice: ")

        if choice == "1":

            # Summary
            show_summary(df)

        elif choice == "2":

            # Department-wise analysis
            department_analysis(df)

            # Salary filtering
            filter_salary(df)

        elif choice == "3":

            show_all_employees(df)

        elif choice == "4":

            show_bar_chart(df)

        elif choice == "5":

            print("\nThank you for using Employee Data Analyzer!")
            break

        else:

            print("\nInvalid choice.")
            print("Please enter a number from 1 to 5.")


# ---------------------------------------------------------
# PROGRAM START
# ---------------------------------------------------------
if __name__ == "__main__":
    main()