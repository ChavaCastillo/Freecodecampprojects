import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('123_FCC\\ProyCert\\Sea Level Predictor\\epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(14,7))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label = 'Original Data')
    
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051)) #ajustar un año más porque... "Expected different line for first line of best fit.(shapes (170,), (171,) mismatch)"
    
    y_pred = intercept + slope * x_pred
    plt.plot(x_pred, y_pred, 'r', label='Fitted Line (1880-2050)')


    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_prend_recent = pd.Series(range(2000, 2051)) #ajustar un año más porque... "Expected different line for first line of best fit.(shapes (170,), (171,) mismatch)"
    y_pred_recent = intercept_recent + slope_recent * x_prend_recent
    plt.plot(x_prend_recent, y_pred_recent, 'g', label= 'Fitted Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()