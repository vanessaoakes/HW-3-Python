import csv
import os
cvspath = os.path.join('budget_data.csv')

total_months = -1

total_profit_losses = 0

average_change = 0
previous_profit_loss = 0

greatest_increase = 0
greatest_decrease = 0

greatest_increase_month = "Month not found. "
greatest_decrease_month = "Month not found. "

with open(cvspath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #print(csvreader)
  #Loop
    for row in csvreader:
        #print(row)

#The total number of months included in the dataset
        total_months = total_months + 1
        if total_months == 0:
            continue
        #("Total Months: " + str(total_months))

#The total net amount of "Profit/Losses" over the entire period
        profit_loss = int(row[1])
        total_profit_losses += profit_loss
        #print("Profit/Losses: " + str(total_profit_losses))

        if total_months == 1:
            previous_profit_loss = profit_loss
            continue

#The average change in "Profit/Losses" between months over the entire period
        profit_change = profit_loss - previous_profit_loss
        average_change += profit_change
        #print("Average Change: " + str(average_change))

#The greatest increase in profits (date and amount) over the entire period

        if profit_change > greatest_increase:
            greatest_increase = profit_change
            greatest_increase_month = (row[0])
        #print("Greatest Increase in Profits: " + greatest_increase_month + " " + "$" + str(greatest_increase))


#The greatest decrease in losses (date and amount) over the entire period
        if profit_change < greatest_decrease:
            greatest_decrease = profit_change
            greatest_decrease_month = (row[0])
        #print ("Greatest Decrease in Profits: " + greatest_decrease_month + " " + "$" + str(greatest_decrease) )

        previous_profit_loss = profit_loss

output = "Financial Analysis\n"
output += "-----------------------\n"
output += "Total Months: " + str(total_months) + "\n"
output += "Total: "  + "$" +str(total_profit_losses)+"\n"
output += "Average Change: "+"$"+ (str(average_change / (total_months - 1)))+"\n"
output += "Greatest Increase in Profits: " + greatest_increase_month + " " + "($" + str(greatest_increase)+")\n"
output += "Greatest Decrease in Profits: " + greatest_decrease_month + " " + "($" + str(greatest_decrease)+")\n"


print(output)

file = open("Vanessa Oakes HMWK #3 - PyBank.txt","w")
file.write(output)

file.close()


#print("Average change: " + str(average_change / (total_months - 1)))
