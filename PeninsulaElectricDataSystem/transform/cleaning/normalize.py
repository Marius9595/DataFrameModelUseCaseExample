import pandas as pd


def normalize(data: pd.DataFrame, relation_of_keys:dict) -> pd.DataFrame:
    data_normalized = data.rename(columns=_relation_of_old_and_new_keys(data, relation_of_keys))
    return data_normalized[relation_of_keys.values()]


def _relation_of_old_and_new_keys(data, new_keys: dict) -> dict:
    relation_old_with_new_keys = {}
    for old_key in data.columns:
        if old_key in new_keys.keys():
            relation_old_with_new_keys[old_key] = new_keys[old_key]
    return relation_old_with_new_keys