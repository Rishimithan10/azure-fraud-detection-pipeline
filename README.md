# Credit Card Fraud Detection on Azure

An end-to-end fraud detection data engineering project built on Azure using a Medallion (Bronze → Silver → Gold) Lakehouse architecture. The solution ingests raw transaction data into Azure Data Lake Storage Gen2, transforms it using Azure Databricks and PySpark, orchestrates workflows through Azure Data Factory, and exposes curated analytics through Azure Synapse Analytics.

---

## Project Overview

Financial institutions process millions of transactions daily, making fraud detection a critical business requirement. This project demonstrates how to build a scalable cloud-native data platform that processes credit card transaction data and generates fraud-related insights for reporting and analytics.

### Business Objectives

* Centralize transaction data in a governed data lake
* Automate ingestion and transformation pipelines
* Build a Medallion Architecture for data quality and governance
* Generate fraud detection KPIs and business metrics
* Enable analytical querying through Azure Synapse Analytics
* Demonstrate enterprise-grade Azure Data Engineering practices

---

## Architecture

```text
Raw Data (CSV / Parquet)
        │
        ▼
Azure Data Lake Storage Gen2
        │
        ▼
Bronze Layer
        │
        ├── Raw transaction data
        ├── Raw identity data
        └── Immutable storage
        │
        ▼
Azure Databricks (PySpark)
        │
        ▼
Silver Layer
        │
        ├── Null handling
        ├── Deduplication
        ├── Data validation
        ├── Type casting
        └── Feature engineering
        │
        ▼
Azure Databricks (PySpark)
        │
        ▼
Gold Layer
        │
        ├── Fraud KPIs
        ├── Transaction trends
        ├── Risk metrics
        └── Business aggregations
        │
        ▼
Azure Synapse Analytics
        │
        ▼
Reporting & Analytics
```

---

## Azure Services Used

| Service                      | Purpose                           |
| ---------------------------- | --------------------------------- |
| Azure Data Lake Storage Gen2 | Data Lake Storage                 |
| Azure Data Factory           | Pipeline Orchestration            |
| Azure Databricks             | Data Processing & Transformations |
| Delta Lake                   | ACID Storage Layer                |
| Azure Synapse Analytics      | SQL Analytics & Reporting         |

---

## Data Pipeline Flow

### Bronze Layer

Purpose:

* Store raw source data without modifications
* Preserve historical data
* Enable replayability

Data Sources:

* Transaction Dataset
* Identity Dataset

Processing:

* Read Parquet files from ADLS Gen2
* Perform schema validation
* Register datasets for downstream processing

---

### Silver Layer

Purpose:

* Improve data quality
* Standardize schema
* Prepare analytical datasets

Transformations:

* Remove duplicate records
* Handle missing values
* Validate transaction amounts
* Standardize data types
* Join transaction and identity datasets
* Create derived fraud features

Example Features:

* Transaction Hour
* High Value Transaction Flag
* Device Risk Indicators
* Email Domain Features
* Transaction Velocity Metrics

---

### Gold Layer

Purpose:

* Generate business-ready analytical datasets

Aggregations:

#### Fraud Rate by Merchant Category

```sql
SELECT
    ProductCD,
    COUNT(*) AS total_transactions,
    SUM(isFraud) AS fraud_transactions,
    ROUND(SUM(isFraud) * 100.0 / COUNT(*),2) AS fraud_rate
FROM fraud_gold
GROUP BY ProductCD;
```

#### Transaction Volume Trends

```sql
SELECT
    transaction_date,
    COUNT(*) AS transaction_count,
    SUM(TransactionAmt) AS total_amount
FROM fraud_gold
GROUP BY transaction_date;
```

#### Risk Scoring Metrics

* Fraud Frequency
* Average Fraud Amount
* High-Risk Categories
* Suspicious Transaction Volume

---

## Databricks Workflow

The project uses a multi-stage Databricks Job.

```text
01_bronze_reader
        │
        ▼
02_silver_transform
        │
        ▼
03_gold_aggregation
```

Features:

* Task dependencies
* Automated retries
* Scheduling support
* Execution monitoring
* Failure handling

---

## Data Quality Checks

Implemented validations include:

* Null value detection
* Empty dataset validation
* Duplicate record checks
* Transaction amount validation
* Schema consistency verification

Example:

```python
assert transactions_df.count() > 0
assert identity_df.count() > 0
```

---

## Synapse Analytics

The Gold layer is exposed through Azure Synapse Analytics for SQL-based querying and reporting.

Example business questions:

* Which merchant categories experience the highest fraud rates?
* What transaction patterns indicate suspicious behavior?
* How does fraud volume trend over time?
* Which transaction segments contribute most to fraud losses?

---

## KPIs Generated

* Fraud Rate by Merchant Category
* Fraud Transaction Count
* Total Transaction Volume
* Average Fraud Amount
* Fraud Trend Analysis
* High-Risk Product Categories
* Fraud Distribution by Device Type
* Fraud Distribution by Email Domain

---

## Future Enhancements

* Real-Time Streaming using Event Hub
* Machine Learning Fraud Prediction Models
* Delta Live Tables
* Change Data Capture (CDC)
* Data Quality Monitoring Framework
* Power BI Dashboard Integration
* Azure Key Vault Integration
* CI/CD using Azure DevOps

---

## Skills Demonstrated

* Azure Data Engineering
* Azure Data Lake Storage Gen2
* Azure Databricks
* PySpark
* Delta Lake
* Azure Data Factory
* Azure Synapse Analytics
* Medallion Architecture
* ETL Pipeline Development
* Data Quality Engineering
* Fraud Analytics
* Cloud Data Platforms

---

## Author

**Rishimithan Kannan**

Azure Data Engineering Project – Credit Card Fraud Detection Platform
