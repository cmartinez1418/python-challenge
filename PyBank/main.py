# Dependencies
import os
import csv
budget_csv = os.path.join('Resources', 'budget_data.csv')


months = []
total = []
average = [] 
differences = []
greatest_increase = []
greatest_loss = []

# Titles
print("Financial Analysis")
print("------------------------")

# Total number of months included in the dataset
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
       months.append(row[0])
       
       total.append(int(row[1]))

       
print("Total Months: " + str(len(months)))

# Net total amount of profit/losses over period
net_profit = sum(total)
print("Total: $" + str(net_profit))


# average of differences
sum_differences = 0
prevNum = 0
for index, number in enumerate(total):
    if index != 0:
        sum_differences =  sum_differences  + (number - total[index-1])
        differences.append(number - total[index-1])


average_diff = sum_differences / (len(months)-1)
print("Average Change: $" + str(round(average_diff, 2)))


# greatest increase in profits (date and amount)
max_diff = -100000000
max_index = -1
for index, difference in enumerate(differences):
    if difference > max_diff:
        max_diff = difference
        max_index = index
        
greatest_increase.append(max_diff)

print("Greatest Increase in Profits: " + str(months[max_index + 1]) + " ($" + str(max_diff) + ")")

# greatest loss in profits (date and amount)
min_diff = 100000000
min_index = -1
for index, difference in enumerate(differences):
    if difference < min_diff:
        min_diff = difference
        min_index = index

greatest_loss.append(min_diff)

print("Greatest Decrease in Profits: " + str(months[min_index +1]) + " ($" + str(min_diff) + ")")

#zipped_csv = zip(months, total, average, differences, greatest_increase, greatest_loss)

output_file = os.path.join("Analysis", "PyBank_final.csv")
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Total Months", "Total", "Average Change", "Greatest Increase", "Greatest Decrease"])
    
    writer.writerow([months, total, average, differences, greatest_increase, greatest_loss])