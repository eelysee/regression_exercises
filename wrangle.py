
import pandas as pd
import os

from env import get_connection
from sklearn.model_selection import train_test_split

# 
def get_zillow():
    '''
    imports bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, and fips from the zillow_2017 table
    
    cache's dataframe in a .csv
    '''
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
    
    
  
def drop_zill(zillow):    
    '''
    Dropping all null values
    Drops 12,628 observations  
    '''
    
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


def X_y_split(train, val, target):
    '''
    Splits train and val into X and Y splits for target testing.
    
    target is target variable entered as the name of the column only in quotes 
    
    returns X_train, y_train , X_val , y_val
    '''
    t = target
    X_train = train.drop(columns=[t])
    y_train = train[t]
    X_val = val.drop(columns=[t])
    y_val = val[t]
    return X_train, y_train , X_val , y_val