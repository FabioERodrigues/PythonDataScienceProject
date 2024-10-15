import matplotlib.pyplot as plt
import seaborn as sns

class HeatmapEvaluation_CSB:
    """
    Student Name: Camilo Sheldon Barreto
    Student Number: 31008527
    
    A class to plot a heatmap, to visualise the correlation between the features of the dataset and annotate each correlation as a percentage to 2 decimal places.
    
    Attributes
    ----------
        df : DataFrame
            The Dataframe to be plotted.
        columns : list
            The list of columns(features) to be plotted on the heatmap.
        figsize : int, optional
            The size of the figure to be plotted (default is 10).
        annotate_bool : bool, optional
            A boolean to indicate if each block should be annotated with a percentage of its correlation (default is False).
        cmap : str, optional
            The colormap to be used for the heatmap (default is PiYG).
        plot_title : str, optional
            The title for the heatmap
    
    Methods
    -------
        __init__(df)
            Initialises the HeatmapEvaluation_CSB object with the df dataframe.
        
        create_heatmap()
            Creates and displays a heatmap of the correlation among the features of the dataframe
    """
    
    def __init__(self, df, columns, figsize=10, annotate_bool=False, cmap='PiYG', plot_title="Default Title"):
        """
        Constructor to initialise the HeatmapEvaluation_CSB object with the df dataframe.
        
        Parameters
        ----------
        df : DataFrame
            The Dataframe to be plotted.
        columns : list
            The list of columns(features) to be plotted on the heatmap.
        figsize : int, optional
            The size of the figure to be plotted (default is 10).
        annotate_bool : bool, optional
            A boolean to indicate if each block should be annotated with a percentage of its correlation (default is False).
        cmap : str, optional
            The colormap to be used for the heatmap (default is PiYG).
        plot_title : str, optional
            The title for the heatmap
        """
        self.df = df
        self.columns = columns
        self.figsize = figsize
        self.annotate_bool = annotate_bool
        self.cmap = cmap
        self.plot_title = plot_title
        
    def create_heatmap(self):
        """
        Creates and displays a heatmap of the correlation among the features of the dataframe 
        """
        # Create a heatmap of the correlation between the columns specified
        corr = self.df[self.columns].corr()
        
        # The figure size for the plot
        plt.figure(figsize=(self.figsize,self.figsize))
        
        # Creating the heatmap
        sns.heatmap(corr, annot=self.annotate_bool, cmap=self.cmap, vmax=1, fmt='.2%')
        plt.title(self.plot_title)
        plt.show()
        
    def __str__(self):
        """
        String representation of the object.
        """
        return f"HeatmapEvaluation_CSB object. Dataframe shape: {self.df.shape}"
    
    def __repr__(self):
        """
        Representation of the object
        """
        return f"HeatmapEvaluation_CSB({self.df})"