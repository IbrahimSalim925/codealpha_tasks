# CodeAlpha Task 2 - Exploratory Data Analysis (EDA)

## 1. Project Overview

This project performs Exploratory Data Analysis (EDA) on a dataset containing 1,000 books collected from the Books to Scrape website.

The goal is to understand the dataset, summarize book prices and ratings, identify patterns, examine relationships between variables, and visualize the results using Python.

## 2. Dataset Description

The dataset contains 1,000 books and the following columns:

- **Title:** The title of the book.
- **Price:** The price of the book in pounds sterling (£).
- **Rating:** The book rating from 1 to 5.
- **Availability:** The availability status recorded during data collection.

Dataset file: `books.csv`

## 3. Tools and Libraries

The project uses the following tools and libraries:

- **Python 3.13:** Programming language used for the analysis.
- **Pandas:** Used to load, inspect, analyze, and summarize the dataset.
- **Matplotlib:** Used to create and save data visualizations.

## 4. Data Inspection and Quality Checks

The dataset was inspected to understand its structure, number of rows and columns, data types, and overall quality.

The following checks were performed:

- Inspected the dataset structure and column data types.
- Checked for missing values.
- Checked for duplicate rows.
- Reviewed descriptive statistics.
- Examined the distribution of book ratings and prices.

The checks found no missing values or duplicate rows in the dataset.

The dataset contains 1,000 rows and 4 columns.

## 5. Statistical Analysis

The analysis produced the following results:

- **Total number of books:** 1,000
- **Average book price:** £35.07
- **Minimum book price:** £10.00
- **Maximum book price:** £59.99
- **Average book rating:** 2.92 out of 5
- **Most common rating:** 1 star, appearing for 226 books

### Average Price by Rating

The average prices for books with each rating were:

| Rating | Average Price |
|---|---:|
| 1 star | £34.56 |
| 2 stars | £34.81 |
| 3 stars | £34.69 |
| 4 stars | £36.09 |
| 5 stars | £35.37 |

### Cheapest and Most Expensive Books

- **Cheapest book:** An Abundance of Katherines — £10.00
- **Most expensive book:** The Perfect Play (Play by Play #1) — £59.99

### Price and Rating Correlation

The correlation coefficient between book price and rating was approximately **0.028**.

This value indicates almost no linear relationship between price and rating in this dataset.

Correlation does not imply causation, and this result applies only to the collected dataset.

## 6. Visualizations

The project generates the following charts using Matplotlib:

1. `rating_distribution.png` — Shows the distribution of book ratings.
2. `price_distribution.png` — Shows the distribution of book prices.
3. `price_vs_rating.png` — Shows the relationship between book prices and ratings using a scatter plot.

These visualizations help summarize the data and explore patterns in book prices and ratings.

## 7. Key Insights

The analysis revealed the following insights:

- The dataset contains 1,000 books.
- Book prices range from £10.00 to £59.99.
- The average book price is approximately £35.07.
- The average book rating is 2.92 out of 5.
- One-star ratings are the most frequent, with 226 books.
- The cheapest book is An Abundance of Katherines, priced at £10.00.
- The most expensive book is The Perfect Play (Play by Play #1), priced at £59.99.
- Average book prices vary across rating groups, ranging from £34.56 for one-star books to £36.09 for four-star books.
- The correlation coefficient of 0.028 indicates almost no linear relationship between price and rating in this dataset.
- All 1,000 books were recorded as "In stock" during data collection. This describes the collected data and does not guarantee their current availability.

## 8. Project Structure

```text
CodeAlpha_Task2/
├── EDA.py
├── books.csv
├── rating_distribution.png
├── price_distribution.png
├── price_vs_rating.png
└── README.md
```

## 9. How to Run the Project

### Prerequisites

- Python 3.13
- Pandas
- Matplotlib

### Step 1: Install the Required Libraries

Run the following command in the terminal:

```powershell
py -3.13 -m pip install pandas matplotlib
```

### Step 2: Check the Project Files

Make sure `books.csv` is in the same folder as `EDA.py`.

### Step 3: Run the Analysis

Run the following command:

```powershell
py -3.13 EDA.py
```

The script prints statistical summaries and key insights in the terminal and generates the visualization files in the project folder.

## 10. Data Source

The dataset was collected from:

https://books.toscrape.com/

## 11. Internship

**Program:** CodeAlpha Internship - Data Analytics

**Task:** Task 2 - Exploratory Data Analysis (EDA)
