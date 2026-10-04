# Week 9 — Sales Data: Model, Queries and Cleaning

## Project overview
This project analyzes a small e-commerce sales dataset using Python and pandas. It includes an Entity-Relationship Diagram (ERD), data cleaning, two analytical questions, and documented findings.

## Dataset
The original dataset is `data/sales_dirty.csv`. It intentionally contains common data-quality problems: missing values, an exact duplicate, inconsistent date formats, inconsistent capitalization/spacing, and numeric values stored as text.

## ERD
The model contains four entities:
- **Customer** — customer information.
- **Order** — purchase transaction.
- **OrderDetail** — products and quantities belonging to an order.
- **Product** — product information and category.

Relationships:
- Customer **1:N** Order
- Order **1:N** OrderDetail
- Product **1:N** OrderDetail

See `erd/modelo_erd.png`.

## Data & Cleaning
The dataset contains e-commerce sales records with customers, orders, products, categories, quantities, prices, cities, and payment statuses. Before cleaning, the data included missing values, an exact duplicate row, inconsistent date formats, inconsistent text capitalization, and numeric values stored as strings. I converted the order dates to a consistent datetime format and standardized text fields by trimming spaces and applying consistent capitalization. I converted quantity and unit price into numeric data types so they could be used safely in calculations. I removed the duplicated row and filled missing values using documented rules, including medians for numeric fields and explicit labels for missing text. After cleaning, I created a `total_sales` column by multiplying quantity by unit price. Finally, I used pandas aggregations to answer two business questions about sales by category and average order value by city.

## Cleaning summary

| Metric | Before | After |
|---|---:|---:|
| Rows | 36 | 35 |
| Columns | 11 | 12 |
| Null cells | 4 | 0 |
| Duplicate rows | 1 | 0 |

## Questions and findings

### 1. Which product categories generate the most sales?
The notebook groups the cleaned data by `category` and sums `total_sales`. The top category and its total are printed automatically.

### 2. Which city has the highest average order value?
The notebook groups the cleaned data by `city` and calculates the mean of `total_sales`. The top city and its average are printed automatically.

## How to run
```bash
pip install -r requirements.txt
jupyter notebook notebooks/analisis_limpieza.ipynb
```

## Project structure
```text
semana-9-sales-data-project/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── sales_dirty.csv
│   └── DATA_DICTIONARY.md
├── erd/
│   └── modelo_erd.png
└── notebooks/
    └── analisis_limpieza.ipynb
```

## GitHub delivery
From the project folder:
```bash
git add .
git commit -m "Add week 9 sales data project"
git push
```

**Important:** replace/add the course-required `CONFIG` block with your own full name and GitHub username before submitting.
