def check_df(dataframe, head=5, tail=5, quan=False):
    """
    Inspect basic properties of a Pandas DataFrame.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The DataFrame to be inspected.

    head : int, optional
        Number of rows to display from the head of the DataFrame. Default is 5.

    tail : int, optional
        Number of rows to display from the tail of the DataFrame. Default is 5.

    quan : bool, optional
        If True, display quantiles (summary statistics) of numeric columns. Default is False.

    Returns
    -------
    None

    Examples
    --------
    >>> check_df(dataframe)
    >>> check_df(dataframe, head=10, tail=10, quan=True)
    """
    print('########## Shape ##########')
    print(dataframe.shape)
    print('########## Types ##########')
    print(dataframe.dtypes)
    print('########## Head ##########')
    print(dataframe.head(head))
    print('########## Tail ##########')
    print(dataframe.tail(tail))
    print('########## NA ##########')
    print(dataframe.isnull().sum())
    if quan:
        print('########## Quantiles ##########')
        print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    Get the names of categorical, numerical, categorical that looks numerical and cardinal that looks categorical variables in the dataset.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The DataFrame from which variable names are to be extracted.

    cat_th : int, float, optional
        Threshold value for classifying numerical but categorical variables.

    car_th : int, float, optional
        Threshold value for classifying categorical but cardinal variables.

    Returns
    -------
    cat_cols : list
        List of categorical variable names.

    num_cols : list
        List of numerical variable names.

    cat_but_car : list
        List of categorical-looking cardinal variable names.

    Notes
    -------
    - cat_cols + num_cols + cat_but_car = total number of variables.
    - num_but_cat is included in cat_cols.
    - cat_th and car_th are user-selectable threshold values and can be adjusted based on the dataset.
    """
    # Categorical columns and categorical-looking but cardinal columns
    cat_cols = [col for col in dataframe.columns if str(dataframe[col].dtypes) in ['category', 'object', 'bool']]
    num_but_cat = [col for col in dataframe.columns if
                   dataframe[col].nunique() < cat_th and dataframe[col].dtypes in ['int', 'int32', 'int64', 'float',
                                                                                   'float32', 'float64']]
    cat_but_car = [col for col in dataframe.columns if
                   dataframe[col].nunique() > car_th and str(dataframe[col].dtypes) in ['category', 'object']]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # Numerical columns
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ['int64', 'float64']]
    num_cols = [col for col in num_cols if col not in cat_cols]

    # Print summary information
    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_but_cat: {len(num_but_cat)}")


def cat_summary(dataframe, col_name, plot=False):
    """
    This function provides summary statistics for a categorical variable and optionally displays a count plot.

    Parameters:
    - dataframe: pandas DataFrame
      The DataFrame to be analyzed.

    - col_name: str
      The name of the categorical variable for which summary statistics will be extracted.

    - plot: bool, optional, default: False
      If True, a count plot of the categorical variable will be displayed. Default is False.

    Returns:
    None

    Examples:
    --------
    cat_summary(data, 'Category_Column', plot=True)
    """
    # Create a frequency table for the categorical variable
    summary_df = pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                               'Ratio': 100 * dataframe[col_name].value_counts() / len(dataframe)})

    # Print the frequency table
    print(summary_df)
    print('####################')

    # If the plot parameter is True, plot a count plot
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


def num_summary(dataframe, numerical_col, plot=False):
    """
    Generate a summary of descriptive statistics for a numerical column and optionally display a histogram.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The DataFrame containing the numerical column.

    numerical_col : str
        The name of the numerical column for which the summary statistics will be generated.

    plot : bool, optional
        If True, a histogram of the numerical column will be displayed. Default is False.

    Returns
    -------
    None

    Notes
    -------
    - Descriptive statistics include count, mean, std, min, 5%, 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 95%, and 99% quantiles.
    """
    # Generate detailed quantiles
    quantiles = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    # Optionally, plot a histogram
    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


def target_summary_with_cat(dataframe, target, categorical_col):
    """
    Generate a summary of the mean of the target variable grouped by a categorical column.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The DataFrame containing the target and categorical columns.

    target : str
        The name of the target variable for which the mean will be calculated.

    categorical_col : str
        The name of the categorical column used for grouping.

    Returns
    -------
    None

    Notes
    -------
    - Calculates and prints the mean of the target variable for each category in the specified categorical column.
    """
    print(pd.DataFrame({'TARGET_MEAN': dataframe.groupby(categorical_col)[target].mean()}), end='\n\n\n')


def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: ['mean', 'median', 'std']}), end='\n\n\n')


def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    """
    Identify and optionally visualize highly correlated columns in a DataFrame.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The DataFrame to analyze for correlated columns.

    plot : bool, optional
        If True, a heatmap of the correlation matrix will be displayed. Default is False.

    corr_th : float, optional
        The correlation threshold above which columns are considered highly correlated. Default is 0.90.

    Returns
    -------
    drop_list : list
        List of column names that are highly correlated with other columns.

    Notes
    -------
    - Uses the Pearson correlation coefficient to measure correlation between columns.
    - Highly correlated columns are identified based on the specified threshold (corr_th).
    """
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]

    # Optionally, plot a heatmap
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (12, 12)})
        sns.heatmap(corr, cmap='RdBu')
        plt.show()

    return drop_list
