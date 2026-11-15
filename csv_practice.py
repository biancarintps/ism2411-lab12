# 1. Compared to Excel, Python is better for repeating the same task fast and on big files. I can write the steps once and run them every time without clicking around. Excel is easier for quickly looking at data and making charts, so it is better for small one-time work.
#
# 2. A store could use an append-mode log to record every sale or every time a report runs. Append mode is the right tool because it adds a new line each time instead of erasing the old ones, so you keep a full history.


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