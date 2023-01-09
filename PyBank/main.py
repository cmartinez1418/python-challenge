# Dependencies
import os
import csv
budget_csv = os.path.join('Resources', 'budget_data.csv')


months = []
total = []
average = []
sum_differences = 0 
differences = []
max_diff = -100000000


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

       
print("Total months: " + str(len(months)))

# Net total amount of profit/losses over period
net_profit = sum(total)
print("Total: $" + str(net_profit))


# average of differences
prevNum = 0
for index, number in enumerate(total):
    if index != 0:
        sum_differences =  sum_differences  + (number - total[index-1])
        differences.append(number - total[index-1])


average_diff = sum_differences / (len(months)-1)
print(round(average_diff, 2))


# greatest increase in profits (date and amount)
max_index = -1
for index, difference in enumerate(differences):
    if difference > max_diff:
        max_diff = difference
        max_index = index
print(max_diff)
print(max_index + 1)

print(months[max_index + 1])

min_diff = 100000000
# greatest loss in profits (date and amount)
min_index = -1
for index, difference in enumerate(differences):
    if difference < min_diff:
        min_diff = difference
        min_index = index

print(min_diff)
print(months[min_index +1])
