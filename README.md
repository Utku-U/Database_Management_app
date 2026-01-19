# Database_Management_app

In this project, a web application has been developed using Python and Streamlit for a simulation database named 'Product_Stock_Management'.

The goal of this application is to enable the processing of all data in the database through a simple interface, without requiring any SQL knowledge.


# Product Stock Management System

A Streamlit-based web application for managing product inventory, categories, suppliers, and stock levels using a MySQL database.

## Features

- **Product Management**: Create, read, update, and delete products.
- **Category Management**: Manage product categories.
- **Supplier Management**: Keep track of suppliers.
- **Inventory Management**: Track stock levels across different warehouses.

## Setup

1.  **Clone the repository** (or download the files).
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure the database**:
    -   Ensure you have MySQL installed and running.
    -   Create a database named `product_stock_management`.
    -   Import your schema (tables: `Categories`, `Product`, `Supplier`, `Inventory`) if not already present.
    -   Create a `.env` file in the root directory with your database credentials (see `.env.example` or below):

    ```env
    DB_HOST=localhost
    DB_USER=root
    DB_PASSWORD=your_password
    DB_NAME=product_stock_management
    ```

## Usage

Run the application using Streamlit:

```bash
streamlit run Product_Stock_Management_MySQL.py
```
