# CodeAlpha Task 3 - Data Visualization

## Project Overview

This project visualizes book data collected from Books to Scrape. It uses Python to create charts and a dashboard that help communicate patterns in book prices and ratings.

## Dataset

The dataset contains 1,000 books with the following columns:

- **Title:** Book title
- **Price:** Book price in pounds (£)
- **Rating:** Book rating from 1 to 5 stars
- **Availability:** Book availability status

## Tools and Libraries

- Python 3.13
- Pandas
- Matplotlib

## Visualizations

The project creates the following visualizations:

1. **Rating Distribution:** Compares the number of books in each rating category.
2. **Price Distribution:** Shows how book prices are distributed across price ranges.
3. **Price vs Rating:** Explores the relationship between book prices and ratings.
4. **Books Dashboard:** Combines the three charts with key dataset metrics in one figure.

## Key Metrics

The dashboard reports:

- Total number of books
- Average book price
- Average book rating

Additional statistics, including minimum and maximum prices, average price by rating, and the price-rating correlation, are printed when the script runs.

## Project Structure

```text
CodeAlpha_Task3/
├── books.csv
├── visualization.py
├── rating_distribution.png
├── price_distribution.png
├── price_vs_rating.png
├── books_dashboard.png
└── README.md
```

## How to Run

Install the required libraries:

```bash
py -3.13 -m pip install pandas matplotlib
```

Run the visualization script:

```bash
py -3.13 visualization.py
```

The script displays the charts and saves the generated PNG files in the project folder.

## Data Source

[Books to Scrape](https://books.toscrape.com/)

## Internship

CodeAlpha Data Analytics Internship — Task 3: Data Visualization.
