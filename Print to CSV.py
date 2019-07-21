import csv

with open('OUTPUT.csv', 'a') as f:
   csv_writer = csv.writer(f)
   csv_writer.writerow(["STRING_HERE"])
