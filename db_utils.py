import yaml
from sqlalchemy import create_engine
import pandas as pd

class RDSDatabaseConnector:
    """
    Extract data from the RDS Database.
    """

    def __init__(self, credentials_file='credentials.yaml'):
        """
        Initialise the RDSDatabaseConnector with database credentials. 

        Args:
            credentials_file: Path to the YAML credentials file
        """
        credentials = self.load_credentials(credentials_file)
        self.host = credentials['RDS_HOST']
        self.user = credentials['RDS_USER']
        self.password = credentials['RDS_PASSWORD']
        self.database = credentials['RDS_DATABASE']
        self.port = credentials['RDS_PORT']

    def load_credentials(self, file_path='credentials.yaml'):
        """
        Load credentials from a YAML file.

        Args:  
            file_path: Path to the YAML credentials file
        
        Returns:
            dict: Dictionary containing the database credentials
        """
        try:
            with open(file_path, 'r') as file:
                credentials = yaml.safe_load(file)
            return credentials
        except FileNotFoundError:
            raise FileNotFoundError(f"Credentials file not found at {file_path}.")
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error parsing YAML file: {e}")
        
    def init_engine(self):
        """
        Initialise and return a SQLAlchemy engine using the stored credentials. 

        Returns:
            sqlalchemy.engine.Engine: Database engine for executing queries

        Example:
            engine = db_connector.init_engine()
            df = pd.read_sql_query("SELECT * FROM table_name", engine)
        """
        connection_string = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        try:
            engine = create_engine(connection_string)
            return engine
        except Exception as e:
            raise Exception(f"Failed to create database engine: {e}")
        
    def extract_data(self):
        """
        Extract data from the loan_payments table in the RDS database.

        Returns:
            pandas.DataFrame: DataFrame containing the loan payments data

        Raises:
            Exception: If there's an error executing the SQL query
        """
        try:
            engine = self.init_engine()
            query = "SELECT * FROM loan_payments"
            df = pd.read_sql_query(query, engine)
            engine.dispose() # close the connection
            return df
        except Exception as e:
            raise Exception(f"Failed to extract data from database: {e}")
        
    def save_to_csv(self, df, file_path='loan_payments.csv'):
        """
        Save the DataFrame to a CSV file.

        Args:
            df: DataFrame to save
            file_path: Path where the CSV file will be saved (Defaults to 'loan_payments.csv')
        
        Raises:
            Exception: If there's an error saving the file
        """
        try:
            df.to_csv(file_path, index=False)
            print(f"Data successfully saved to {file_path}")
        except Exception as e:
            raise Exception(f"Failed to save data to CSV: {e}")
        
    def load_data_from_csv(self, file_path='loan_payments.csv'):
        """
        Load data from a local CSV file into a pandas DataFrame.

        Args:
            file_path: Path to the CSV file (Defaults to loan_payments.csv)
        
        Returns:
            pandas.DataFrame: DaraFrame containing the loan payments data
        """
        try:
            df = pd.read_csv(file_path)
            print(f"Data successfully loaded from {file_path}")
            return df
        except FileNotFoundError:
            raise FileNotFoundError(
                f"CSV file not found at {file_path}. "
                "Please extract data from database first using extract_data() "
                "and save it using save_to_csv()"
            )


db_connector = RDSDatabaseConnector

loan_payments = db_connector.load_data_from_csv()
      