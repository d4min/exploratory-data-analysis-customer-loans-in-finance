# Exploratory Data Analysis - Customer Loans in Finance

Exploratory data analysis of a financial institution's loan portfolio to uncover patterns, relationships, and anomalies in lending data. This analysis aims to enhance decision-making for loan approvals, improve risk management strategies, and optimize portfolio profitability through statistical analysis and data visualisation techniques.

## Setup and Installation

1. Clone this repository.
2. Install the required dependencies:

### Usage Example:

```bash
pip install pandas sqlalchemy psycopg2-binary pyyaml numpy
```

## Database Connection

The project includes an 'RDSDatabaseConnector'

### Credentials Setup

Create a 'credentials.yaml' file in the project root with the following structure:

```yaml
RDS_HOST: your_host_address
RDS_USER: your_username
RDS_PASSWORD: your_password
RDS_DATABASE: your_database_name
RDS_PORT: your_port_number
```

## Data Transformation

The project includes a 'DataTransform' class that handles data type conversions and cleaning of loan payment data:

- Converts date columns to datetime format
- Converts percentage strings to float values
- Converts currency strings to float values
- Converts appropriate columns to categorical type

### Usage Example:

```python 
from data_transformer import DataTransform

transformer = DataTransform()
transformed_df = transformer.transform_data(df)
```

## Data Analsis

The project includes a 'DataFrameInfo' class that provides comprehensive exploratory data analysis capabilities:

### Key Features:

- Basic DataFrame information (shape, data types)
- Statistical summary of numeric columns
- NULL value analysis
- Unique value counts for categorical columns
- Detailed column-specific summaries
- Correlation matrix generation 

### Usage Example:

```python
from dataframe_info import DataFrameInfo

df_info = DataFrameInfo(df)
print(df_info.get_basic_info())
print(df_info.get_null_info())
```

## Project Structure

```
├── README.md
├── credentials.yaml
├── db_utils.py           # Database connection and data extraction
├── data_transformer.py   # Data type transformation and cleaning
├── dataframe_info.py     # Data analysis utilities
└── loan_data_dict.md     # Data dictionary
```