from datetime import datetime

from PeninsulaElectricDataSystem.extraction.extraction import extract_data_from_ree_on
from PeninsulaElectricDataSystem.transform.DataFrameModels.peninsula import PeninsularData
from PeninsulaElectricDataSystem.transform.transform import transform_to_peninsular_data_from


def get_data_on(date: datetime) -> PeninsularData:
    return transform_to_peninsular_data_from(
        extract_data_from_ree_on(date)
    )