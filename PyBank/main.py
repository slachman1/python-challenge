# import modules
import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

row_count = 0
total_amount = 0
previous_amount = 0
total_change = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

with open(csvpath, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        row_count += 1
        date = row[0]  # Assuming the first column contains dates
        amount = int(row[1])  # Assuming the second column contains integers
        total_amount += amount
        if row_count > 1:
            change = amount - previous_amount
            total_change += change
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = date
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date
        previous_amount = amount

average_change = total_change / (row_count - 1)  # Exclude the first row from the calculation

print("Financial Analysis")
print("----------------------")
print(f"Total Months: {row_count}")
print(f"Total Amount: ${total_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
