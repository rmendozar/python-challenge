# You will be give a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# Dependencies
import pandas as pd
import numpy as np
import os



# Load in File from resources
# PyBank_Data.csv'

csvpath = os.path.join("Resources", "PyBall_Data.csv")
# Import the PyBall_Data.csv file as a DataFrame
df = pd.read_csv(csvpath, encoding="ISO-8859-1")
# Read and display with pandas
df=df.rename(columns={"Voter ID": "Votes"})
df.head(10)


# The total number of votes cast
Total_Voters = len(df['Votes'].value_counts())
Total_Voters = format(Total_Voters, ',.0f')
Total_Voters


# A complete list of candidates who received votes
grouped = df.groupby("Candidate",as_index=False).count()
grouped

# The percentage of votes each candidate won
# The total number of votes each candidate won

grouped = df.groupby(["Candidate"])[['Votes']].count()
grouped['% of Total'] = grouped.Votes / grouped.Votes.sum()
grouped = grouped.sort_values('% of Total',ascending=False)
grouped.reset_index(inplace=True)

format_dict = {"Votes":'${0:,.0f}',"% of Total": '{:.2%}'}
style=grouped.style.format(format_dict)

from IPython.display import display
display(style)

Khan = grouped.loc[grouped['Candidate'] == "Khan", :].to_string(index=False,header=None)
Correy = grouped.loc[grouped['Candidate'] == "Correy", :].to_string(index=False,header=None)
Li = grouped.loc[grouped['Candidate'] == "Li", :].to_string(index=False,header=None)
OTooley = grouped.loc[grouped['Candidate'] == "O'Tooley", :].to_string(index=False,header=None)



# The winner of the election based on popular vote.
winner = grouped.loc[grouped['Votes'] == grouped['Votes'].max()]
winner.reset_index(inplace=True)
winner = winner['Candidate'].to_string()
winner = winner.split('    ')[1]
winner


print(f''' ===============================
        \n         Election Results:
        \n ===============================
        \n Total Votes: {Total_Voters}
        \n ===============================
        \n winner: {winner}
        \n ===============================
         \n      Results by candidate:''')
    
from IPython.display import display
display(style)


file = "PyBall.csv" 
f = open('PayBall.csv','w')
f.write("===============================")
f.write("\n         Election Results:")
f.write("\n ===============================")
f.write("\n Total Votes:"+ Total_Voters +"   " )  
f.write("\n ===============================")
f.write("\n winner: " + winner)
f.write("\n ===============================")
f.write("\n      Results by candidate:")
f.write("\n"+Khan)
f.write("\n"+Correy)
f.write("\n"+Li)
f.write("\n"+OTooley)


f.close()

