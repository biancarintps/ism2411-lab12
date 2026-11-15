import csv

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