#import libraries
import os
import csv
import pandas as pd



#create data frame 
csv_path = os.path.join('Resources', 'week-3-python_homework_PyBank_Resources_budget_data.csv')

bank_df = pd.read_csv(csv_path, low_memory=False)

#calculating results

tot_months=bank_df["Date"].count()
total=bank_df["Profit/Losses"].sum()
start_price = bank_df.iloc[0,1]
end_price = bank_df.iloc[tot_months-1,1]
avg_price = (end_price-start_price)/(tot_months-1)

#Looping through the data
dec = 0.00
inc= 0.00

for i in range(tot_months):
    diff =  bank_df.iloc[i,1] - bank_df.iloc[i-1,1]
    if diff <= dec:
        dec=diff
        month_dec = bank_df.iloc[i,0]
    if diff>= inc:
        inc=diff
        month_inc = bank_df.iloc[i,0]

#printing top line

print("Financial Analysis ")
print("****************************")

#printing results
print(f"Total Months: {tot_months}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_price} ")
print(f"Greatest Increase in Profits: ({month_inc}) ${inc} ")
print(f"Greatest Decrease in Profits: ({month_dec}) ${dec} ")

#writing to file
file1 = open("Output.txt","w") 
file1.write("Financial Analysis \n")
file1.write(f"Total Months: {tot_months} \n")
file1.write(f"Total: ${total} \n")
file1.write(f"Average Change: ${avg_price} \n")
file1.write(f"Greatest Increase in Profits: ({month_inc}) ${inc} \n")
file1.write(f"Greatest Decrease in Profits: ({month_dec}) ${dec} \n")


file1.close()  
