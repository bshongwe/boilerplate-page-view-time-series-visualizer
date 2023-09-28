import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import the data and set the index to the date column
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset
q25, q75 = df['page_views'].quantile([0.25, 0.75])
df = df[df['page_views'].between(q25, q75)]

# Define a function to draw a line plot
def draw_line_plot():
  # Create a figure
  fig = plt.figure()

  # Plot the line chart
  plt.plot(df.index, df['page_views'])

  # Set the title, labels, and legend
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  plt.xlabel('Date')
  plt.ylabel('Page Views')
  plt.legend(['Page Views'], loc='upper left')

  # Return the figure
  return fig

# Define a function to draw a bar plot
def draw_bar_plot():
  # Calculate the average daily page views for each month grouped by year
  df_bar = df.groupby(['year', 'month'])['page_views'].mean()

  # Create a figure
  fig = plt.figure()

  # Plot the bar chart
  plt.bar(df_bar.index, df_bar.values)

  # Set the title, labels, and legend
  plt.title('Average Daily Page Views by Month and Year')
  plt.xlabel('Years')
  plt.ylabel('Average Page Views')
  plt.legend(df_bar.index.levels[1], title='Months')

  # Rotate the x axis labels to prevent overlapping
  plt.xticks(rotation=45)

  # Return the figure
  return fig

# Define a function to draw two adjacent box plots
def draw_box_plot():
  # Create a figure
  fig = plt.figure()

  # Create the first box plot (year-wise)
  ax1 = sns.boxplot(
    x = 'year',
    y = 'page_views',
    showmeans=True,
    data=df
  )

  # Set the title and labels
  ax1.set_title('Year-wise Box Plot (Trend)')
  ax1.set_xlabel('Years')
  ax1.set_ylabel('Page Views')

  # Create the second box plot (month-wise)
  ax2 = sns.boxplot(
    x = 'month',
    y = 'page_views',
    showmeans=True,
    data=df
  )

  # Set the title and labels
  ax2.set_title('Month-wise Box Plot (Seasonality)')
  ax2.set_xlabel('Months')
  ax2.set_ylabel('Page Views')

  # Rotate the x axis labels to prevent overlapping
  ax2.set_xticks(rotation=45)

  # Adjust the layout
  plt.subplots_adjust(top=0.9)

  # Return the figure
  return fig

# Draw the line plot
fig = draw_line_plot()

# Save the line plot to a file
fig.savefig('line_plot.png')

# Draw the bar plot
fig = draw_bar_plot()

# Save the bar plot to a file
fig.savefig('bar_plot.png')

# Draw the box plot
fig = draw_box_plot()

# Save the box plot to a file
fig.savefig('box_plot.png')
