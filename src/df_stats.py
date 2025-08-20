import pandas as pd

def get_outliers_iqr(df: pd.DataFrame, column_name: str, iqr_multiplier: float = 1.5) -> pd.DataFrame:
    q1 = df[column_name].quantile(0.25)
    q3 = df[column_name].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - iqr * iqr_multiplier # By default, 1.5 multiplier is used
    upper_bound = q3 + iqr * iqr_multiplier
    return df[(df[column_name] < lower_bound) | (df[column_name] > upper_bound)]