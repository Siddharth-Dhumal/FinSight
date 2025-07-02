import csv
import os

current_directory = os.path.dirname(__file__)
csv_path = os.path.join(current_directory, '..', 'data', 'transactions.csv')

with open(csv_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    print("📊 Your Transactions")
    print("-" * 50)

    for row in reader:
        date = row['Date']
        description = row['Description']
        amount = float(row['Amount'])
        category = row['Category']

        print(f"{date} | {description:<20} | ${amount:>7.2f} | {category}")