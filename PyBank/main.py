# Worked on this section of the assignment with the study group Stuart Smith and Tim Smith
# Create the file path across operating systems
import os

# The module for reading csv file
import csv

# The path for the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Use the Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
 
    # Initialize the variable for # of months to zero
    count_month=0
    # Initialize the variable for Profit/Loss value to zero
    ProfitLoss = 0
    # Initialize the variable for Greatest Increase in Profit value to zero
    GreatestProfit=0
    # Initialize the variable for Greatest Decrease in Profit value to zero
    GreatestLoss=0
    # Initialize the variable for last month's profit/loss value to zero
    lastmonthPL=0
    # Initialize the variable for change value to zero
    change=0
    # Initialize the variable for total change of profit/loss value to zero
    totalchangesPL=0

    # Read each row of data after the header
    for row in csvreader:

        # If it is the first month, save the Profit/Loss value in column 2
        if count_month ==0:
            PLfirstmonth = int(row[1])
            
        # Calculate the total number of months in the data set
        count_month+=1

        # Calculate the net total amount of Profit/Losses over the entire period
        ProfitLoss+=int(row[1])

        # Calculate the Profit/Loss change month over month
        change = int(row[1]) - int(lastmonthPL)

        # Add the Profit/Loss changes and keep a running total of all the Profit/Loss changes
        totalchangesPL+=change
        
        # If change is less than the greatest loss value, save it as GreatestLoss and save the month and year
        if change < int(GreatestLoss):
            GreatestLoss = change
            GreatestLossDate = row[0]

        # If change is greater than the greatest profit value, save it as GreatestProfit and save the month and year
        if change > int(GreatestProfit):
            GreatestProfit = change
            GreatestProfitDate = row[0]

        # Save the current Profit/Loss value as last month to calculate the next Profit/Loss change
        lastmonthPL = row[1]

# Calculate the changes in the "Profit/Losses" over the entire period, then find the average of those changes        
# Calculate the average monthly change
avg_change = (totalchangesPL-PLfirstmonth)/(count_month-1)

print(f'Financial Analysis')
print(f'----------------------------')
# Print the total number months included in the data set
print(f'Total Months: {count_month}')
# Print the net total amount of "Profit/Losses" over the entire period
print(f'Total: ${ProfitLoss}')
# Print the average montly "Profit/Losses" over the entire period
print(f'Average Change: ${round(avg_change,2)}')
# Print the greatest increase in profits (date and amount) over the entire period
print(f'Greatest Increase in Profits: {GreatestProfitDate} (${GreatestProfit})')
# Print the greatest decrease in profits (date and amount) over the entire period
print(f'Greatest Decrease in Profits: {GreatestLossDate} (${GreatestLoss})')

# Learnt to write text files with Tim Smith in study group
# Reviewed website (https://www.pythontutorial.net/python-basics/python-write-text-file/#:~:text=To%20write%20to%20a%20text%20file%20in%20Python%2C,close%20the%20file%20using%20the%20close%20%28%29%20method)
# Specify the file to write to
output_path = os.path.join("analysis", "PyPollAnalysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as f:

   # Write the results that were printed earlier to the text file
    f.write(f'Financial Analysis \n')
    f.write(f'---------------------------- \n')
    f.write(f'Total Months: {count_month} \n')
    f.write(f'Total: ${ProfitLoss} \n')
    f.write(f'Average Change: ${round(avg_change,2)} \n')
    f.write(f'Greatest Increase in Profits: {GreatestProfitDate} (${GreatestProfit}) \n')
    f.write(f'Greatest Decrease in Profits: {GreatestLossDate} (${GreatestLoss}) \n')

