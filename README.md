# Bank Customer Churn and Retention Analysis

### Optimizing Customer Lifetime Value in Nigerian Retail Banking

This project analyzes churn patterns within a major Nigerian financial institution to identify behavioral, demographic, and product-level drivers of attrition. By leveraging SQL, modular Python code and statistical modeling, the goal is to provide actionable insights for relationship managers and product teams to increase customer "stickiness."

## Business Problem
The bank is facing an increasing churn rate. To protect the bottom line, this analysis seeks to answer:

- Behavioral Drivers: Which specific actions (or lack thereof) precede a customer closing their account?

- Digital Adoption: Does the usage of mobile apps and digital banking reduce churn?

- FX Loyalty: Are customers holding domiciliary (USD/GBP/EUR) accounts more loyal and profitable than Nigerian Naira-only customers?

## Key Insights
- Risk Profile: "Medium risk" customers are the most volatile, accounting for 51.7% of the total churned population.
- There is a massive disparity in churn based on product ownership. Customers with Credit Cards have a churn rate of only 0.04%, while those without them churn at 53.93%. Promoting credit card adoption is the strongest driver of retention found in the data.
- Activity vs. Tenure: Tenure (years) has almost no correlation with active usage. Old accounts are not necessarily "safe" accounts.
- The Digital Paradox: The data suggests that digital adoption is NOT currently reducing churn.
- Users who utilize all 3 digital channels (Mobile App, Internet Banking, and USSD) actually represent the highest volume of churned customers (over 94,000 users).
- Foreign currency (FX) customers are significantly more profitable but much less loyal than Naira (NGN) customers.
- USD customers maintain an average balance 19x higher than NGN customers.
- Churn Rates: GBP (74.4%), USD (71.1%), and EUR (68.0%) all have significantly higher churn rates than NGN (53.6%).
- Statistical Significance: A Chi-square test (p < 0.01) confirmed that currency type is a major factor in churn. FX customers churn roughly 20 percentage points more than local currency customers.

| Customer Segment | Churn Risk | Strategy |
| :--- | :--- | :--- |
| **FX / Domiciliary** | 🔴 Very High | High-value retention; these are profitable but highly "leakable." |
| **Naira (NGN) Only** | 🟡 Moderate | Focus on cross-selling to increase friction. |
| **Digital-Heavy Users** | 🟠 High | Introduce "human" touchpoints or loyalty rewards. |
| **No Credit Card** | ⚫ Extremely High | **Primary Goal:** Convert these to Credit Card holders to "lock in" loyalty. |

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