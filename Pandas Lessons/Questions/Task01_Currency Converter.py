from operator import index
from random import choice
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/currency.csv")

print(df)

#write a program that:
#   lets the user enter a date
#   validates the date input
#   lets the user enter a currency conversion
#   validates the currency input
#   shows the user their chosen conversion rate
#       on their chosen day
#   repeats

earliest = "18/12/2020"
latest = "16/03/2021"

conversions = ["GBP - EUR","EUR - GBP","GBP - AUD","AUD - GBP","GBP - JPY","JPY - GBP"]

dateInput = input(f"Enter a date between {earliest} and {latest}\nmust be in the format 'DD/MM/YYYY': ")

print("Here are the options")
for index in range(len(conversions)):
    print(f"{index}: {conversions[index]}")


choice = int(input("Enter your choice: "))
conversion = conversions[choice]

# Condition that selects the date we want
dfSelectDate = df[df["Date"] == dateInput]
dfSelectCurrency = dfSelectDate[conversion]
print(dfSelectCurrency)

#write a program that:
#   lets the user enter a currency conversion
#   validates the currency input
#   plots a graph of dates against conversion rates

x = df["Date"]
y = df[conversion]
plt.title(conversion)
plt.xlabel("Dates")
plt.ylabel("Conversion Rates")
plt.plot(x,y)
plt.show()