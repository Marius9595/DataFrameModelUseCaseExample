import pandas as pd


def format_decimals(data: pd.DataFrame, column_to_exclude: str) -> pd.DataFrame:
    columns_to_format = list(data.columns.drop(column_to_exclude))
    data[columns_to_format] = round(data[columns_to_format].astype(float), 3)
    return data