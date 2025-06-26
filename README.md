# Regulatory Reporting Tool


# Overview
This project simulates regulatory reporting workflows for OTC derivatives. It transforms raw OTC trade data (e.g., interest rate swaps) into structured XML and JSON reports using real-world standards like ISDA taxonomy and UPI.


# Project Goals
- Ingest and transform raw trade data.
- Enrich with regulatory classification using ISDA taxonomy.
- Generate compliant XML/JSON output for regulatory reporting.
- Simulate the entire trade-to-report pipeline.


# Prerequisites
- Python 3.9+
- pip (Python package installer)


# To install, clone or download the repository: reg_reporting_tool

git clone https://github.com/ericwang-finmktdatalab/reg_reporting_tool.git
cd reg_reporting_tool


# Folder Structure
reg_reporting_tool/
├── config/                     # Configuration files (e.g., mappings)
│   └── mapping_rules.yaml
├── data/
│   ├── raw/                    # Sample input trades
│   │   └── sample_trades.csv
│   └── reference/             # Reference ISDA taxonomies and UPI
│       └── product_reference.csv
│       └── ISDA-Taxonomy_EQ-CR-FX-IR_v2.0__3-_September_2019-FINAL.xls
│       └── UPI-Product-Definitions-RATES.xlsx
├── output/                    # Generated reports
│   ├── ir_report.json
│   └── ir_report.xml
├── src/                       # Source code modules
│   ├── loader.py
│   ├── reporter.py
│   ├── transformer.py
│   └── utils.py
└── run_pipeline.py            # Main script to execute transformation


# How to Use - Step-by-step Example
1) Prepare your raw trades in data/raw/sample_trades.csv
2) Configure field mappings in config/mapping_rules.yaml
3) Set reference enrichment mappings in data/reference/product_reference.csv
4) Run the transformation pipeline: python run_pipeline.py


# Sample Input Format

CSV (data/raw/sample_trades.csv)
TradeID,TradeDate,Counterparty,AssetClass,BaseProduct,SubProduct,TransactionType,Notional,Currency,Maturity,Action
T001,2025-06-01,Bank A,Interest Rate,IR Swap,Fixed Float,OIS,1000000,USD,2027-06-01,New

CSV (data/reference/product_reference.csv)
asset_class,base_product,sub_product,transaction_type,isda_taxonomy,dsb_product_name,upi
Interest Rate,IR Swap,Fixed Float,OIS,IR:Swap:FixedFloat:OIS,Rates.Swap.Fixed_Float_OIS,QZWT24156782


# Sample Output Format
JSON (output/ir_report.json)
[
    {
        "trade_id":"T001",
        "trade_date":"2025-06-01",
        "counterparty":"Bank A",
        "asset_class":"Interest Rate",
        "base_product":"IR Swap",
        "sub_product":"Fixed Float",
        "transaction_type":"OIS",
        "notional_amount":1000000,
        "notional_currency":"USD",
        "maturity_date":"2027-06-01",
        "action_type":"New",
        "isda_taxonomy":"IR:Swap:FixedFloat:OIS",
        "dsb_product_name":"Rates.Swap.Fixed_Float_OIS",
        "upi":"QZWT24156782"
    },
...

XML (output/ir_report.xml)
<trades>
	<trade>
		<trade_id>T001</trade_id>
		<trade_date>2025-06-01</trade_date>
		<counterparty>Bank A</counterparty>
		<asset_class>Interest Rate</asset_class>
		<base_product>IR Swap</base_product>
		<sub_product>Fixed Float</sub_product>
		<transaction_type>OIS</transaction_type>
		<notional_amount>1000000</notional_amount>
		<notional_currency>USD</notional_currency>
		<maturity_date>2027-06-01</maturity_date>
		<action_type>New</action_type>
		<isda_taxonomy>IR:Swap:FixedFloat:OIS</isda_taxonomy>
		<dsb_product_name>Rates.Swap.Fixed_Float_OIS</dsb_product_name>
		<upi>QZWT24156782</upi>
	</trade>
...


# Contributions
This is a simulated project for educational purposes. Contributions or suggestions are welcomed for improving realism or adding new jurisdiction templates (e.g. CFTC, EMIR, ASIC, MAS)


# License
This project is for educational and non-commercial use only.
