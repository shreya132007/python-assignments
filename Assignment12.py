"""
Write a Python program to count the total number of rows in a CSV file
"""

import csv

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['ID', 'Name', 'Age'])

    writer.writerow([1, 'Shreya', 19])
    writer.writerow([2, 'Aman', 20])
    writer.writerow([3, 'Riya', 18])

print("CSV file created successfully!")


with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    row_count = sum(1 for row in reader)

print("Total number of rows (including header):", row_count)

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    row_count = sum(1 for row in reader)

print("Total number of data rows (excluding header):", row_count)