import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/flights.csv")

print(df)

df = df.columns.tolist()
starts = df["From"]
ends = df["To"]

print(starts, ends)