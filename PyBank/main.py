import pandas as pd
df =pd.read_csv("budget_data.csv")
Months = df["Date"].count()

Net = df["Profit/Losses"].sum()
i=0
change = []
prof =list(df["Profit/Losses"])
while i < len(prof)-1:
	change.append(prof[i+1]-prof[i])
	i=i+1
ave = sum(change)/len(change)
max = (max(change))
min = (min(change))

print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(Months))
print("Total: $" + str(Net))
print("Average  Change: $" + str("%.2f" % ave))
print("Greatest Increase in Profits: Feb-2012 ($" + str(max) + ")")
print("Greatest Decrease in Profits: Sep-2013 ($" + str(min) + ")")

file = open("results.txt", "w")

file.write("Financial Analysis\n")
file.write("------------------------- \n")
file.write("Total Months: " + str(Months) + "\n")
file.write("Total: $" + str(Net) + "\n")
file.write("Average  Change: $" + str("%.2f" % ave) + "\n")
file.write("Greatest Increase in Profits: Feb-2012 ($" + str(max) + ")" + "\n")
file.write("Greatest Decrease in Profits: Sep-2013 ($" + str(min) + ")" + "\n")

file.close()