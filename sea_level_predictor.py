import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (10,5))
    ax.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Reference: https://www.youtube.com/watch?v=kHQmGTpiUKo
    # Create first line of best fit
    ## Fitting the Model using the training data
    lin_out = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    ## Creating the test set
    years_1880_2050 = pd.Series(list(range(1880, 2051)))
    ## Prediction from 1880 to 2050
    y_fit = years_1880_2050*lin_out[0]+lin_out[1]
    ## Plot the line
    ax.plot(years_1880_2050,y_fit)


    # Create second line of best fit
    ## Getting the training set from the dataset
    df_2000 = df[df['Year']>=2000]
    ## Fitting the model
    lin_out_2000 = linregress(df_2000['Year'],df_2000['CSIRO Adjusted Sea Level'])
    ## Creating the test set from 2000 to 2050
    years_2000_2051 = pd.Series(list(range(2000, 2051)))
    ## Prediction
    y_fit_2000 = years_2000_2051*lin_out_2000[0]+lin_out_2000[1]
    ## Plotting the line
    ax.plot(years_2000_2051,y_fit_2000,color = 'r')


    # Add labels and title
    ax.set(
        title ="Rise in Sea Level",
        xlabel = "Year",
        ylabel = "Sea Level (inches)",
        xlim = [1850,2075]
        )

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
