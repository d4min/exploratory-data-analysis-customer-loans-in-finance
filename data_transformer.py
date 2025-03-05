import pandas as pd
import numpy as np

class DataTransform:
    """
    Class to handle datatype transformations and cleaning of loan payment data.
    """

    @staticmethod
    def convert_dates(df):
        """
        Convert date columns to datetime format.
        """
        date_columns = [
            'issue_date',
            'earliest_credit_line',
            'last_payment_date',
            'next_payment_date',
            'last_credit_pull_date'
        ]

        for col in date_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col])

        return df
    
    @staticmethod
    def convert_percentages(df):
        """
        Convert percentage strings to float values (e.g. '12.34% -> 0.1234)
        """
        percentage_columns = [
            'int_rate',
            'revol_util'
        ]

        for col in percentage_columns:
            if col in df.columns:
                df[col] = df[col].str.rstrip('%').astype('float') / 100.0
        
        return df
    
    @staticmethod
    def convert_currencies(df):
        """
        Convert currency strings to float values (e.g. '$1,234.56 _> 1234.56)
        """
        currency_columns = [
            'loan_amount',
            'funded_amount'
            'funded_amount_inv',
            'total_payment',
            'total_payment_inv',
            'total_rec_prncp',
            'total_rec_int',
            'total_rec_late_fee',
            'recoveries',
            'collection_recovery_fee',
            'last_payment_amount'
        ]
        
        for col in currency_columns:
            if col in df.columns:
                df[col] = df[col].replace('[\$,]', '', regex=True).astype(float)

        return df
    
    @staticmethod
    def convert_categorical(df):
        """
        Convert appropriate columns to categorical type.
        """
        categorical_columns = [
            'term',
            'grade',
            'sub_grade',
            'home_ownership',
            'verification_status',
            'loan_status',
            'purpose',
            'payment_plan',
            'application_type',
            'emp_length',
        ]
        
        for col in categorical_columns:
            if col in df.columns:
                df[col] = df[col].astype('category')

        return df
    
    def transform_data(self, df):
        """
        Apply all transformation to the DataFrame

        Args:
            df: orginial DataFrame 
        
        Returns:
            pandas.DataFrame: Transformed DataFrame
        """
        df = df.copy()  # Create a copy to avoid modifying the original

        # Apply all transformations
        df = self.convert_dates(df)
        df = self.convert_percentages(df)
        df = self.convert_currencies(df)
        df = self.convert_categorical(df)


        return df
    
         
