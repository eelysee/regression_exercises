import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.metrics import mean_squared_error, explained_variance_score

# creates a residual plot
# plot_residuals(y, yhat): 

# returns the following values
def regression_errors(df): 
    sns.scatterplot(data=df,x='y_train', y='yhat')
    plt.axhline(0, color='firebrick')
    plt.title("Model Yhat Plot")
    plt.xlabel("Actual")
    plt.ylabel("Yhat")
    
    sns.scatterplot(data=df,x=y_train, y='residual')
    plt.axhline(0, color='firebrick')
    plt.title("Model Residual Plot")
    plt.xlabel("Actual")
    plt.ylabel("Residual")
    plt.show()
    
    
def f_y_mean(y_train):
    '''
    calculates the mean of y_train
    TAKES 1 array
    RETURNS 1 value
    '''
    y_mean = y_train.mean()
    return y_mean

#explained sum of squares (ESS)
def f_ess(yhat,y_mean):
    '''
    calculates the exlpained sum of squares
    TAKES in 2 arrays
    '''
    ess = sum((yhat-y_mean)**2)
    return ess 


def f_r2(y_train, yhat):
    '''
    calculates the explained variance score
    TAKES 2 df
    RETURNS one value
    REQUIREs from sklearn.metrics import explained_variance_score
    '''
    r2 = explained_variance_score(y_train,y_hat)
    
    return r2
    
    
def f_tss():
    '''
    calculates total sum of squares 
    RETURNS one value
    REQUIRES 
            FUNCTION f_ess(), f_sse()
    '''
    tss = f_ess() + f_sse()
    
    return tss


def f_mse(y_train, yhat):
    '''
    calculates mean squared error
    TAKES 2 DataFrames
    RETURNS one value
    REQUIRES from sklearn.metrics import mean_squared_error,
             import pandas as pd
    '''
    mse = mean_squared_error(y_train,yhat)
    
    return mse


def f_sse(y_train, y_hat):
    '''
    calculates the sum of squared errors
    RETURNS single value
    REQUIRES from sklearn.metrics import mean_squared_error,
            import pandas as pd,
            FUNCTION f_mse            
    '''
    sse = f_mse *(len(y_train))
    
    return sse

   
#root mean squared error (RMSE)
def f_rmse(y_train, yhat):
    '''
    calculates root of the mean squared error
    TAKES 2 DataFrames 
    RETURNS one number
    REQUIRES import math,
            from sklearn.metrics import mean_squared_error,
            import pandas as pd,
            FUNCTION: f_mse()
    
    '''
    rmse = sqrt(f_mse(y_train,yhat))
    
    return rmse


#baseline_mean_errors(y): computes the SSE, MSE, and RMSE for the baseline model

#better_than_baseline(y, yhat): returns true if your model performs better than the baseline, otherwise false


def mean_or_median_baseline(y_train):
    '''
    used for determining best baseline for regression test
    TAKES argument y_train(target variable). 
    - An array or df with one column.
    determins mean and median whicher has a lower RSME score
    RETURNS a dataframe with two columns
    REQUIRES from math import sqrt, 
            import pandas as pd, 
            from sklearn.metrics import mean_squared_error
    '''
    mean = y_train.mean()
    median = y_train.median()
    rsme_med = sqrt(mean_squared_error(y_train,))
    # rsme_mean =
    evals = pd.DataFrame({'actual':y_train})
    
    if sqrt(mean_squared_error) < rsme(median):
        evals['mean'] = mean
    else:
        evals['median'] = median
        
    return evals