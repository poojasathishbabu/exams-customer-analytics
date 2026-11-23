def test_no_pii():
    import pandas as pd
    df=pd.read_csv("data/cleaned_tickets.csv")
    assert "Customer Email" not in df.columns
    assert "Customer Name" not in df.columns
    print("PASS no PII")
def test_csat_not_filled():
    import pandas as pd
    df=pd.read_csv("data/cleaned_tickets.csv")
    # Open tickets must still have NaN CSAT - we did NOT mean-fill
    assert df.loc[df["Ticket Status"]=="Open","Customer Satisfaction Rating"].isna().all()
    print("PASS CSAT not mean-filled")
if __name__=="__main__": test_no_pii(); test_csat_not_filled()
