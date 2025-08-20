import pandas as pd

def to_csv(df: pd.DataFrame, path: str) -> None:
    """Save the dataframe to a csv file, by prepending the dtypes to the top of the dataframe."""
    # Prepend dtypes to the top of df
    df.loc[-1] = df.dtypes
    df.index = df.index + 1
    df.sort_index(inplace=True)
    # Then save it to a csv
    # Write the dataframe to a file. Create the file if it doesn't exist.
    with open(path, 'w') as f:
        df.to_csv(f, index=False, lineterminator='\n')

def from_csv(path: str) -> pd.DataFrame:
    """Load the dataframe from a csv file, by reading the dtypes from the first line of the file."""
    # Read types first line of csv
    dtypes = pd.read_csv(path, nrows=1).iloc[0].to_dict()
    # Read the rest of the lines with the types from above
    return pd.read_csv(path, dtype=dtypes, skiprows=[1])