# Exploratory Data Analysis - Customer Loans in Finance

Exploratory data analysis of a financial institution's loan portfolio to uncover patterns, relationships, and anomalies in lending data. This analysis aims to enhance decision-making for loan approvals, improve risk management strategies, and optimize portfolio profitability through statistical analysis and data visualisation techniques.

## Setup and Installation

1. Clone this repository.
2. Install the required dependencies:

```bash
pip install pandas sqlalchemy psycopg2-binary pyyaml
```

## Database Connection

The project includes an 'RDSDatabaseConnector'

### Credentials Setup

Create a 'credentials.yaml' file in the project root with the following structure:

```yaml
HOST: your_host_address
USER: your_username
PASSWORD: your_password
DATABASE: your_database_name
PORT: your_port_number
```
