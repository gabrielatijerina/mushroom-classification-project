
import pandas as pd
############### ACQUIRE DATA ###############
def get_mushroom_data():
    '''
    This function will pull the dataset from the provided .csv file and will write it to a pandas dataframe. To reproduce the results, you will need the mushrooms.csv file in your working directory.
    '''
    df = pd.read_csv('mushrooms.csv')  
    return df

