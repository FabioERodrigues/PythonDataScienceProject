import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class StockPlotter_FR:
    """
   
    Student Name: Fabio Rodrigues
    StudentID: 31016067
   
   
    A class for plotting various aspects of stock data including high prices, low prices, and volume traded over time.
   
    This class provides functionalities to clean the data by removing outliers and to visualize the stock data through various kinds of         plots such as line plots and box plots. It is designed to work with dataframes that contain stock market data indexed by date.
   
    Attributes
    ----------
    df : DataFrame
        The dataframe containing stock market data.
    fig, ax1 : Figure and AxesSubplot
        The figure and the first axes subplot for plotting.
    ax2 : AxesSubplot
        The second axes subplot for plotting on a different y-axis scale.
    min_high_price : float
        Minimum 'High Price' in the dataframe after removing outliers.
    min_low_price : float
        Minimum 'Low Price' in the dataframe after removing outliers.
   
    Methods
    -------
    remove_outliers(columns):
        Removes outliers from specified columns in the dataframe.
    plot_high_price(color, linestyle):
        Plots the high price.
    plot_low_price(color, linestyle):
        Plots the low price.
    plot_boxplot_by_year():
        Plots a boxplot of closing prices by year.
    plot_boxplot_for_Volume():
        Plots a boxplot of volumes traded by year.
    show():
        Displays the plots.
    """
    # Constructor method to initialize the StockPlotter_FR instance
    def __init__(self, dataframe):
        """
        Initializes the StockPlotter_FR instance with a dataframe, sets up the plotting environment, and removes outliers from 'High Price'         and 'Low Price'.
       
        Parameters
        ----------
        dataframe : DataFrame
            The pandas DataFrame containing stock market data indexed by date.
        """
        self.df = dataframe  # Assign the passed dataframe to the instance variable
        self.remove_outliers(['High Price', 'Low Price']) # call methods to remove outliers
        self.fig, self.ax1 = plt.subplots(figsize=(12, 6)) # create a figure and subplot for plotting
        self.ax2 = self.ax1.twinx()
          # Calculate and store the minimum 'High Price' and 'Low Price' after removing outliers
        self.min_high_price = self.df['High Price'].min()#
        self.min_low_price = self.df['Low Price'].min()
        self.df.index = pd.to_datetime(self.df.index)
       
    def remove_outliers(self, columns):
        """
        Removes outliers from specified columns based on the Interquartile Range (IQR) method. This done as the data reset to 0 at the end of 2019.
       
        Parameters
        ----------
        columns : list of str
            The columns from which outliers will be removed.
       
        Returns
        -------
        None
            This method modifies the dataframe in place and does not return any value.
        """
        for column in columns:
           # Calculate the first and third quartiles and the IQR
            Q1 = self.df[column].quantile(0.25)
            Q3 = self.df[column].quantile(0.75)
            IQR = Q3 - Q1
            # Determine the lower and upper bounds for acceptable data points
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            # Filters the dataframe to only include rows where column values are within the bounds
            self.df = self.df[(self.df[column] >= lower_bound) & (self.df[column] <= upper_bound)]

    def plot_high_price(self, color='blue', linestyle='dotted'):
        """
        Plots the 'High Price' from 2009 to 2023 with specified color and linestyle.
       
        Parameters
        ----------
        color : str, optional
            The color of the line plot for 'High Price'.
        linestyle : str, optional
            The style of the line plot for 'High Price'.
       
        Returns
        -------
 
            This method plots the 'High Price' on ax1 and does not return any value.
        """
        # Plots the  'High Price' on the primary y-axis with specified color and linestyle
        self.ax1.plot(self.df.index, self.df['High Price'], color=color, label='High Price', linestyle=linestyle)
           # Set labels and title for the plot
        self.ax1.set_xlabel('Date')
        self.ax1.set_ylabel('High Price', color=color)
        self.ax1.set_ylim(3500, 8000)# Set the y-axis limits
        plt.title('Low and High Stock Price Over Time')
        self.ax1.set_yticks(range(4000, 8000, 500)) # Set y-axis tick marks
       
    def plot_low_price(self, color='red', linestyle='dashed'):
        """
        Plots the 'Low Price' from 2009 to 2023 with specified color and linestyle.
       
        Parameters
        ----------
        color : str, optional
            The color of the line plot for 'Low Price'.
        linestyle : str, optional
            The style of the line plot for 'Low Price'.
       
        Returns
        -------
            This method plots the 'Low Price' on ax2 and does not return any value.
        """
         # Plot 'Low Price' on the secondary y-axis with specified color and linestyle
        self.ax2.plot(self.df.index, self.df['Low Price'], color=color, label='Low Price', linestyle=linestyle)
           # Set the y-axis label and limits
        self.ax2.set_ylabel('Low Price', color=color)
        self.ax2.set_ylim(3500, 8000)
        self.ax2.set_yticks(range(4000, 8000, 500))
       
    def plot_boxplot_by_year(self):
        """
        Plots a boxplot of 'Close Price' by year to visualize the distribution of closing stock prices annually.
       
        Parameters
        ----------
        None
       
        Returns
        -------
            This method generates a boxplot and does not return any value.
        """
        self.df['Year'] = self.df.index.year
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='Year', y='Close Price', data=self.df)
          # Set the plot title and axis labels
        plt.title('Closing Stock Prices by Year')
        plt.xlabel('Year')
        plt.ylabel('Closing Stock Price')
        plt.show()   # Display the plot
       
    def plot_boxplot_for_Volume(self):
        """
        Plots a boxplot of 'Volume' traded by year to visualize the distribution of volumes traded annually.
       
        Parameters
        ----------
        None
       
        Returns
        -------
            This method generates a boxplot and does not return any value.
        """
        self.df['Year'] = self.df.index.year
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='Year', y='Volume', data=self.df)
        # Set the plot title and axis labels
        plt.title('Volume Traded Year by Year')
        plt.xlabel('Year')
        plt.ylabel('Volume')
        plt.show()# Display the plot
       
    def show(self):
        """
        Displays the generated plots with appropriate settings for ticks, grid, and layout.
       
        Parameters
        ----------
        None
       
        Returns
        -------
        None
            This method displays the plots and does not return any value.
        """
        plt.xticks(rotation=45) #Rotates the x axis for improved readability
        self.ax1.grid(True)#Enables grids
        self.fig.tight_layout() # # Adjust subplot parameters for a tight layout
        plt.show()  # Display all plots