import pandas as pd
df =pd.read_csv("election_data.csv")
Votes = (df["Voter ID"].count())

#print(df["Candidate"].unique())

K = 0
C = 0
L = 0
O = 0
Can = list(df["Candidate"])
for i in Can:
	if i == "Khan":
		K = K + 1
	if i == "Correy":
		C = C + 1
	if i == "Li":
		L = L + 1
	if i == "O'Tooley":
		O = O + 1
Winner = "Khan"
WinNum = K
if C > WinNum:
	Winner = "Correy"
	WinNum = C
if L > WinNum:
	Winner = "Li"
	WinNum = L
if O > WinNum:
	Winner = "O'Tooley"
	WinNum = O
	
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(Votes))
print("-------------------------")
print("Khan: " + str("%.3f" % (100*(K/Votes))) + "% " + "(" + str(K) + ")")
print("Correy: " + str("%.3f" % (100*(C/Votes))) + "% " + "(" + str(C) + ")")
print("Li: " + str("%.3f" % (100*(L/Votes))) + "% " + "(" + str(L) + ")")
print("O'Tooley: " + str("%.3f" % (100*(O/Votes))) + "% " + "(" + str(O) + ")")
print("-------------------------")
print("Winner: " + Winner)
print("-------------------------")

file = open("results.txt", "w")

file.write("Election Results\n")
file.write("------------------------- \n")
file.write("Total Votes: " + str(Votes) + "\n")
file.write("------------------------- \n")
file.write("Khan: " + str("%.3f" % (100*(K/Votes))) + "% " + "(" + str(K) + ")" + "\n")
file.write("Correy: " + str("%.3f" % (100*(C/Votes))) + "% " + "(" + str(C) + ")" + "\n")
file.write("Li: " + str("%.3f" % (100*(L/Votes))) + "% " + "(" + str(L) + ")" + "\n")
file.write("O'Tooley: " + str("%.3f" % (100*(O/Votes))) + "% " + "(" + str(O) + ")" + "\n")
file.write("------------------------- \n")
file.write("Winner: " + Winner + "\n")
file.write("------------------------- \n")

file.close()