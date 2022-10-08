from typing import List

import pandas as pd

from .DataFrameModels.peninsula import PeninsularData
from .cleaning.filter_to_today_data import filter_to_today_data
from .cleaning.normalize import normalize
from .cleaning.normalized_keys import NORMALIZED_KEYS
from .cleaning.remove_duplicates_from_change_hour import remove_duplicates_from_change_hour
from .formating.format_decimals import format_decimals


def transform_to_peninsular_data_from(data_extracted: List[dict]) -> PeninsularData:
    date_column = 'date'
    data_extracted = pd.DataFrame(data_extracted)
    data_normalized = normalize(data_extracted, NORMALIZED_KEYS)
    today_data = filter_to_today_data(data_normalized, date_column)
    data_cleaned = remove_duplicates_from_change_hour(today_data, date_column)
    data_formated = format_decimals(data_cleaned, date_column)
    return PeninsularData(data_formated)