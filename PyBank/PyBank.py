# Dependencies
import pandas as pd
import locale
import os

# Load in File from resources
# PyBank_Data.csv'

csvpath = os.path.join("Resources", "PyBank_Data.csv")
# Import the PyBank_Data.csv file as a DataFrame
df = pd.read_csv(csvpath, encoding="ISO-8859-1")
# Read and display with pandas
df.head(10)

# The total number of months included in the dataset

Total_Months = len(df['Date'].value_counts())
Total_Months

# The net total amount of "Profit/Losses" over the entire period

Total_Profit = df['Profit/Losses'].sum()
Total_Profit = ('$' + format(Total_Profit, ',.2f'))

#df = df.set_index('Date')
#df.head()

# The average of the changes in "Profit/Losses" over the entire pe#riod
df['OTM'] = df['Profit/Losses'] - df['Profit/Losses'].shift(1)
#df['OTY'] = df['Profit/Losses'] - df['Profit/Losses'].shift(12)
average_OTM_change = df['OTM'].mean()
average_OTM_change = ('$' + format(average_OTM_change, ',.2f'))
#average_OTY_change = df['OTY'].mean()
#average_OTY_change

# The greatest increase in profits (date and amount) over the entire period
Max_change = df['OTM'].max()
date_max = df.loc[df['OTM'] == Max_change, 'Date'].to_string()
date_max=(date_max.split(' ', ))
date_max=date_max[4]
Max_change = ('$' + format(Max_change, ',.2f'))
Max = date_max + '   ' + Max_change


# The greatest decrease in losses (date and amount) over the entire period
Min_change = df['OTM'].min()
date_min = df.loc[df['OTM'] == Min_change, 'Date'].to_string()
date_min=(date_min.split(' ', ))
date_min=date_min[4]
Min_change = ('$' + format(Min_change, ',.2f'))
Min = date_min + '   ' + Min_change


Results = {'Total Months':int(Total_Months),
          'Total Profits':Total_Profit,
           'Average Monthly Change':average_OTM_change,
           'Greatest Monhtly Increase':Max,
           'Greatest Monthly decrease':Min
          }
Results

df_final=pd.DataFrame.from_dict(Results,orient='index', columns=['Finnacial Summary'])
df_final

df_final.to_csv("PyBank_Summary.csv", index=True, header=True)