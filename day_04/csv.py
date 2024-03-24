import csv

csv_path = "sample.csv"
csv_file = open(csv_path, "r", encoding="utf-8")
csv_data = csv.DictReader(csv_file)
for row in csv_data:
    print(row)
