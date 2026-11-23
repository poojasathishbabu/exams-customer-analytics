# 01 - Exams / Customer Support Analytics
## Business Problem
8,469 customer support tickets. Which tickets hurt satisfaction? Where is the bottleneck?

## Data
- Source: customer_support_tickets.csv (Kaggle-style, uncleaned)
- Rows: 8,469 | Columns: 17 -> cleaned to 14 (PII removed: Name, Email, Description)
- Key cleaning decisions (see src/clean.py):
  - Resolution / Time to Resolution / CSAT missing in 5,700 rows = NOT imputed with mean. Why? Those are Open + Pending tickets, not missing at random. Filling mean would fake CSAT.
  - Resolution filled as 'Not Resolved - Pending' (label, not value)
  - CSAT kept NaN for open tickets, analysis on Closed only (n=2,769)
  - Resolution_Hours = Time to Resolution - First Response Time, clipped 0-200h

## Key Findings (Evidence)
- Closed rate: Only 32.7% (2,769 / 8,469). 67.3% are Open (2,819) + Pending Customer Response (2,881). Biggest leak = Pending bucket.
- Avg CSAT (Closed only): 2.99 / 5.0 - Flat, not good.
- CSAT by Channel: Chat 3.08 highest, Phone 2.95 lowest. Chat > Phone by 0.13.
- Tickets by Type: Almost equal - Refund 1,752, Technical 1,747, Cancellation 1,695, Product 1,641, Billing 1,634. No single type dominates -> systemic, not one product.
- CSAT by Priority: Almost flat (Low 3.05, Critical 2.96). Priority does NOT explain CSAT.
- Top Product: Canon EOS 240, GoPro Hero 228 - volume, not satisfaction driver.

## Now What (Monday Action)
1. Fix Pending bucket first: Auto-nudge customers after 48h, close or re-assign. Target: Pending 2,881 -> <1,500 in 2 weeks.
2. Move Phone -> Chat playbook: Chat has highest CSAT. Give Phone agents Chat scripts.
3. Do NOT chase Priority: Priority is not the CSAT driver. Chase Status (Open/Pending) instead.
4. Re-check in 1 week: Closed rate, CSAT (Closed only), Pending count.

## How to Run
pip install -r requirements.txt
python src/clean.py
python src/analysis.py
Open dashboard.html for the result dashboard.

## Links (for Resume)
- Link 1 - Repo: github.com/<your-username>/01-exams-customer-analytics
- Link 2 - Live Result Dashboard: <your-dashboard-link> (dashboard.html / Dashboard (HTML) / Streamlit)

## Tests
python src/test_clean.py  # checks no PII + CSAT not mean-filled
