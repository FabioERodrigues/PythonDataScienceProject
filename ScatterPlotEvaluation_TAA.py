import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class ScatterPlotEvaluation_TAA:
    """
    Student Number: 31002744
    Student Name: Tina Azad Arjastan
    
    A class for creating and visualizing scatter plots of yearly mean open and close prices.

    Attributes:
        df (DataFrame): A pandas DataFrame containing financial data with datetime index.

    Methods:
        create_ScatterGraph: 
            Generates a scatter plot illustrating the yearly mean open and close prices from the provided DataFrame.
            The x-axis represents the years, while the y-axis represents the prices.
            The scatter plot displays two series: Yearly Mean Open Price and Yearly Mean Close Price.
            Data is resampled yearly to calculate the mean.
            This module code uses matplotlib and pandas libraries for plotting and data manipulation.
    """
    def __init__(self, df):
        """
        Constructor to initialise the dataframe
        
        Attributes:
        df (DataFrame): A pandas DataFrame containing financial data with datetime index.
        """
        self.df = df
        
    def create_ScatterGraph(self):
        """
        This creates a Scatter graph and displays the data shown below.
        """

        # Converting the index to datetime 
        self.df.index = pd.to_datetime(self.df.index)

        # Resampling the data to calculate the yearly mean
        yearly_mean = self.df.resample('Y').mean()

        # Plotting the yearly mean in a Scatter graph
        plt.figure(figsize=(12, 6))
        plt.scatter(yearly_mean.index, yearly_mean['Open Price'], label='Yearly Mean Open Price')
        plt.scatter(yearly_mean.index, yearly_mean['Close Price'], label='Yearly Mean Close Price')
        plt.xlabel('Year')
        plt.ylabel('Price')
        plt.title('Yearly Mean Open and Close Prices (Scatter Plot)')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()