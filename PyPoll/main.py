import pandas as pd
df =pd.read_csv("election_data.csv")
Votes = (df["Voter ID"].count())

Candidates = df["Candidate"].unique()

K = 0
C = 0
L = 0
O = 0
Can = list(df["Candidate"])
for i in Can:
	if i == Candidates[0]:
		K = K + 1
	if i == Candidates[1]:
		C = C + 1
	if i == Candidates[2]:
		L = L + 1
	if i == Candidates[3]:
		O = O + 1
Winner = Candidates[0]
WinNum = K
if C > WinNum:
	Winner = Candidates[1]
	WinNum = C
if L > WinNum:
	Winner = Candidates[2]
	WinNum = L
if O > WinNum:
	Winner = Candidates[3]
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