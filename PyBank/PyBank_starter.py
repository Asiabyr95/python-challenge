#importing libraries
import csv
import os

# use absolute path for the files
input_file=os.path.join("Resources","budget_data.csv")
output_file=os.path.join("analysis","financial_analysis.txt")

#initializing all the required variables
total_months=0
net_total=0
changes=[]
dates=[]
previous_profit=None

#reading the csv file
with open(input_file,'r') as csvfile:
    csvreader=csv.reader(csvfile)
    header=next(csvreader)

    # initializing for loop for the required calculations
    for row in csvreader:
        date,profit=row[0],int(row[1])
        total_months += 1
        net_total += profit

        if previous_profit is not None:
            change=profit-previous_profit
            changes.append(change)
            dates.append(date)

        previous_profit=profit

#calculating all the asked questions
average_change=sum(changes)/len(changes)
greatest_increase=max(changes)
greatest_decrease=min(changes)
increase_date=dates[changes.index(greatest_increase)]
decrease_date=dates[changes.index(greatest_decrease)]

# displaying the output in given format
output=(
    "Financial Analysis\n"
    "---------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n"
)

#printing the output
print(output)

with open(output_file,'w') as file:
    file.write(output)

