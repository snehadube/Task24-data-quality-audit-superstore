import pandas as pd
import numpy as np

FILE = "samplesuperstore.xlsx"

sales = pd.read_excel(FILE, sheet_name="Sales_Facts")
products = pd.read_excel(FILE, sheet_name="Product_Dimension")
customers = pd.read_excel(FILE, sheet_name="Coustomer_Dimension")
locations = pd.read_excel(FILE, sheet_name="Location_Dimension")
dates = pd.read_excel(FILE, sheet_name="Date_Dimension")

checks = {
    "missing_cells": int(sales.isna().sum().sum()),
    "exact_duplicate_rows": int(sales.duplicated().sum()),
    "duplicate_row_ids": int(sales["Row ID"].duplicated().sum()),
    "duplicate_product_ids": int(products["Product ID"].duplicated().sum()),
    "invalid_ship_dates": int((sales["Ship Date"] < sales["Order Date"]).sum()),
    "invalid_quantity": int((sales["Quantity"] <= 0).sum()),
    "invalid_discount": int(((sales["Discount"] < 0) | (sales["Discount"] > 1)).sum()),
    "negative_sales": int((sales["Sales"] < 0).sum()),
    "missing_customer_keys": int((~sales["Customer ID"].isin(customers["Customer ID"])).sum()),
    "missing_product_keys": int((~sales["Product ID"].isin(products["Product ID"])).sum()),
}

location_keys = set(zip(
    locations["City"], locations["State/Province"],
    locations["Country/Region"], locations["Region"]
))
fact_location_keys = sales[["City","State/Province","Country/Region","Region"]].apply(tuple, axis=1)
checks["missing_location_keys"] = int((~fact_location_keys.isin(location_keys)).sum())

# Create a cleaned sample without inventing replacement values.
cleaned = sales.copy()
bad_ship = cleaned["Ship Date"] < cleaned["Order Date"]
cleaned["Quality_Flag"] = np.where(
    bad_ship, "REVIEW: Ship Date earlier than Order Date", "OK"
)
cleaned.loc[bad_ship, "Ship Date"] = pd.NaT
cleaned.to_csv("cleaned_sales_facts.csv", index=False)

pd.DataFrame([checks]).to_csv("audit_metrics.csv", index=False)

print("Audit completed.")
for key, value in checks.items():
    print(f"{key}: {value}")
