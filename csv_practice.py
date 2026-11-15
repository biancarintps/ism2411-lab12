import csv
from datetime import datetime

total_revenue = 0

with open("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total_revenue += price * quantity

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as log:
    log.write(f"{timestamp} - Total revenue: ${total_revenue:.2f}\n")

print(f"Logged total revenue: ${total_revenue:.2f}")