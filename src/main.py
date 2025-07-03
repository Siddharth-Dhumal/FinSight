import csv
import os
from collections import defaultdict
import matplotlib.pyplot as plt
import random

monthly_budgets = {
    "Food": 100.00,
    "Transport": 70.00,
    "Subscription": 40.00,
    "Groceries": 150.00,
    "Rent": 1200.00,
    "Utilities": 60.00,
    "Shopping": 50.00
}

current_directory = os.path.dirname(__file__)
csv_path = os.path.join(current_directory, '..', 'data', 'transactions.csv')

category_totals = defaultdict(float)

with open(csv_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    print("Your Transactions")
    print("-" * 50)

    for row in reader:
        date = row['Date']
        description = row['Description']
        amount = float(row['Amount'])
        category = row['Category']

        print(f"{date} | {description:<20} | ${amount:>7.2f} | {category}")

        category_totals[category] += amount

print("\n Spending Summary by Category:")
print("-" * 50)
for category, total in category_totals.items():
    print(f"{category:<15} : ${total:>8.2f}")

print("\nOverspending Alerts:")
print("-" * 50)

overspending_found = False

for category, total in category_totals.items():
    budget = monthly_budgets.get(category)
    if budget is not None and abs(total) > budget:
        overspending_found = True
        print(f"{category}: Spent ${abs(total):.2f} / Budget ${budget:.2f} — Over by ${abs(total) - budget:.2f}")

if not overspending_found:
    print("You stayed within your budget in all categories!")

categories = list(category_totals.keys())
amounts = [abs(total) for total in category_totals.values()]

colors = [plt.cm.tab20(i) for i in range(len(categories))]

plt.figure(figsize=(10, 6))
plt.bar(categories, amounts, color=colors)
plt.title("Spending by Category", fontsize=14)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Amount ($)", fontsize=12)
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()