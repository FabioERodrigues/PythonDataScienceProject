import numpy as np
import pandas


class TrainTest_CO:
    """
    Student Name: Chids Osuala
    Student Number: 31012446 
    
    A class that is able to split columns in a dataframe into training and testing sets
    """

    def __init__(self, df, train_percent, independent, dependent):
        """
        Attributes:
        
        df - datframe to extract columns from
        train_percent - the percentage of the columns to be used for training set
        independent - the name of the column in the dataframe that will affect the prediction
        dependent - the name of the column in the dataframe that we are predicting
        
        """
        self.df = df
        self.independent = independent
        self.dependent = dependent
        self.train_size = int(len(self.df[independent]) * (train_percent/100))
    
    def create_sets(self):
        """
        creates the training sets and the data sets
        """
        sets = {"Training Sets" : [], "Testing Sets" : []}

        print(self.train_size)
        
        column1 = self.df[self.independent]
        column2 = self.df[self.dependent]

        sets["Training Sets"].append(column1[:self.train_size].to_numpy())
        sets["Training Sets"].append(column2[:self.train_size].to_numpy())

        sets['Testing Sets'].append(column1[self.train_size:].to_numpy())
        sets['Testing Sets'].append(column2[self.train_size:].to_numpy())
        return sets

    def getTrainSize(self):
        return self.train_size