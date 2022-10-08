import pandas as pd


def remove_duplicates_from_change_hour(data: pd.DataFrame, column_date:str) -> pd.DataFrame:
    items_to_replace = ['1A', '1B', '2A', '2B']
    col_date = 'date'
    for item in items_to_replace:
        data[col_date] = data[col_date].str.replace(item, f'0{item[0]}')
    data.drop_duplicates(subset=[col_date], inplace=True)
    return data.reset_index(drop=True)