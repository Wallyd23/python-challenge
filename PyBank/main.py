# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
txtpath = os.path.join('.', 'analysis', 'budget_profit.txt')

total_months = 0
profits_list = []
changes_months = []
changes_list = []
greatest_increase = ["yo momma", 0]
greatest_decrease = ["yo momma", 99999999999999]

# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    csv_row = next(csvreader)
    total_months = total_months + 1
    profits = int(csv_row[1])
    profits_list.append(profits)
    previous = int(csv_row[1])

    # Read each row of data after the header
    for row in csvreader:
        total_months = total_months + 1
        profits = int(row[1])
        profits_list.append(profits)
        change = profits - previous
        changes_list.append(change)
        previous = int(row[1])
        changes_months.append(row[0])
        if change > greatest_increase[1]:
            greatest_increase[1] = change
            greatest_increase[0] = row[0]

        if change < greatest_decrease[1]:
            greatest_decrease[1] = change
            greatest_decrease[0] = row[0]
    avg_change = sum(changes_list) / len(changes_list)   
    total_profit = sum(profits_list)
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: {avg_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)
with open(txtpath,"w") as txtfile:
    txtfile.write(output)
    print(output)

    
        


# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)