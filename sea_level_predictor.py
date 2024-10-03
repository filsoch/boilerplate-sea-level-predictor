import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=0.6, label='Sea Level')
    
    # Create first line of best fit
    reg_line = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    ax.plot(range(1880,2051), reg_line.intercept + reg_line.slope*range(1880,2051), 'r--', label='Prediction for 2013-2050 based\n on data since 1880')
    ax.legend()
    
    # Create second line of best fit
    df_2 = df[df['Year']>=2000]
    reg_line_2 = linregress(x=df_2['Year'], y=df_2['CSIRO Adjusted Sea Level'])
    ax.plot(range(2000,2051), reg_line_2.intercept + reg_line_2.slope*range(2000,2051), 'g--', label='Prediction for 2013-2050 based\n on data since 2000',)
    ax.legend()

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()