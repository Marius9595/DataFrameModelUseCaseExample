import pandas as pd


def filter_to_today_data(data: pd.DataFrame, column_date: str) -> pd.DataFrame:
    today_filter = pd.to_datetime(data[column_date]).dt.day == min(pd.to_datetime(data[column_date]).dt.day)+1
    return data[today_filter].reset_index(drop=True)