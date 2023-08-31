
import pandas as pd
import os

from env import get_connection


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
        filename = pd.read_sql(query,url)
        filename.to_csv('zillow.csv', index=False)
        
        return filename
    
    
# Dropping all null values
# Drops 12,628 observations    
def drop_zill(zillow):    
    zillow = zillow.dropna()
    zillow = zillow.rename(columns = {'bedroomcnt':'bed', 'bathroomcnt':'bath', 
                                  'calculatedfinishedsquarefeet': 'sqft', 'taxvaluedollarcnt': 'value', 
                                  'yearbuilt': 'year', 'taxamount':'tax'})
    return zillow