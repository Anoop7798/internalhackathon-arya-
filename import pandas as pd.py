import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print("=" * 50)
print(" SALES FORECASTING & BUSINESS INSIGHTS")
print("=" * 50)

# 1. Load and prepare data
df = pd.read_csv("sample_sales.csv")
df["date"] = pd.to_datetime(df["date"])
df["sales"] = df["quantity_sold"] * df["price"]
df["month"] = df["date"].dt.to_period("M").astype(str)

print("\nData loaded successfully!")

# 2. Business Summary
total_sales = df["sales"].sum()
total_units = df["quantity_sold"].sum()
avg_price = df["price"].mean()

print("\n--- BUSINESS SUMMARY ---")
print("Total Sales  :", round(total_sales, 2))
print("Total Units  :", total_units)
print("Average Price:", round(avg_price, 2))

# 3. Product and Region Analysis
product_sales = df.groupby("product")["sales"].sum()
region_sales = df.groupby("region")["sales"].sum()

best_product = product_sales.idxmax()
best_region = region_sales.idxmax()

print("\n--- SALES BY PRODUCT ---")
print(product_sales)

print("\n--- SALES BY REGION ---")
print(region_sales)

print("\nBest Product:", best_product)
print("Best Region :", best_region)

# 4. Monthly Sales
monthly = (
    df.groupby("month", as_index=False)["sales"]
      .sum()
)

monthly["month_no"] = np.arange(1, len(monthly) + 1)

print("\n--- MONTHLY SALES ---")
print(monthly[["month", "sales"]])

# 5. Sales Forecasting
model = LinearRegression()
model.fit(monthly[["month_no"]], monthly["sales"])

months = int(input("\nEnter number of future months to forecast: "))

future_no = np.arange(
    len(monthly) + 1,
    len(monthly) + months + 1
)

forecast = np.maximum(
    model.predict(future_no.reshape(-1, 1)),
    0
)

future_dates = pd.date_range(
    start=pd.to_datetime(monthly["month"].iloc[-1]) + pd.DateOffset(months=1),
    periods=months,
    freq="MS"
)

forecast_df = pd.DataFrame({
    "month": future_dates.strftime("%Y-%m"),
    "forecast_sales": forecast
})

print("\n--- SALES FORECAST ---")
print(forecast_df)

# 6. Business Insights
best_month = monthly.loc[monthly["sales"].idxmax(), "month"]

first_sales = monthly["sales"].iloc[0]
last_sales = monthly["sales"].iloc[-1]

if last_sales > first_sales:
    trend = "Increasing"
elif last_sales < first_sales:
    trend = "Decreasing"
else:
    trend = "Stable"

print("\n--- BUSINESS INSIGHTS ---")
print("Highest Sales Month:", best_month)
print("Best Product       :", best_product)
print("Best Region        :", best_region)
print("Sales Trend        :", trend)

# 7. Monthly Sales Chart
plt.figure(figsize=(10, 5))
plt.plot(
    monthly["month"],
    monthly["sales"],
    marker="o"
)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()

# 8. Product Sales Chart
plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 9. Region Sales Chart
plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 10. Actual vs Forecast Sales
plt.figure(figsize=(12, 6))

plt.plot(
    monthly["month"],
    monthly["sales"],
    marker="o",
    label="Actual Sales"
)

plt.plot(
    forecast_df["month"],
    forecast_df["forecast_sales"],
    marker="o",
    linestyle="--",
    label="Forecast Sales"
)

# Connect last actual value to first forecast value
plt.plot(
    [monthly["month"].iloc[-1], forecast_df["month"].iloc[0]],
    [monthly["sales"].iloc[-1], forecast_df["forecast_sales"].iloc[0]],
    linestyle="--"
)

plt.title("Actual Sales vs Forecast Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

print("\n" + "=" * 50)
print(" PROJECT COMPLETED")
print("=" * 50)