# Sales Forecasting & Business Insights

## 📊 Project Overview

This project is a Python-based **Sales Forecasting and Business Insights** application.

It reads sales data from a CSV file, analyzes sales performance, generates business insights, and uses **Linear Regression** to forecast future monthly sales.

The project also creates visual charts for:

* Monthly Sales
* Sales by Product
* Sales by Region
* Actual Sales vs Forecast Sales

---

## 🚀 Features

### 1. CSV Data Loading

The program reads sales data from a CSV file.

### 2. Business Summary

The program calculates:

* Total Sales
* Total Units Sold
* Average Price

### 3. Product Analysis

It calculates total sales for each product and identifies the product with the highest sales.

### 4. Region Analysis

It calculates total sales for each region and identifies the region with the highest sales.

### 5. Monthly Sales Analysis

Sales are grouped by month to understand sales performance over time.

### 6. Sales Forecasting

The project uses **Linear Regression** from Scikit-learn to forecast sales for future months.

### 7. Business Insights

The program identifies:

* Highest Sales Month
* Best Product
* Best Region
* Overall Sales Trend

### 8. Data Visualization

Matplotlib is used to generate four charts:

1. Monthly Sales
2. Sales by Product
3. Sales by Region
4. Actual Sales vs Forecast Sales

---

## 📁 Project Structure

```text
Sales-Forecasting/
│
├── sales_forecasting.py
├── sample_sales.csv
└── README.md
```

---

## 📄 CSV File Format

The CSV file should contain the following columns:

```text
product,quantity_sold,price,date,region
```

### Example

```csv
product,quantity_sold,price,date,region
Laptop,10,50000,2025-01-10,North
Phone,20,20000,2025-01-15,South
Tablet,15,30000,2025-02-05,East
Laptop,12,50000,2025-02-12,West
Phone,25,20000,2025-03-08,North
```

### Column Description

| Column          | Description          |
| --------------- | -------------------- |
| `product`       | Name of the product  |
| `quantity_sold` | Number of units sold |
| `price`         | Price per unit       |
| `date`          | Date of the sale     |
| `region`        | Sales region         |

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data processing and analysis
* **NumPy** – Numerical calculations
* **Matplotlib** – Data visualization
* **Scikit-learn** – Linear Regression forecasting

---

## 📦 Installation

Make sure Python is installed on your computer.

Install the required libraries using:

```bash
pip install pandas numpy matplotlib scikit-learn
```

---

## ▶️ How to Run

### Step 1: Open the project folder

Make sure your Python file and CSV file are in the same folder.

Example:

```text
Newfolder/
├── sales_forecasting.py
├── sample_sales.csv
└── README.md
```

### Step 2: Open the terminal

Navigate to the project folder:

```bash
cd C:\Users\anoop\OneDrive\Desktop\Newfolder
```

### Step 3: Run the Python program

```bash
python sales_forecasting.py
```

### Step 4: Enter the CSV filename

When the program asks:

```text
Enter CSV file name (example: sales_data.csv):
```

enter:

```text
sample_sales.csv
```

### Step 5: Enter the forecast period

For example:

```text
Enter number of future months to forecast: 3
```

The program will then display the analysis and generate the charts.

---

## 📈 Forecasting Method

The project uses **Linear Regression**.

The monthly sales data is converted into sequential month numbers:

```text
Month 1
Month 2
Month 3
Month 4
...
```

The model learns the relationship between the month number and sales:

```text
Sales = Linear Regression(Month)
```

The trained model is then used to estimate sales for future months.

Negative forecast values are prevented using:

```python
np.maximum(forecast, 0)
```

---

## 📊 Output

The program displays a business summary similar to:

```text
--- BUSINESS SUMMARY ---
Total Sales  : 2500000.00
Total Units  : 450
Average Price: 27500.00
```

It also displays:

```text
--- BUSINESS INSIGHTS ---
Highest Sales Month: 2025-06
Best Product       : Laptop
Best Region        : North
Sales Trend        : Increasing
```

The forecast is displayed as:

```text
--- SALES FORECAST ---
     month  forecast_sales
0  2025-07       425000.00
1  2025-08       438000.00
2  2025-09       451000.00
```

---

## 📉 Charts Generated

### Monthly Sales

Shows how sales change from month to month.

### Sales by Product

Compares total sales between different products.

### Sales by Region

Compares sales performance across different regions.

### Actual vs Forecast Sales

Shows historical sales together with predicted future sales.

---

## ⚠️ Common Error

### `File not found`

If you see:

```text
File not found. Please check the CSV file name.
```

make sure `sample_sales.csv` is located in the same folder from which the program is being executed.

For example:

```text
C:\Users\anoop\OneDrive\Desktop\Newfolder\
```

should contain:

```text
sample_sales.csv
```

You can check the files in PowerShell using:

```powershell
dir
```

---

## 🔮 Future Improvements

Possible improvements include:

* Add interactive dashboards
* Add yearly sales analysis
* Add profit and revenue calculations
* Add product-level forecasting
* Add region-level forecasting
* Compare multiple forecasting algorithms
* Add forecast accuracy metrics
* Export analysis results to Excel
* Add a graphical user interface
* Automatically detect the CSV file
* Add more advanced forecasting models such as ARIMA or Random Forest

---

## 🎯 Learning Objectives

This project demonstrates practical use of:

* Data loading
* Data cleaning
* Data transformation
* GroupBy analysis
* Business analytics
* Data visualization
* Machine learning
* Linear Regression
* Sales forecasting
* Business insight generation

---

## 👨‍💻 Project

**Project Name:** Sales Forecasting & Business Insights

**Language:** Python

**Type:** Data Analysis & Machine Learning Project

**Input:** CSV Sales Data

**Output:** Business Insights, Forecasts, and Visualizations
