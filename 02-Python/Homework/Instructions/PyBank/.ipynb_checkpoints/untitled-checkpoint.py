# Import the pathlib and csv library
import os
import sys
from pathlib import Path
import csv 

# Set the file path
csvpath = Path(os.path.join(sys.path[0], 'Resources/budget_data.csv'))

# Initializatione
records = []
numMonths = 0
profit_total = 0
maxMonthlyProfitibility = None
minMonthlyProfitability = None
previousMonthlyProfit = None
monthlyProfitChange = 0
totalMonthlyProfitChange = 0
# method 1
minMonthlyChange = float("inf")
minChangeMonth = ""
# method 2
maxMonthlyChange = [-float("inf"), ""]


# Open the csv file as an object
with open(csvpath, 'r') as csvfile:
        
    # Read header
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
    
        # print(row)
        
        # Count number of months
        numMonths+= 1
        
        # Calculate total Profit/Loss
        monthlyProfitLoss = int(row[1])
        profit_total += monthlyProfitLoss
        
        # Calculate monthly profit change
        if previousMonthlyProfit is None:
            # we are on the first row
            previousMonthlyProfit = monthlyProfitLoss
            # print("We are on the first row")
            # print(f"previousMonthlyProfit = {previousMonthlyProfit}")
        else: 
            # we are not on the first row
            # print("We are not on the first row")
            # print(f"previousMonthlyProfit = {previousMonthlyProfit}")
            monthlyProfitChange = monthlyProfitLoss - previousMonthlyProfit
            previousMonthlyProfit = monthlyProfitLoss
        
        # comment
        # Calculate min / max Monthly Change

        # method 1
        if monthlyProfitChange < minMonthlyChange:
            minMonthlyChange = monthlyProfitChange
            minChangeMonth = row[0]
        
        # method 2
        maxMonthlyChange = max(maxMonthlyChange, [monthlyProfitChange, row[0]])

        totalMonthlyProfitChange += monthlyProfitChange
        # print(monthlyProfitChange)
        # print(totalMonthlyProfitChange)
        
# Average P/L
averagePnl = round(profit_total / numMonths, 2)

# Average monthly profit change
averageMonthlyProfitChange = round(totalMonthlyProfitChange / (numMonths - 1), 2)

# Print results
print("Financial Analysis")
print("-" * 25)
print("Total Months:", numMonths)
print("Total: $", profit_total, sep="")
print(f"Average Change: ${averageMonthlyProfitChange}")
 
# C-style formatting
("My digit: %d, my string %s" % (5, "five"))
# .format() method
("My digit: {}, my string {}".format(5, "five"))
# f-string
(f"My digit: {5}, my string {'five'}")

print("Greatest increase in profits: {} (${})".format(maxMonthlyChange[1], maxMonthlyChange[0]))
print(f"Greatest decrease in profits: {minChangeMonth} (${minMonthlyChange})")
