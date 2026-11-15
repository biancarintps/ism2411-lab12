import csv

summary = {}

with open("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        line_total = price * quantity

        if product in summary:
            summary[product] += line_total
        else:
            summary[product] = line_total

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")