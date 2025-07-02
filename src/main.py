import csv
import os
from collections import defaultdict

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