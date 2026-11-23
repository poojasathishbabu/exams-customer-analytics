"""Project 1 - Analysis: CSAT on Closed only"""
import pandas as pd
df=pd.read_csv("data/cleaned_tickets.csv")
print("Closed rate:", round((df["Ticket Status"]=="Closed").mean()*100,1), "%")
print("CSAT Closed only:", round(df.loc[df["Ticket Status"]=="Closed","Customer Satisfaction Rating"].mean(),2))
print(df.groupby("Ticket Channel")["Customer Satisfaction Rating"].mean().round(2))
print(df.groupby("Ticket Type").size())
