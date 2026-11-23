"""Project 1 - Clean
Rule: Missing is NOT random. Resolution/CSAT missing in 5700 rows = Open+Pending, so do NOT mean-fill.
PII: Drop Name/Email/Description. Resolution filled as label 'Not Resolved - Pending'.
Run: python src/clean.py  (expects raw file at data/raw/customer_support_tickets.csv, writes data/cleaned_tickets.csv)
"""
import pandas as pd
def clean(inp="data/raw/customer_support_tickets.csv", out="data/cleaned_tickets.csv"):
    df=pd.read_csv(inp)
    df["Date of Purchase"]=pd.to_datetime(df["Date of Purchase"], errors="coerce")
    df["First Response Time"]=pd.to_datetime(df["First Response Time"], errors="coerce")
    df["Time to Resolution"]=pd.to_datetime(df["Time to Resolution"], errors="coerce")
    df=df.drop(columns=["Customer Name","Customer Email","Ticket Description"], errors="ignore")
    df["Resolution"]=df["Resolution"].fillna("Not Resolved - Pending")
    df["Is_Closed"]=(df["Ticket Status"]=="Closed").astype(int)
    df["Resolution_Hours"]=((df["Time to Resolution"]-df["First Response Time"]).dt.total_seconds()/3600).clip(0,200)
    df.to_csv(out, index=False)
    print(f"cleaned {len(df)} rows -> {out}")
    return df
if __name__=="__main__": clean()
