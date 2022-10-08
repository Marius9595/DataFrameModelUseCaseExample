import datetime
import json
from typing import List

from .http_service import http_client


def _parse_data_to_records(dirty_data: str) -> List[dict]:
    data_parsable = dirty_data.split("(")[1].replace(");", "")
    key_access_data = 'valoresHorariosGeneracion'
    return json.loads(data_parsable)[key_access_data]


def extract_data_from_ree_on(date: datetime) -> List[dict]:
    return _parse_data_to_records(
        http_client.get_data_from_ree(date)
    )