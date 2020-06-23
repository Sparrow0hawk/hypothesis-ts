# some functions that work with pandas dataframes

def columnbiner(dataframe):
    """
    Multiplies two columns together and creates a new column with
    the result.
    """
    
    dataframe['byned'] = dataframe['a'] * dataframe['b']


def cleanify(dataframe, colname):
    """
    remove prefix from string column (based on colname)
    """
    
    cleaned_series = dataframe[colname].str.replace('pre','')

    dataframe[colname] = cleaned_series


