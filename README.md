# Data Quality Audit - Sample Superstore

## About the Project

This project was completed as part of a Data Analytics Internship task.

The main purpose of this project is to check the quality of the Sample Superstore dataset and find common data problems using Python and Pandas.

## Objective

The objective of this project is to:

- Find missing values
- Find duplicate records
- Check incorrect or unusual values
- Check date consistency
- Check numeric ranges
- Check fact and dimension table relationships
- Create an issue log
- Prepare a cleaned sample dataset

## Dataset

The dataset used for this project is the Sample Superstore dataset.

The Excel workbook contains the following tables:

- Sales_Facts
- Product_Dimension
- Coustomer_Dimension
- Location_Dimension
- Date_Dimension

## Tools Used

- Python
- Pandas
- Excel
- Jupyter Notebook / Python environment

## Data Quality Checks

The following checks were performed:

1. Missing values
2. Duplicate rows
3. Duplicate Row IDs
4. Ship Date and Order Date consistency
5. Quantity validation
6. Discount validation
7. Sales value validation
8. Duplicate Product IDs
9. Customer ID matching
10. Product ID matching
11. Location matching
12. Date Dimension matching

## Main Results

The audit produced the following results:

| Check | Result |
|---|---:|
| Sales records | 10,194 |
| Missing cells | 0 |
| Exact duplicate rows | 0 |
| Duplicate Row IDs | 0 |
| Ship Date before Order Date | 2,185 |
| Invalid Quantity | 0 |
| Invalid Discount | 0 |
| Negative Sales | 0 |
| Duplicate Product IDs | 32 |
| Missing Customer IDs | 0 |
| Missing Product IDs | 0 |
| Missing Location keys | 0 |
| Missing Date Dimension dates | 0 |

## Issues Found

### 1. Ship Date Issue

There are 2,185 records where the Ship Date is earlier than the Order Date.

This is a date consistency problem because a shipment should normally not occur before the order.

For the cleaned file, I did not guess replacement dates. The invalid Ship Date values were left blank and a `Quality_Flag` column was added so that these records can be reviewed later.

### 2. Duplicate Product IDs

There are 32 duplicate Product IDs in the Product Dimension.

This can create problems when Product ID is used as a unique key.

The records were not deleted randomly. They should be checked against the original product master before making a final correction.

## Cleaning Approach

The cleaning process was kept simple and traceable.

- Valid data was not changed.
- Invalid Ship Dates were marked for review.
- A `Quality_Flag` column was added.
- Duplicate Product IDs were recorded in the issue log.
- No values were guessed or artificially created.

## Project Files

- `samplesuperstore.xlsx` - Original dataset
- `Data_Quality_Audit_Report.pdf` - Project report
- `data_quality_audit.py` - Python/Pandas audit script
- `audit_summary.csv` - Audit results
- `issue_log.csv` - Important data quality issues
- `cleaned_sales_facts.csv` - Cleaned fact table
- `cleaned_sales_sample_100_rows.csv` - Sample cleaned data
- `requirements.txt` - Required Python packages

## How to Run the Python Script

Install the required packages:

```bash
pip install pandas openpyxl
