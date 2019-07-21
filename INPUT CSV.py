import csv
import sys

scriptDir = sys.path[0]

with open('ITEMS.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
