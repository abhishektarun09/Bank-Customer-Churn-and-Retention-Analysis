# Bank Customer Churn and Retention Analysis

### Optimizing Customer Lifetime Value in Nigerian Retail Banking

This project analyzes churn patterns within a major Nigerian financial institution to identify behavioral, demographic, and product-level drivers of attrition. By leveraging SQL, modular Python code and statistical modeling, the goal is to provide actionable insights for relationship managers and product teams to increase customer "stickiness."

## Business Problem
The bank is facing an increasing churn rate. To protect the bottom line, this analysis seeks to answer:

- Behavioral Drivers: Which specific actions (or lack thereof) precede a customer closing their account?

- Digital Adoption: Does the usage of mobile apps and digital banking reduce churn?

- FX Loyalty: Are customers holding domiciliary (USD/GBP/EUR) accounts more loyal and profitable than Nigerian Naira-only customers?

## Key Insights
1. The Baseline & Risk Profile
    - Overall Churn Rate: The bank is experiencing a significant churn rate of 53.97%.
    - Primary Risk Segment: High-risk customers are the most volatile, accounting for 18.31pp more on average than Medium and Low Risk Customers.
    - The "Tenure" Myth: There is nearly zero correlation between account age (Tenure) and active usage. Older accounts are just as likely to churn as newer ones, suggesting that loyalty is not built over time alone.

2. The "Stickiness" Factor: Credit Cards
    - Massive Disparity: Customers with credit cards have a churn rate of only 0.04%, compared to 53.93% for those without.
    - Projected Impact: Targeted promotion of credit cards to non-cardholders is estimated to reduce the overall churn rate.

3. The Digital Paradox
    - Negative Correlation: Contrary to expectations, higher digital adoption currently correlates with higher churn.
    - Channel Fatigue: Customers utilizing all three digital channels (Mobile App, Internet Banking, and USSD) represent the highest volume of churn, with USSD-only accounts having highest churn.

4. FX/Domiciliary Customer Volatility
    - Profitability vs. Loyalty: Foreign Currency (FX) customers are the bank's most profitable yet most disloyal segment.
    - Balance Disparity: USD account holders maintain an average balance 19x higher than local NGN customers.
    - Attrition Rates: Churn is significantly higher in FX segments: GBP (74.4%), USD (71.1%), and EUR (68.0%), compared to NGN (53.6%).
    - Statistical Proof: A Chi-Square test of independence (p < 0.01) confirmed that currency type is a statistically significant driver of churn.


## Dataset Overview
- Source: The data-set was obtained from a multinational bank with branches in Nigeria and across Africa. It was generated in 2023.
- Description: The data-set contains 19 variables and 500,000 rows. It is part of a larger data-set of over 20 million records

- Target Variable: churn (Binary: 1 if churned, 0 if retained)


- Key Features:

  - Financials: Average Balance, Risk Rating, Currency, 

  - Engagement: Credit Card, Tenure, Scheme, Credit & Debit Value, Credit & Debit Volume

  - Digital banking: Mobile App, Internet banking, USSD Banking

  - New Engineered Features: Digital Channels Usage

- Data Cleaning
  - Changed column names to lower case and renamed columns
  - Cleaned rows from Average Balance, Debit Value, and Credit Value column.
  - Replaced Y with 1 and N with 0 in categorical columns.

Link : https://rpubs.com/R4DataScience/1305224

## Project Architecture & Tools
Unlike a simple notebook-based analysis, this project follows a Modular Software Engineering approach:

- Database: PostgreSQL

- Orchestration: Python scripts for automated data ingestion and summary table generation.

- Analytics: SQL, Pandas, NumPy

- Visualization: Seaborn, Matplotlib, Jupyter Notebook

- Statistical Analysis: Chi-Square Test for Independence, Correlation Matrix Analysis

<pre>
CHURN_ANALYSIS/
├── data/                       # (Gitignored)
├── logs/                       # (Gitignored) Execution logs
├── notebooks/                  # Exploratory Data Analysis & Prototyping
│   ├── 01_eda.ipynb
│   ├── 02_customer_churn_analysis.ipynb
├── src/                        # Modular Python source code
│   ├── __init__.py
│   ├── database/               # Database connection logic
│   │   ├── __init__.py
│   │   └── postgres_session.py
│   ├── ingestion/              # Data loading scripts
│   │   ├── __init__.py
│   │   └── ingestion_to_db.py
│   ├── processing/             # Feature engineering & transformation
│   │   ├── __init__.py
│   │   └── get_summary_table.py
│   └── utils/                  # Reusable helper scripts
│       ├── __init__.py
│       ├── logger.py
│       └── exception.py
├── tests/                      # Unit tests
├── .env                        # (Gitignored) DB Credentials & Secrets
├── .gitignore                  # Prevents junk files from being uploaded
├── README.md                   # Project documentation
├── requirements.txt            # Project dependencies
└── main.py                     # Entry point to run the entire pipeline
</pre>

## How to Run
1. Clone the repo: `git clone https://github.com/abhishektarun09/Bank-Customer-Churn-and-Retention-Analysis.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables in `.env`.
4. Run ingestion and data cleaning through ETL `python main.py`
5. Explore results in `notebooks/02_customer_churn_analysis.ipynb`.


## Contact
- **Author:** Abhishek Tarun 
- **Email:** [abhishek.tarun09@gmail.com](mailto:abhishek.tarun09@gmail.com)