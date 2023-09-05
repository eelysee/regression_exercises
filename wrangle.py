
import pandas as pd
import os

from env import get_connection
from sklearn.model_selection import train_test_split

# imports edroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, and fips from the zillow_2017 table
def get_zillow():
    filename = 'zillow.csv'
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else:
        query ='''
                SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
                FROM properties_2017
                WHERE propertylandusetypeid = 261
                ;
                '''
        
        url = get_connection('zillow')
        df = pd.read_sql(query,url)
        df.to_csv(filename, index=False)
        
        return df
    
    
# Dropping all null values
# Drops 12,628 observations    
def drop_zill(zillow):    
    zillow = zillow.dropna()
    zillow = zillow.rename(columns = {'bedroomcnt':'bed', 'bathroomcnt':'bath', 
                                  'calculatedfinishedsquarefeet': 'sqft', 'taxvaluedollarcnt': 'value', 
                                  'yearbuilt': 'year', 'taxamount':'tax'})
    return zillow



def train_val_test(df, seed = 55):
    train, val_test = train_test_split(df, train_size = 0.7,
                                       random_state = seed)
    
    val, test = train_test_split(val_test, train_size = 0.5,
                                 random_state = seed)
    
    return train, val, test

