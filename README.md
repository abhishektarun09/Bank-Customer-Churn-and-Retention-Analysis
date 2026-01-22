# Bank Customer Churn and Retention Analysis

## Business Problem
- Churn rate is X%. Which customer behaviors are driving churn, and which ones protect against it?
- Does digital adoption actually reduce churn, or are we just pushing apps for nothing?
- Can we identify churn before it happens?
- Do loans improve stickiness or increase dissatisfaction and churn?
- Which schemes/products are killing retention?
- Which customers should relationship managers prioritize?
- Are foreign currency customers more loyal and profitable?
- If we improve X, how much churn can we realistically reduce?

Link to dataset : https://drive.google.com/file/d/12riQHlBIUUZ4Y9mKqIoFhJ_QryiyFRCx/view?usp=sharing

CHURN_ANALYSIS/
├── data/                   # (Gitignored) Raw, interim, and processed data
├── dbt_churn_analysis/      # Your dbt models and configurations
├── notebooks/              # All Jupyter notebooks
│   ├── 01_eda.ipynb
│   └── 02_customer_churn_analysis.ipynb
├── src/                    # The "Engine": Modular, reusable code
│   ├── __init__.py
│   ├── database/           # DB connections and sessions
│   │   └── postgres_session.py
│   ├── utils/              # Helper functions
│   │   ├── logger.py
│   │   └── exception.py
│   ├── ingestion/          # Logic for moving data to DB
│   │   └── ingestion_to_db.py
│   └── processing/         # Data cleaning and summary logic
│       └── get_summary_table.py
├── tests/                  # Unit and integration tests
├── .env                    # Secrets (DB credentials)
├── .gitignore              # Ignores venv, __pycache__, data/, .env
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── main.py                 # (Optional) Entry point to run the full pipeline