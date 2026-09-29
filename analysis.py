import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "data/hr_employee_data.csv"
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_FILE)

print("\n===== HR EMPLOYEE ANALYTICS =====")
print("Total employees:", len(df))
print(f"Average monthly salary: ₹{df["Monthly_Salary"].mean():,.0f}")
print(f"Average age: {df["Age"].mean():.1f} years")
print(f"Average experience: {df["Experience_Years"].mean():.1f} years")

dept = df.groupby("Department").agg(
    Employees=("Employee_ID","count"),
    Average_Salary=("Monthly_Salary","mean"),
    Average_Experience=("Experience_Years","mean")
).sort_values("Employees", ascending=False)

print("\n--- Department Summary ---")
print(dept.round(1))

top10 = df.nlargest(10, "Monthly_Salary")[
    ["Employee_ID","Employee_Name","Department","Job_Role","Monthly_Salary"]
]
print("\n--- Top 10 Highest-Paid Employees ---")
print(top10.to_string(index=False))

dept.round(1).to_csv(os.path.join(OUTPUT_DIR,"department_summary.csv"))
top10.to_csv(os.path.join(OUTPUT_DIR,"top_10_highest_paid.csv"),index=False)

plt.figure(figsize=(9,5))
df.groupby("Department")["Monthly_Salary"].mean().sort_values().plot(kind="barh")
plt.title("Average Monthly Salary by Department")
plt.xlabel("Average Salary (₹)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR,"average_salary_by_department.png"))
plt.close()

plt.figure(figsize=(8,5))
df["Department"].value_counts().plot(kind="bar")
plt.title("Employees by Department")
plt.xlabel("Department"); plt.ylabel("Number of Employees")
plt.xticks(rotation=0); plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR,"employees_by_department.png"))
plt.close()

plt.figure(figsize=(8,5))
plt.scatter(df["Experience_Years"],df["Monthly_Salary"],alpha=0.7)
plt.title("Experience vs Monthly Salary")
plt.xlabel("Experience (Years)"); plt.ylabel("Monthly Salary (₹)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR,"experience_vs_salary.png"))
plt.close()

print("\nAnalysis complete. Results saved in outputs/.")
