
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("Cleaned_Superstore.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Calculate summary
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()

sales_category = df.groupby("Category")["Sales"].sum()
profit_category = df.groupby("Category")["Profit"].sum()
monthly_sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Sales"].sum()

# Find top category
top_category = sales_category.idxmax()

# Generate text report
with open("summary_report.txt", "w") as file:
    file.write("SUPERSTORE SALES REPORT\n")
    file.write("=======================\n")
    file.write(f"Total Sales: ${total_sales:,.2f}\n")
    file.write(f"Total Profit: ${total_profit:,.2f}\n")
    file.write(f"Unique Orders: {total_orders}\n")
    file.write(f"Top Sales Category: {top_category}\n")

print("Report generated: summary_report.txt")

# 1. Sales by category
sales_category.plot(kind="bar", title="Sales by Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.close()

# 2. Profit by category
profit_category.plot(kind="bar", title="Profit by Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.close()

# 3. Monthly sales
monthly_sales.index = monthly_sales.index.astype(str)
monthly_sales.plot(kind="line", marker="o",
                   title="Monthly Sales Trend")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.close()

print("All charts generated successfully!")
