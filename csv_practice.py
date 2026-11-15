# 1. Compared to Excel, Python is better for repeating the same task fast and on big files. I can write the steps once and run them every time without clicking around. Excel is easier for quickly looking at data and making charts, so it is better for small one-time work.
#
# 2. A store could use an append-mode log to record every sale or every time a report runs. Append mode is the right tool because it adds a new line each time instead of erasing the old ones, so you keep a full history.


import csv
from datetime import datetime

# ------Exercise 1------
with open("data/sales.csv", "r") as f:
    print("Opened OK")

# --------Exercise 2--------
print("\n--- Exercise 2 ---")
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ------Exercise 3------
print("\n--- Exercise 3 ---")
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        print(row)

# -------Exercise 4-------
print("\n--- Exercise 4 ---")
total_revenue = 0
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        total_revenue += line_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")

# -----Exercise 5------
print("\n--- Exercise 5 ---")
total_rows = 0
written_rows = 0
with open("data/sales.csv", "r") as infile, open("data/cleaned.csv", "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in reader:
        total_rows += 1
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        if line_total > 100:
            writer.writerow([product, f"{price:.2f}", quantity, f"{line_total:.2f}"])
            written_rows += 1
print(f"Rows written: {written_rows}")
print(f"Rows in original: {total_rows}")

# Exercise 6: csv.DictReader
# csv.reader gives each row as a list, so you use an index like row[1], which is fine for quick scripts.
# csv.DictReader uses the column names like row["price"], which is clearer and safer if columns get reordered.
print("\n--- Exercise 6 ---")
total_revenue = 0
with open("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        line_total = price * quantity
        total_revenue += line_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")

# --------Exercise 7-------
print("\n--- Exercise 7 ---")
summary = {}
with open("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        line_total = float(row["price"]) * int(row["quantity"])
        if product in summary:
            summary[product] += line_total
        else:
            summary[product] = line_total
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

# ---------Exercise 8-------
print("\n--- Exercise 8 ---")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("data/run_log.txt", "a") as log:
    log.write(f"{timestamp} - Total revenue: ${total_revenue:.2f}\n")
print(f"Logged total revenue: ${total_revenue:.2f}")