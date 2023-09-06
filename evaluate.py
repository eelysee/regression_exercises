import seaborn as sns
import matplotlib.pyplot as plt

# creates a residual plot
# plot_residuals(y, yhat): 

# returns the following values
def regression_errors(df): 
    sns.scatterplot(data=df,x=y_train, y='yhat')
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
    
'''    
sum of squared errors (SSE)

explained sum of squares (ESS)

total sum of squares (TSS)

mean squared error (MSE)

root mean squared error (RMSE)

baseline_mean_errors(y): computes the SSE, MSE, and RMSE for the baseline model

better_than_baseline(y, yhat): returns true if your model performs better than the baseline, otherwise false
'''