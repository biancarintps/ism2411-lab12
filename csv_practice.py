import csv

# Comparison: csv.reader gives each row as a list, so you access values by index
# which is fine for quick scripts. csv.DictReader uses the header names
# which is clearer and safer when columns have names or might get reordered.

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