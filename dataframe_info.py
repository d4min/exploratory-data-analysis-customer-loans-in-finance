import pandas as pd
import numpy as np 

class DataFrameInfo:
    """
    A utility class for extracting and analysing information from pandas DataFrames.
    """

    def __init__(self, df):
        """
        Initialise with a pandas DataFrame:
        
        Args:
            df: the DataFrame to analyse
        """
        self.df = df

    def get_basic_info(self):
        """
        Get basic information about the DataFrame including shape and data types.
        """
        print("DataFrame Shape:", self.df.shape)
        print("\nData Types Information:")
        return self.df.dtypes
    
    def get_statistical_summary(self, numeric_only=True):
        """
        Get statistical summary of numeric columns.

        Args:
            numeric_only: If True, include only numeric columns (Defaults to True)
        """
        stats = self.df.describe()
        if not numeric_only:
            stats = self.df.describe(include='all')
        return stats
    
    def get_null_info(self):
        """
        Get information about NULL values in each column.
        """
        null_counts = self.df.isnull().sum()
        null_percentages = (null_counts / len(self.df)) * 100

        null_info = pd.DataFrame({
            'Null Count': null_counts,
            'Null Percentage': null_percentages.round(2)
        })

        return null_info[null_info['Null Count'] > 0]
    
    def get_unique_counts(self, categorical_only=True):
        """
        Get count of unique values in columns.
        
        Args:
            categorical_only: If True, only show for object and category dtypes
        """
        if categorical_only:
            cat_columns = self.df.select_dtypes(include=['object', 'category']).columns
            unique_counts = self.df[cat_columns].nunique()
        else:
            unique_counts = self.df.nunique()
            
        return pd.DataFrame({'Unique Values': unique_counts})
    
    def get_column_summary(self, column):
        """
        Get detailed summary of a specific column.

        Args:
            column: name of the column to analyse
        """
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' not found in DataFrame")

        summary = {}
        summary['dtype'] = self.df[column].dtype
        summary['null_count'] = self.df[column].isnull().sum()
        summary['unique_count'] = self.df[column].nunique()
        
        if np.issubdtype(self.df[column].dtype, np.number):
            summary['mean'] = self.df[column].mean()
            summary['median'] = self.df[column].median()
            summary['std'] = self.df[column].std()
            summary['min'] = self.df[column].min()
            summary['max'] = self.df[column].max()
        
        if self.df[column].dtype == 'object' or self.df[column].dtype.name == 'category':
            summary['value_counts'] = self.df[column].value_counts().head()
            
        return summary

    def get_correlation_matrix(self, method='pearson'):
        """
        Get correlation matrix for numeric columns

        Args:
            method: the correlation method to use 'pearson', 'spearman' or 'kendall' (Defaults to 'pearson)
        """
        numeric_df = self.df.select_dtypes(include=[np.number])
        return numeric_df.corr(method=method)