import pandas as pd

def to_csv(df: pd.DataFrame, path: str) -> None:
    """
    Save the dataframe to a csv file, by prepending the `dtypes` to the TOP of the dataframe.

    This is helpful when you are loading the dataframe from a csv file later and don't want to lose the types of the columns.

    Example:
    ```
    df = pd.read_csv('data.csv')
    # Some df.dtypes modification here (e.g. pd.to_datetime)
    to_csv(df, 'data_with_dtypes.csv')
    ```
    """
    # Copy the dataframe to prevent modifying the original one
    df_copy = df.copy()
    # Prepend dtypes to the top of df
    df_copy.loc[-1] = df_copy.dtypes
    df_copy.index = df_copy.index + 1
    df_copy.sort_index(inplace=True)
    # Then save it to a csv
    # Write the dataframe to a file. Create the file if it doesn't exist.
    with open(path, 'w') as f:
        df_copy.to_csv(f, index=False, lineterminator='\n')

def from_csv(path: str) -> pd.DataFrame:
    """
    Load the dataframe from a csv file, by reading the `dtypes` from the FIRST LINE of the file.
    In order to do this, the csv file must be created with the `to_csv()` method.

    Example:
    ```
    # Notebook 1
    to_csv(df, '../data/data_with_dtypes.csv')

    # Notebook 2
    df = from_csv('../data/data_with_dtypes.csv') # The dtypes are read from the first line of the file
    ```
    """
    # Read types first line of csv
    dtypes = pd.read_csv(path, nrows=1).iloc[0].to_dict()
    # Read the rest of the lines with the types from above
    return pd.read_csv(path, dtype=dtypes, skiprows=[1])