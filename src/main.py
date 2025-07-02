import csv
import os
from collections import defaultdict
import matplotlib.pyplot as plt
import random

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

categories = list(category_totals.keys())
amounts = [abs(total) for total in category_totals.values()]  # Use absolute values for clean display

plt.figure(figsize=(10, 6))

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