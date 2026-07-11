# Expense-Tracker
# Personal Finance & Expense Tracker

A lightweight Python application designed to help users record, categorize, and analyze their daily expenses against a set budget limit. The application provides instant visual feedback through `matplotlib` charts to help users understand their spending habits at a glance.

## 🚀 Features

- **Full Expense Management:** Easily Add, Edit, and Delete expense entries via an interactive command-line interface.
- **Predefined Categorization:** Tracks spending across 6 core categories: *Food, Entertainment, Travelling, Subscription, Maintenance, and Investment*.
- **Data Persistence:** Automatically compiles and saves your layout into a structured CSV file (`expense_tracker.csv`) using `pandas`.
- **Budget Threshold Tracking:** Visualizes total spending directly against a maximum budget threshold ($50,000) to flag overspending.
- **Dual-Chart Visualization:** Generates side-by-side data visualizations:
  - A **Pie Chart** breaking down percentage expenditure per category.
  - A **Bar Chart** comparing total historical spending side-by-side with the set budget ceiling.
