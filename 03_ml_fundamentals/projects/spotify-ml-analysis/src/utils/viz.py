import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_style("white")


def plot_distribution(df, column, bins=30, kde=True, hist_color='C0', box_color='C1', figsize=(12, 4)):
    """
    Plots a histogram with KDE and a boxplot for a numeric column in a DataFrame.

    Parameters:
    - df: pandas DataFrame
    - column: str, column name to plot
    - bins: int, number of bins for histogram
    - kde: bool, whether to show KDE on histogram
    - hist_color: color for histogram
    - box_color: color for boxplot
    - figsize: tuple, size of the figure
    """

    fig, axes = plt.subplots(1, 2, figsize=figsize)

    # Histogram with KDE
    sns.histplot(df[column], bins=bins, kde=kde, ax=axes[0], color=hist_color)
    axes[0].set_title(f'{column} Distribution')
    axes[0].set_xlabel(column)
    axes[0].set_ylabel('Count')

    # Boxplot to show spread and outliers
    sns.boxplot(x=df[column], ax=axes[1], color=box_color)
    axes[1].set_title(f'{column} Boxplot')
    axes[1].set_xlabel(column)

    plt.tight_layout()
    plt.show()





def plot_all_distributions(df, numeric_only=True, bins=30, kde=True, hist_color='C0', box_color='C1', figsize=(12, 4)):
    """
    Plots histograms with KDE and boxplots for all numeric columns in a DataFrame.

    Parameters:
    - df: pandas DataFrame
    - numeric_only: bool, if True, only numeric columns are plotted
    - bins: int, number of bins for histograms
    - kde: bool, whether to show KDE on histograms
    - hist_color: color for histograms
    - box_color: color for boxplots
    - figsize: tuple, size of each subplot figure
    """
    if numeric_only:
        columns = df.select_dtypes(include='number').columns
    else:
        columns = df.columns

    for col in columns:
        fig, axes = plt.subplots(1, 2, figsize=figsize)

        # Histogram with KDE
        sns.histplot(df[col], bins=bins, kde=kde, ax=axes[0], color=hist_color)
        axes[0].set_title(f'{col} Distribution')
        axes[0].set_xlabel(col)
        axes[0].set_ylabel('Count')

        # Boxplot
        sns.boxplot(x=df[col], ax=axes[1], color=box_color)
        axes[1].set_title(f'{col} Boxplot')
        axes[1].set_xlabel(col)

        plt.tight_layout()
        plt.show()



